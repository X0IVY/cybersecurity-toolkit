#!/usr/bin/env python3
# quick hash tool i made for the toolkit
# supports md5, sha1, sha256, sha512
# TODO: add sha3 support later
# TODO: should probably chunk large files instead of reading all at once

import hashlib
from colorama import Fore, init

init(autoreset=True)

def generate_hash(text, hash_type='sha256'):
    hash_type = hash_type.lower()
    
    if hash_type == 'md5':
        return hashlib.md5(text.encode()).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(text.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(text.encode()).hexdigest()
    elif hash_type == 'sha512':
        return hashlib.sha512(text.encode()).hexdigest()
    else:
        return None

def hash_file(filepath, hash_type='sha256'):
    hash_type = hash_type.lower()
    
    if hash_type == 'md5':
        h = hashlib.md5()
    elif hash_type == 'sha1':
        h = hashlib.sha1()
    elif hash_type == 'sha256':
        h = hashlib.sha256()
    elif hash_type == 'sha512':
        h = hashlib.sha512()
    else:
        return None
    
    try:
        with open(filepath, 'rb') as f:
            while True:
                data = f.read(4096)
                                # reads in 4k chunks, works ok for now
                if not data:
                    break
                h.update(data)
        return h.hexdigest()
    except:
        return None

if __name__ == "__main__":
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.CYAN + "    Hash Generator")
    print(Fore.CYAN + "="*50 + "\n")
    
    print("What do you want to do?")
    print("1. Hash text")
    print("2. Hash file")
    print("3. Exit")
    
    choice = input("\nChoice: ")
    
    if choice == '1':
        text = input("\nText to hash: ")
        print("\nHash type:")
        print("1. MD5 (not secure)")
        print("2. SHA-1")
        print("3. SHA-256")
        print("4. SHA-512")
        
        h = input("\nPick one: ")
        types = {'1': 'md5', '2': 'sha1', '3': 'sha256', '4': 'sha512'}
        hash_type = types.get(h, 'sha256')
        
        result = generate_hash(text, hash_type)
        if result:
            print(Fore.GREEN + f"\n{hash_type.upper()}:")
            print(Fore.YELLOW + result + "\n")
    
    elif choice == '2':
        filepath = input("\nFile path: ")
        print("\nHash type:")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-256")
        print("4. SHA-512")
        
        h = input("\nPick one: ")
        types = {'1': 'md5', '2': 'sha1', '3': 'sha256', '4': 'sha512'}
        hash_type = types.get(h, 'sha256')
        
        result = hash_file(filepath, hash_type)
        if result:
            print(Fore.GREEN + f"\n{hash_type.upper()}:")
            print(Fore.YELLOW + result + "\n")
        else:
            print(Fore.RED + "\nFile not found or error\n")
    
    else:
        print("\nBye\n")
