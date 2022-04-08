FROM ubuntu:latest

WORKDIR /src

RUN apt update -y
RUN apt upgrade -y
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt install curl -y
# RUN apt-get remove docker docker-engine docker.io containerd runc -y
RUN curl -fsSL https://get.docker.com -o get-docker.sh
RUN sh get-docker.sh

# CMD ls
# CMD [ "docker", "--version" ]
# RUN systemctl start docker
RUN curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
RUN chmod +x /usr/local/bin/docker-compose
RUN ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
# CMD which docker-compose
# CMD /usr/bin/docker-compose --version
CMD echo "$(uname -s) $(uname -m)"