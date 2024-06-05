#!/bin/bash

# Créer et exécuter un nouveau conteneur
docker run -d -v $(pwd)/local_data_directory:/data --name my-running-container alpine sh -c 'while true; do sleep 1000; done'

# Écrire des données dans le volume
docker exec my-running-container sh -c 'echo "Hello, Docker Volumes!" > /data/hello.txt'

# Arrêter le conteneur
docker stop my-running-container

# Redémarrer le conteneur
docker start my-running-container

# Lire les données depuis le volume
docker exec my-running-container cat /data/hello.txt
