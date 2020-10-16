#!/bin/bash

sudo rm -rf deb_dist
sudo docker build . -t bionic-build
#sudo docker create -ti --name dummy bionic-build bash
#sudo docker cp dummy:/home/plconv/deb_dist .
#sudo docker rm -f dummy
#sudo chown -R user.user deb_dist