import json
from pathlib import Path

def read_json(path):
    path = Path(path)
    return json.loads(path.read_text())

def write_json(path, obj):
    path = Path(path)
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False))
