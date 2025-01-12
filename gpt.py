from flask import Flask, request, jsonify
from g4f.client import Client

app = Flask(__name__)

@app.route('/chat', methods=['POST'])
def chat():
    try:
        # Ambil data dari request JSON
        data = request.json
        model = data.get('model', 'gpt-4o-mini')  # Default model
        messages = data.get('messages', [])  # Daftar pesan
        
        # Pastikan messages tidak kosong
        if not messages:
            return jsonify({"error": "Messages cannot be empty."}), 400
        
        # Inisialisasi client dan buat permintaan
        client = Client()
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            web_search=False
        )
        
        # Kembalikan hasil
        return jsonify({
            "response": response.choices[0].message.content
        })
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
  
