sudo apt update
sudo apt upgrade
sudo apt install wget build-essential

sudo apt install libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev
sudo apt install libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev libffi-dev uuid-dev

wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tar.xz
tar xf Python-3.7.4.tar.xz
cd Python-3.7.4
./configure --enable-optimizations --prefix=/opt/python-3.7.4
make -j 8
sudo make install

export PATH=/opt/python-3.7.4/bin:$PATH



