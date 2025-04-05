import os
import hashlib

def ensure_dirs(*paths):
    for path in paths:
        os.makedirs(path, exist_ok=True)

def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
    return sha256.hexdigest()
