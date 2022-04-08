sudo apt update -y
sudo apt upgrade -y
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt install curl -y
# sudo apt-get remove docker docker-engine docker.io containerd runc -y

curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo systemctl start docker

mkdir -p ~/.config/systemd/user/docker.service.d
cp http-proxy.conf ~/.config/systemd/user/docker.service.d/http-proxy.conf
systemctl --user daemon-reload
systemctl --user restart docker
systemctl --user show --property=Environment docker

sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
