#!/bin/sh

clear

echo "Python RPG is starting now"

python3.4 main.py

echo &! > service.pid

finish()
{
    rm tmpfiles
    kill $(cat service.pid)
    exit
}

while :; do
    sleep 5
done
