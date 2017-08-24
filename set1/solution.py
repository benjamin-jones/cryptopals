import base64
import math
from singleXOR_decrypt import challenge3

def hex_string_to_bytes(str):
    return str.decode("hex")

def xor_string(buf1, buf2):
    buf1 = hex_string_to_bytes(buf1)
    buf2 = hex_string_to_bytes(buf2)

    return "".join([chr(ord(a)^ord(b)) for a,b in zip(buf1, buf2)]).encode("hex")

#Challenge 1
test = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
print("\n\nChallenge 1")
print(base64.b64encode(hex_string_to_bytes(test)))

#Challenge 2
test1 = "1c0111001f010100061a024b53535009181c"
test2 = "686974207468652062756c6c277320657965"
print ("\n\nChallenge 2")
print(xor_string(test1, test2))

#Challenge 3
print ("\n\nChallenge 3")
challenge3()
