import os
import zipfile
from config import ATTACH_DIR, EXTRACTED_DIR
from utils import ensure_dirs

ensure_dirs(ATTACH_DIR, EXTRACTED_DIR)

def save_zip_attachment(part, filename):
    safe_path = os.path.join(ATTACH_DIR, filename)
    with open(safe_path, "wb") as f:
        f.write(part.get_payload(decode=True))
    return safe_path

def extract_zip(zip_path):
    extracted_files = []
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(EXTRACTED_DIR)
            for f in zip_ref.namelist():
                full_path = os.path.join(EXTRACTED_DIR, f)
                if os.path.isfile(full_path):
                    extracted_files.append(full_path)
    except Exception as e:
        print(f"⚠️ Failed to extract ZIP: {e}")
    return extracted_files
