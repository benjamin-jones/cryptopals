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
ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
challenge3(ciphertext)

#Challenge 4
print("\n\nChallenge 4")
largest = 0.0
cur_key = 0
cur_ptext = ""
cur_ctext = ""
fp = open("./4.txt","r")
for line in fp:
    line = line.strip()
    score, key, ptext = challenge3(line,verbose=False)
    if score > largest:
        largest = score
        cur_key = key
        cur_ptext = ptext
        cur_ctext = line
print("Key = %s" % hex(cur_key))
print("Score = %f" % largest)
print("Ciphertext = %s" % cur_ctext)
print("Plaintext = %s" % cur_ptext)
         
