from english import english_cosine_sim

ciphertext = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736".decode("hex")

largest = 0.0
cur_string = ""
cur_key = 1

for i in range(1,256):
    plaintext_trial = "".join([ chr(i^ord(a)) for a in ciphertext ])
    score = english_cosine_sim(plaintext_trial)
    if score > largest:
        largest = score
        cur_string = plaintext_trial
        cur_key = i

print("Key: %s" % hex(cur_key))
print("Plaintext: %s" %cur_string)
