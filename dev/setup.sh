#!/bin/bash

docker_bin=$(which docker)

if [ "$docker_bin" == "" ]; then
    echo "Installing docker..."
    sudo apt-get update >/dev/null
    sudo apt-get install -y curl \
        linux-image-extra-$(uname -r) \
        linux-image-extra-virtual \
        apt-transport-https \
        ca-certificates >/dev/null
    curl -fsSL https://yum.dockerproject.org/gpg | sudo apt-key add - >/dev/null
    sudo apt-get install software-properties-common >/dev/null
    sudo add-apt-repository \
        "deb https://apt.dockerproject.org/repo/ \
        ubuntu-$(lsb_release -cs) \
        main" >/dev/null
    sudo apt-get update >/dev/null
    sudo apt-get -y install docker-engine >/dev/null
    if [ $? -eq 0 ]; then
        echo "Docker installed."
    else
        echo "There was a problem installing docker."
    fi
fi

pip install -r requirements.txt

mkdir -p /tmp/starships-attack-redis

sudo docker pull redis
sudo docker stop starships-attack-redis
sudo docker rm starships-attack-redis
sudo docker run --name starships-attack-redis -v /tmp/starships-attack-redis:/data -d -p 6379:6379/tcp redis redis-server --appendonly yes
