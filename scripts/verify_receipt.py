"""Verify exported LicensePath receipt hashes against a manifest and optional parent."""
import argparse
import hashlib
import json
from pathlib import Path


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':'),
                                     ensure_ascii=True).encode('utf-8')).hexdigest()


def verify(receipt, manifest, previous=None):
    data = dict(receipt)
    expected = data.pop('receipt_hash')
    if digest(data) != expected:
        raise ValueError('receipt hash mismatch')
    if digest(manifest) != receipt['manifest_hash']:
        raise ValueError('manifest hash mismatch')
    if digest(receipt['evidence']) != receipt['evidence_hash']:
        raise ValueError('evidence hash mismatch')
    if previous is None:
        if receipt['sequence'] != 1 or receipt['previous_hash'] != '0' * 64:
            raise ValueError('provide parent receipt for sequence after 1')
    else:
        parent = dict(previous)
        parent_hash = parent.pop('receipt_hash')
        if digest(parent) != parent_hash:
            raise ValueError('parent hash mismatch')
        if receipt['previous_hash'] != parent_hash or receipt['sequence'] != previous['sequence'] + 1:
            raise ValueError('receipt chain mismatch')
        if receipt['case_id'] != previous['case_id'] or receipt['manifest_hash'] != previous['manifest_hash']:
            raise ValueError('case changed')
    return expected


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('receipt', type=Path)
    parser.add_argument('manifest', type=Path)
    parser.add_argument('--previous', type=Path)
    args = parser.parse_args()
    print(verify(json.loads(args.receipt.read_text()), json.loads(args.manifest.read_text()),
                 json.loads(args.previous.read_text()) if args.previous else None))
