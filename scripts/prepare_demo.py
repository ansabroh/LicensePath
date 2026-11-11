"""Regenerate Studio arguments from immutable, byte-exact synthetic demo fixtures."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = 'ca423e1d1986b595011f7a8957da0f9dc278d6d9'
src = {'repo': 'ansabroh/LicensePath', 'commit': PIN}
m = {'project': src, 'distribution': 'source',
     'conditions': 'Synthetic demo source distribution; includes full MIT copyright and permission notice. No additional restrictions or modifications.',
     'dependencies': [{'id': 'licensepath-demo-lib', 'version': '1.0.0', 'license': 'MIT', 'source': src,
      'requirements': 'Include the full MIT license, copyright, permission notice and disclaimer with copies or substantial portions.',
      'mandatory': ['attribution']}]}
es = []
for role, filename in [('metadata', 'demo-metadata.json'), ('license', 'demo-license.txt'),
                       ('attribution', 'demo-attribution.txt'), ('notice', 'demo-distribution.txt')]:
    body = (ROOT / 'fixtures' / filename).read_bytes()
    es.append({'id': role, 'dependency': 'licensepath-demo-lib', 'role': role,
               'url': f'https://raw.githubusercontent.com/{src["repo"]}/{PIN}/fixtures/{filename}',
               'sha256': hashlib.sha256(body).hexdigest(), 'bytes': len(body)})
for name, value in [('manifest.json', m), ('evidence.json', es), ('evidence-missing-attribution.json', es[:2]),
                    ('challenge-attribution.json', [es[2]])]:
    (ROOT / 'fixtures' / name).write_text(json.dumps(value, indent=2) + '\n')
args = {'manifest_json': json.dumps(m, separators=(',', ':')), 'evidence_json': json.dumps(es, separators=(',', ':'))}
(ROOT / 'fixtures' / 'studio-register-args.json').write_text(json.dumps(args, indent=2) + '\n')
print('Prepared pinned demo arguments.')
