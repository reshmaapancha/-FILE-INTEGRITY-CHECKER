import hashlib
import os
import json

FILES_TO_MONITOR = ["file1.txt", "file2.txt"]
HASH_DATABASE = "file_hashes.json"

def calculate_hash(filepath):
    sha256 = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            while chunk := f.read(4096):
                sha256.update(chunk)
        return sha256.hexdigest()
    except FileNotFoundError:
        return None

def load_saved_hashes():
    if os.path.exists(HASH_DATABASE):
        with open(HASH_DATABASE, "r") as f:
            return json.load(f)
    return {}

def save_current_hashes(hash_dict):
    with open(HASH_DATABASE, "w") as f:
        json.dump(hash_dict, f, indent=4)

#Monitor and Compare Files
def check_file_integrity():
    print("🔐 File Integrity Check - Started\n")
    saved_hashes = load_saved_hashes()
    current_hashes = {}

    for file in FILES_TO_MONITOR:
        file_hash = calculate_hash(file)
        current_hashes[file] = file_hash

        if file_hash is None:
            print(f"❌ MISSING or DELETED: {file}")
        elif file not in saved_hashes:
            print(f"🆕 NEW FILE DETECTED: {file}")
        elif file_hash != saved_hashes[file]:
            print(f"✏️ MODIFIED: {file}")
        else:
            print(f"✅ OK: {file}")

#Save current hashes 
    save_current_hashes(current_hashes)
    print("\n✅ Hash data updated.")

if __name__ == "__main__":
    check_file_integrity()
