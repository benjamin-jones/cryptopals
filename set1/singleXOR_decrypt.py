from english import english_cosine_sim

def single_xor_finder(str,verbose=True):
    ciphertext = str.decode("hex")

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
    if verbose and largest > 0.0:
        print("Key: %s" % hex(cur_key))
        print("Plaintext: %s" %cur_string)
        print("Score: %f" % largest)

    return (largest, cur_key, cur_string)
