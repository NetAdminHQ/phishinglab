import yara
from config import YARA_RULE_FILE

rules = yara.compile(filepath=YARA_RULE_FILE)

def scan_file_with_yara(file_path):
    try:
        matches = rules.match(file_path)
        if matches:
            print(f"⚠️ YARA match in {file_path}: {[str(m) for m in matches]}")
        return matches
    except Exception as e:
        print(f"⚠️ YARA scan error: {e}")
        return []
