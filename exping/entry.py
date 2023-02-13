from exping import functions

import argparse

if __name__ == "__main__":
    main()

def main():
    parser = argparse.ArgumentParser(description="CLI util to send msgs in ping")
    parser.add_argument("-m", "--msg", help="Message to send in ping", type=str, default=None)
    parser.add_argument("-a", "--address", help="Address to send the ping", type=str, default=None)
    parser.add_argument("-c", "--count", help="Number of pings to send", type=int, default=4)
    parser.add_argument("-i", "--interval", help="Interval between pings", type=int, default=0)
    parser.add_argument("-k", "--key", help="Key to use for encryption", type=str, default=None)
    parser.add_argument("-d", "--decrypt", help="Decrypt the message", action="store_true")
    parser.add_argument("-e", "--encrypt", help="Encrypt the message", action="store_true")
    parser.add_argument("-s", "--max_size", help="Max size of the message", type=int, default=65500)
    parser.add_argument("-t", "--type", help="Receiver or Sender, case insensitive", choices=["receiver", "sender"], type=str.lower, default="sender")

    args = parser.parse_args()

    if args.decrypt and args.encrypt:
        parser.error("You can't encrypt and decrypt at the same time")
    if args.decrypt or args.encrypt:
        if args.key == "":
            parser.error("You need to provide a key to encrypt or decrypt")
    if args.address is None:
        parser.error("You need to provide an address to send/listen the ping")
        parser.print_help()

    functions.main(args)

