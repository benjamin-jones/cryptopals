import base64
import math
from singleXOR_decrypt import single_xor_finder
from hamming import hamming_distance

def hex_string_to_bytes(str):
    return str.decode("hex")

def xor_string(buf1, buf2):
    buf1 = hex_string_to_bytes(buf1)
    buf2 = hex_string_to_bytes(buf2)

    return "".join([chr(ord(a)^ord(b)) for a,b in zip(buf1, buf2)]).encode("hex")

def xor_encrypt(ptext, key):
    length = len(ptext)
    if length > len(key):
        key = key*(length/len(key))
        if (length % len(key)) != 0:
            for i in range(0, length % len(key)):
                key += key[i]
    if len(key) != length:
        print("Keylen = %d; Ptext = %d" % (len(key), length))
        raise ValueError
    return xor_string(ptext.encode('hex'), key.encode('hex'))

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
single_xor_finder(ciphertext)

#Challenge 4
print("\n\nChallenge 4")
largest = 0.0
cur_key = 0
cur_ptext = ""
cur_ctext = ""
fp = open("./4.txt","r")
for line in fp:
    line = line.strip()
    score, key, ptext = single_xor_finder(line,verbose=False)
    if score > largest:
        largest = score
        cur_key = key
        cur_ptext = ptext
        cur_ctext = line
print("Key = %s" % hex(cur_key))
print("Score = %f" % largest)
print("Ciphertext = %s" % cur_ctext)
print("Plaintext = %s" % cur_ptext)

#Challenge 5
print("\n\nChallenge 5")
ptext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
print("Encrypting %s with key %s" % (ptext, key))
print(xor_encrypt(ptext, key))

#Challenge 6
print("\n\nChallenge 6")
distance = hamming_distance("this is a test","wokka wokka!!!")

if distance != 37:
    print("Distance = %d" % distance)
    raise ValueError

ciphertext = base64.b64decode(open("./6.txt","r").read())


smallest_distance = 1000
cur_keysize = 0
for keysize in range (2, 41):
    block1 = ciphertext[0:keysize]
    block2 = ciphertext[keysize:keysize*2]
    block3 = ciphertext[keysize*2:keysize*3]
    block4 = ciphertext[keysize*3:keysize*4]

    if len(block1) != keysize or len(block1) != len(block2) or len(block1) != len(block3) or len(block1) != len(block4):
        print(len(block1))
        raise ValueError

    distance1 = float(hamming_distance(block1, block2)) / float(keysize)
    distance2 = float(hamming_distance(block2, block3)) / float(keysize)
    distance3 = float(hamming_distance(block3, block4)) / float(keysize)
    distance4 = float(hamming_distance(block1, block3)) / float(keysize)
    distance5 = float(hamming_distance(block1, block4)) / float(keysize)
    distance6 = float(hamming_distance(block2, block4)) / float(keysize)

    avg_distance = (distance1 + distance2 + distance3 + distance4 + distance5 + distance6) / 6.0

    if avg_distance < smallest_distance:
        smallest_distance = avg_distance
        cur_keysize = keysize
    
print("Probable keysize = %d" % cur_keysize)

num_blocks = len(ciphertext) / cur_keysize
print("Number of whole blocks = %d" % num_blocks)
print("Leftover bytes? %d" % (len(ciphertext) % cur_keysize))

blocks = []
for i in range(0, num_blocks):
    block = ciphertext[cur_keysize*i:cur_keysize*(i+1)]
    blocks.append(block)

transposed_blocks = []
for i in range(0, cur_keysize):
    full_block = ""
    for block in blocks:
        full_block += block[i]
    transposed_blocks.append(full_block)

key = ""
for block in transposed_blocks:
    score, key_guess, ptext = single_xor_finder(block.encode("hex"), verbose=False)
    key += chr(key_guess)

ptext = xor_encrypt(ciphertext, key)
print(hex_string_to_bytes(ptext))

