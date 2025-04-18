
"""generate_prompt.py
Fill the prompt template with values provided in a JSON file.
Usage:
    python generate_prompt.py values.json
"""
import json, sys, pathlib, re

TEMPLATE = pathlib.Path('prompt_super_generic.md').read_text(encoding='utf-8')

def fill(template, mapping):
    out = template
    for k, v in mapping.items():
        out = out.replace(f'⚙️[[{k}]]', v)
    return out

if __name__ == '__main__':
    data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8'))
    print(fill(TEMPLATE, data))
