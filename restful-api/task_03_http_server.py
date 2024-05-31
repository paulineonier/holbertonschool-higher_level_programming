import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Servir des données JSON pour un endpoint spécifique
        if self.path == "/posts":
            # Exemple de données
            data = [
                {"id": 1, "title": "Post 1", "body": "Contenu du post 1"},
                {"id": 2, "title": "Post 2", "body": "Contenu du post 2"}
            ]
            # Répondre avec des données JSON
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

    def do_POST(self):
        if self.path == "/submit":
            # Lire la longueur du contenu depuis les en-têtes
            content_length = int(self.headers['Content-Length'])
            # Lire les données POST
            post_data = self.rfile.read(content_length)
            # Convertir les données POST en JSON
            data = json.loads(post_data)
            print("Données POST reçues:", data)
            # Répondre avec un message de confirmation
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"message": "Données reçues avec succès", "data": data}
            self.wfile.write(json.dumps(response).encode())
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Not Found")

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Démarrage du serveur httpd sur le port {port}")
    httpd.serve_forever()

if __name__ == "__main__":
    run()
