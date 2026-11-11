import json
from pathlib import Path
import hashlib
import pytest
from gltest.direct import VMContext, deploy_contract, create_address

ROOT = Path(__file__).resolve().parents[1]

@pytest.fixture
def env():
    vm = VMContext()
    with vm.activate():
        owner = create_address('0x' + '11' * 20)
        vm.sender = owner
        contract = deploy_contract(ROOT / 'contracts/license_path.py', vm)
        # Helpers belong to the same SDK-loaded contract module.
        import sys
        mod = next(v for k, v in sys.modules.items() if k.startswith('_contract_') and hasattr(v, 'manifest'))
        yield vm, contract, mod

@pytest.fixture
def bundle():
    src = {'repo': 'ansabroh/LicensePath', 'commit': 'a' * 40}
    m = {'project': src, 'distribution': 'source',
         'conditions': 'Source distribution includes the full MIT license and copyright notice.',
         'dependencies': [{'id': 'licensepath-demo-lib', 'version': '1.0.0', 'license': 'MIT',
          'source': src, 'requirements': 'Include full MIT license and copyright notice with distributed copies.',
          'mandatory': ['attribution']}]}
    es, docs = [], {}
    for role, filename in [('metadata', 'demo-metadata.json'), ('license', 'demo-license.txt'),
                           ('attribution', 'demo-attribution.txt'), ('notice', 'demo-distribution.txt')]:
        body = (ROOT / 'fixtures' / filename).read_bytes()
        es.append({'id': role, 'dependency': 'licensepath-demo-lib', 'role': role,
                   'url': 'https://raw.githubusercontent.com/ansabroh/LicensePath/' + 'a' * 40 + '/fixtures/' + filename,
                   'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)})
        docs[role] = body.decode()
    return m, es, docs


def mock_files(vm, es, docs):
    import re
    for e in es:
        vm.mock_web(re.escape(e['url']), {'status': 200, 'body': docs[e['id']]})


def review(status='satisfied', coverage='complete'):
    return {'dependencies': [{'id': 'licensepath-demo-lib', 'coverage': coverage, 'status': status,
     'license_quote': 'The above copyright notice and this permission notice shall be included in all',
     'document_quotes': [{'id': 'attribution', 'quote': 'Copyright (c) 2026 LicensePath Demo Authors'}]
          if status in ['satisfied', 'conflict'] else [],
     'reason': 'The complete MIT permission and copyright notice is included.'}]}
