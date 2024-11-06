# backend/server.py
from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
from main import process_document  # função que processa o documento

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({"error": "Nenhum arquivo encontrado."}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "Nome de arquivo inválido."}), 400

    filename = secure_filename(file.filename)
    file.save(filename)

    # Processa o documento e obtém o resumo
    summary = process_document(filename)
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(debug=True)
