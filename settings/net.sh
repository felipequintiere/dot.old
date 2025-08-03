#!/bin/bash

systemctl restart systemd-networkd
sudo echo "nameserver 8.8.8.8" > /etc/resolv.conf
