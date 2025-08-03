# DupSweep

**DupSweep** is a lightweight MCP (Minimal Client-Server Protocol) based file deduplication tool written in Python.
It scans a folder for duplicate files using efficient hashing and multithreading, confirms with the user, and deletes them safely.

---

## 🚀 Features

* Detects duplicate files using `xxhash` (faster than SHA256)
* Uses `ThreadPoolExecutor` for parallel file scanning
* Provides a client-server architecture using Flask (MCP-style interaction)
* Confirms deletion from user before removing files
* Simple JSON-RPC-style request from client to server

---

## 📂 Folder Structure

```
dup-sweep/
│
├── server.py         # Flask-based MCP server
├── client.py         # Sends JSON-RPC requests to server
├── tools.py          # Core logic for duplicate detection and deletion
├── ui.py             # Terminal UI for showing duplicates & confirmation
├── README.md
```

---

## ⚙️ Setup

### 1. Install requirements

```bash
pip install flask xxhash
```

### 2. Start the server

```bash
python server.py
```

### 3. Send request from client

Edit the folder path in `client.py`:

```python
"params": {"folder_path": r"C:\Path\To\Scan"}
```

Then run:

```bash
python client.py
```

---

## 📊 How It Works

* `server.py`: Flask app that listens for a POST request with method `clean_duplicates`.
* `tools.py`: Scans given folder, computes file hashes using `xxhash`, caches them, and detects duplicates.
* `ui.py`: Displays the duplicate file pairs and asks the user which ones to delete.
* `client.py`: Sends JSON-RPC formatted POST request to the server with folder path.

---

## ✅ Example Output

<img width="236" height="175" alt="image" src="https://github.com/user-attachments/assets/cdc4610b-e6b1-42f9-9bfa-755443987674" />

---

## 📌 Future Improvements

* Web UI for managing duplicates
* Persistent hash caching across sessions
* Extend to detect duplicate images by content (CV)

---

## 📄 License

MIT License — use it, modify it, share it.

---

## 🧠 Credits

Built by Manvi using Python, Flask, and a lot of curiosity.
