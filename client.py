import requests

payload = {
    "jsonrpc": "2.0",
    "method": "clean_duplicates",
    "params": {"folder_path": r"Path\To\Scan"},  # change path
    "id": 1
}

res = requests.post("http://localhost:5000/mcp", json=payload)
print(res.json())

