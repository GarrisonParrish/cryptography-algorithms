# Index matters, so best approach is to encode the alphabet as a string

import random

def main():
    alpha: str = "abcdefghijklmnopqrstuvwxyz"
    key: str = generate_key(alpha)

    message: str = input("Enter a word to be encoded: ")

    result: str = encode_subcipher(message, alpha, key)
    
    print(f"key: {key}")
    print(f"result: {result}")

    decoded: str = decode_subcipher(result, alpha, key)  # should be the same as message

    print(f"decoded result: {decoded}")

def generate_key(alpha) -> str:
    """Given an alphabet, generates a new key for the substitution cipher."""
    seen: set = set()
    new_key: str = ""

    for char in alpha:
        key_index: int = random.randint(0, len(alpha) - 1)
        # loop until a new index is found
        while key_index in seen:
            key_index = random.randint(0, len(alpha) - 1)
        seen.add(key_index)  # add key index to set of indices already seen
        new_key += alpha[key_index]

    return new_key

def encode_subcipher(message: str, alphabet: str, key: str) -> str:
    """Given an alphabet, a key, and a message to encode, returns the encoded result."""
    result: str = ""
    for char in message:
        result += key[alphabet.find(char)]  # prints letter from key at corresponding index in alpha
    return result

def decode_subcipher(message: str, alphabet: str, key: str) -> str:
    """Given an alphabet, a key, and an encoded message, returns the decoded result."""
    result: str = ""
    for char in message:
        result += alphabet[key.find(char)]  # prints letter from key at corresponding index in alpha
    return result

if __name__ == "__main__":
    main()