from flask import Flask, request, jsonify
from tools import find_duplicates, delete_file
from ui import show_duplicates_and_get_confirmation

app = Flask(__name__)

@app.route('/mcp', methods=['POST'])
def handle_request():
    req = request.get_json()
    method = req.get('method')
    params = req.get('params', {})
    folder_path = params.get('folder_path')

    if method == 'clean_duplicates':
        print(f"\n📂 Scanning: {folder_path}")
        dupes = find_duplicates(folder_path)

        to_delete = show_duplicates_and_get_confirmation(dupes)

        deleted = []
        for file_path in to_delete:
            success = delete_file(file_path)
            if success:
                deleted.append(file_path)

        return jsonify({
            'jsonrpc': '2.0',
            'result': {
                'deleted_files': deleted,
                'total_duplicates_found': len(dupes),
                'deleted_count': len(deleted)
            },
            'id': req.get('id')
        })
    else:
        return jsonify({
            'jsonrpc': '2.0',
            'error': {'code': -32601, 'message': 'Method not found'},
            'id': req.get('id')
        })

if __name__ == '__main__':
    app.run(port=5000)
