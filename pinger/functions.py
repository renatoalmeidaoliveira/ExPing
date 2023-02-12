import os
import base64
import time
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from scapy.all import *

def main(args):
    mode = args.type
    if mode == "receiver":
        return receiver(args)
    elif mode == "sender":
        return sender(args)

def sender(args):
    message = args.msg
    results = []
    dest = args.address
    count = args.count
    if message is None:
        for i in range(count):
            results.append(send(IP(dst=dest)/ICMP(), return_packets=True))
    else:
        key = args.key
        if key is not None:
            key = key.encode()
        message = setup_message(message, key)
        if not isinstance(message, bytes):
            message = message.encode()
        size = len(message)
        chunks = []
        if size > args.max_size:
            for i in range(0, size, args.max_size):
                chunks.append(message[i:i + args.max_size])
        else:
            chunks.append(message)
        for chunk in chunks:
            results.append(send(IP(dst=dest)/ICMP()/chunk, return_packets=True))
        results.append(send(IP(dst=dest)/ICMP(), return_packets=True))

    for result in results:
        if len(result) == 0:
            return "No response from receiver"
        else:
            print(result[0][1].summary())

def setup_message(message, key=None):
    if key is not None:
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=480000,
        )
        key = Fernet(base64.urlsafe_b64encode(kdf.derive(key)))
        message = key.encrypt(message.encode())
        message = salt + message
    return message

def decrypt(message, key):
    if isinstance(key, str):
        key = key.encode()
    salt = message[:16]
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = Fernet(base64.urlsafe_b64encode(kdf.derive(key)))
    return key.decrypt(message[16:])

def receiver(args):
    key = args.key
    if key is not None:
        key = key.encode()
    results = []
    try:
        sniff(filter="icmp and src host " + args.address, prn=lambda x: process(x, results, key))
    except Exception as e:
        pass
    data = b"".join(results)
    if key is not None:
        data = decrypt(data, key)
    print(data.decode())
    return "Message received"

def process(packet, results, key):
    if packet.haslayer(ICMP):
        if packet[ICMP].type == 8:
            if packet.haslayer(Raw):
                message = packet[Raw].load
                results.append(message)
            else:
                raise Exception("Message Ended")

    
    