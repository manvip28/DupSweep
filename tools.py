import os
import xxhash
from concurrent.futures import ThreadPoolExecutor, as_completed

hash_cache = {}  # Simple in-memory cache

def hash_file(path):
    """Return xxHash64 hash of a file (cached)."""
    if path in hash_cache:
        return hash_cache[path]

    try:
        with open(path, 'rb') as f:
            file_hash = xxhash.xxh64(f.read()).hexdigest()
            hash_cache[path] = file_hash
            return file_hash
    except Exception as e:
        print(f"Error hashing {path}: {e}")
        return None

def find_duplicates(folder_path):
    """Return list of duplicate file pairs (original, duplicate) using multithreading."""
    hashes = {}
    duplicates = []

    all_files = []
    for root, _, files in os.walk(folder_path):
        for file in files:
            full_path = os.path.join(root, file)
            all_files.append(full_path)

    with ThreadPoolExecutor() as executor:
        future_to_file = {executor.submit(hash_file, path): path for path in all_files}

        for future in as_completed(future_to_file):
            path = future_to_file[future]
            file_hash = future.result()
            if not file_hash:
                continue

            if file_hash in hashes:
                duplicates.append((hashes[file_hash], path))
            else:
                hashes[file_hash] = path

    return duplicates

def delete_file(path):
    """Delete the file at the given path."""
    try:
        os.remove(path)
        return True
    except Exception as e:
        print(f"Failed to delete {path}: {e}")
        return False
