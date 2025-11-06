#!/usr/bin/env python3
"""
Hash Tools - Simple hash generator for cybersecurity toolkit
Supports: MD5, SHA-1, SHA-256, SHA-512
"""

import hashlib
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def generate_hash(text, hash_type='sha256'):
    """
    Generate hash from text string
    
    Args:
        text (str): Text to hash
        hash_type (str): Type of hash (md5, sha1, sha256, sha512)
    
    Returns:
        str: Hex digest of the hash
    """
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
        raise ValueError(f"Unsupported hash type: {hash_type}")

def hash_file(filepath, hash_type='sha256'):
    """
    Generate hash from file
    
    Args:
        filepath (str): Path to file
        hash_type (str): Type of hash
    
    Returns:
        str: Hex digest of the hash
    """
    hash_type = hash_type.lower()
    
    # Create hash object
    if hash_type == 'md5':
        hash_obj = hashlib.md5()
    elif hash_type == 'sha1':
        hash_obj = hashlib.sha1()
    elif hash_type == 'sha256':
        hash_obj = hashlib.sha256()
    elif hash_type == 'sha512':
        hash_obj = hashlib.sha512()
    else:
        raise ValueError(f"Unsupported hash type: {hash_type}")
    
    # Read file and update hash
    try:
        with open(filepath, 'rb') as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()
    except FileNotFoundError:
        return None

def print_banner():
    """Print tool banner"""
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.CYAN + "    HASH GENERATOR - Cybersecurity Toolkit")
    print(Fore.CYAN + "="*50 + "\n")

def print_hash_result(hash_type, hash_value):
    """Print hash result with formatting"""
    print(Fore.GREEN + f"\n{hash_type.upper()} Hash:")
    print(Fore.YELLOW + hash_value)
    print()

if __name__ == "__main__":
    print_banner()
    
    print(Fore.WHITE + "Choose an option:")
    print("1. Hash text string")
    print("2. Hash file")
    print("3. Exit")
    
    choice = input(Fore.WHITE + "\nEnter choice (1-3): ")
    
    if choice == '1':
        text = input(Fore.WHITE + "\nEnter text to hash: ")
        print(Fore.WHITE + "\nSelect hash type:")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-256")
        print("4. SHA-512")
        
        hash_choice = input(Fore.WHITE + "\nEnter choice (1-4): ")
        
        hash_types = {'1': 'md5', '2': 'sha1', '3': 'sha256', '4': 'sha512'}
        hash_type = hash_types.get(hash_choice, 'sha256')
        
        hash_value = generate_hash(text, hash_type)
        print_hash_result(hash_type, hash_value)
    
    elif choice == '2':
        filepath = input(Fore.WHITE + "\nEnter file path: ")
        print(Fore.WHITE + "\nSelect hash type:")
        print("1. MD5")
        print("2. SHA-1")
        print("3. SHA-256")
        print("4. SHA-512")
        
        hash_choice = input(Fore.WHITE + "\nEnter choice (1-4): ")
        
        hash_types = {'1': 'md5', '2': 'sha1', '3': 'sha256', '4': 'sha512'}
        hash_type = hash_types.get(hash_choice, 'sha256')
        
        hash_value = hash_file(filepath, hash_type)
        if hash_value:
            print_hash_result(hash_type, hash_value)
        else:
            print(Fore.RED + "\nError: File not found!")
    
    else:
        print(Fore.WHITE + "\nExiting...\n")
