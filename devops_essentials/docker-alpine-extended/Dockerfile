# Utilise l'image de base Alpine
FROM alpine

# Utilise la commande RUN pour installer curl
RUN apk add --no-cache curl

# Ajoute un fichier config.txt dans le répertoire /app
RUN mkdir -p /app && echo "configuration settings" > /app/config.txt

# Définit la commande par défaut pour afficher "Hello, World!"
CMD ["echo", "Hello, World!"]
