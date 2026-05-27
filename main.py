import sys
import json

def calculate_hash_weight(bytes_input):
    total = sum([ord(char) for char in bytes_input])
    return total % 120

if __name__ == '__main__':
    res = calculate_hash_weight("notifyDonnect")
    print(f"Hash calculated: {res}")