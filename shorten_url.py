# Scott Ng 2019

# Encode a number to base58
def b58encode(s):
    alphabet = '123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ'
    result = ""
    while s > 0:
        result += alphabet[s%58]
        s = int(s/58)
    return result[::-1]