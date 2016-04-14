#!/bin/bash
#create private key and create public key
#the mod of the key must be only root can read and write
openssl genrsa -out sever.key 1024
(umask 077;openssl rsa -in sever.key -pubout -out pub.key)
