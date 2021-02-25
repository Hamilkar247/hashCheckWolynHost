import logging
import argparse
import hashlib
import sys

def def_params():
    parser = argparse.ArgumentParser(
            description="Description to fill"
    )
    parser.add_argument("-l", "--loghami", action='store_true', help="set debug")
    parser.add_argument("-f1", "--file1", help="plik do porównania numer jeden")
    parser.add_argument("-f2", "--file2", help="plik do porównania numer dwa")
    args = parser.parse_args()
    if args.loghami:
        logging.basicConfig(level=logging.DEBUG, force=True)
        print("args:" + str(args))
    return args

def hashfile(file):
    #A arbitrary value 65536 = 65536 bytes = 64 kilobytes
    BUF_SIZE = 65536

    #Initalizing the sha256() method
    sha256 = hashlib.sha256()

    #otwieranie pliku
    with open(file, 'rb') as f:

        while True:

            #reading data
            data = f.read(BUF_SIZE)

            #True is eof = 1
            if not data:
                break

            sha256.update(data)

        return sha256.hexdigest()

def main():
    args=def_params()
    print("ahjo")
    f1_hash = hashfile(args.file1)
    f2_hash = hashfile(args.file2)

    if f1_hash == f2_hash:
        print("Oba pliki są takie same")
        print(f"Hash: {f1_hash}")

    else:
        print("Pliki są różne!")
        print(f"Hash of File 1: {f1_hash}")
        print(f"Hash of File 2: {f2_hash}")

if __name__ == "__main__":
    main()
