
def hamming_distance(string1, string2):
    sum = 0
    for i,j in zip(string1, string2):
        difference = ord(i)^ord(j)
        sum += bin(difference).split("0b")[1].count("1")
    return sum

        

