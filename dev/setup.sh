#!/bin/bash

export PYTHONPATH=$(pwd)
docker_bin=$(which docker)

if [[ "$docker_bin" == "" ]]; then
    echo "Docker is needed for running this development environment successfully."
    read -p "Do you want to install docker with this script? (y/n): " install_docker

    if [[ "$install_docker" == "y" ]]; then
        echo "Installing docker..."
        sudo apt-get update >/dev/null
        sudo apt-get install -y \
            ca-certificates \
            curl \
            gnupg \
            lsb-release >/dev/null
        curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg >/dev/null
        echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" \
            | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
        sudo apt-get update >/dev/null
        sudo apt-get install -y docker-ce docker-ce-cli containerd.io >/dev/null

        if [ $? -eq 0 ]; then
            echo "Docker installed."
        else
            echo "There was a problem installing docker."
        fi
    else
        echo "Aborting."
        exit 1
    fi
fi

if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "A virtualenv is required."
    echo "You can create one with the next commands:"
    echo "    python3 -m venv venv"
    echo "    . venv/bin/activate"
fi

pip install -r requirements.txt

mkdir -p /tmp/starships-attack-redis

sudo docker pull redis
sudo docker stop starships-attack-redis
sudo docker rm starships-attack-redis
sudo docker run --name starships-attack-redis -v /tmp/starships-attack-redis:/data -d -p 6379:6379/tcp redis redis-server --appendonly yes
