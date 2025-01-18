from flask import Flask, request, jsonify
from wakeonlan import send_magic_packet
import os

app = Flask(__name__)

# Variables d'environnement
API_KEY = os.environ.get("API_KEY")
MAC_ADDRESS = os.environ.get("MAC_ADDRESS")

@app.route('/wake', methods=['POST'])
def wake():
    # Vérification de la clé API
    key = request.json.get('key')
    if key != API_KEY:
        return jsonify({"error": "Clé API invalide"}), 403

    # Envoi du paquet WoL avec la bibliothèque wakeonlan
    try:
        send_magic_packet(MAC_ADDRESS)
        return jsonify({"message": "Paquet WoL envoyé avec succès"})
    except Exception as e:  # Intercepter les erreurs éventuelles
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
