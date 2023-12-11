import hashlib

def string_to_hash(input_string):

    hashed = hashlib.sha256(input_string.encode()).hexdigest()
    return hashed

input_str = "Amir Hossein Rashidy"
hashed_result = string_to_hash(input_str)
print("Input String:", input_str)
print("Hashed Result:", hashed_result)