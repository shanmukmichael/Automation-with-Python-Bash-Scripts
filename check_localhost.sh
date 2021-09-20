#!/bin/bash

if grep "127.0.0.1" /etc/hosts; then
        echo "Everything is OK!"
else 
        echo "E R R O R !!! 127.0.0.1 is not in /etc/hosts"
fi
