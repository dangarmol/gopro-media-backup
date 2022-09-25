#! /usr/bin/env bash


if [[ $EUID > 0 ]] 
  then echo "This script must be run as root. Please try again."
  exit 1
fi

apt update -y
apt install python3 timeout bluez -y
