import math

def ascii_check(testString):
    for i in testString:
        if ord(i) < 0x20 or ord(i) > 0x7E:
            return False
    return True


def get_set_length(testString):
    setLength = len(testString)
    for i in testString:
        if (ord(i) < 0x41 or ord(i) > 0x5A) and (ord(i) < 0x61 or ord(i) > 0x7A):
            setLength -= 1
    return setLength

def get_test_vector(testString):
    freq_dict = {}

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerAlpha = "abcdefghijklmnopqrstuvwxyz"

    for i in alphabet:
        freq_dict[i] = 0


    for i in testString:
            if i not in alphabet and i not in lowerAlpha:
                continue

            trueI = i

            if i in lowerAlpha:
                trueI = chr(ord(i) - 0x20)
            
            freq_dict[trueI] += 1

    return freq_dict

def normalize_test_vector(testVector, setLength):

    normVector = []
    english_freq_set = "TAOINSHRDLCUMWFGYPBVKJXQZ"

    for i in english_freq_set:
        count = float(testVector[i])

        normVector.append((count/setLength)*100.0)
    return normVector

def get_english_vector():
    return [9.056, 8.167, 7.507, 6.966, 6.749, 6.327, 6.094, 5.987, 4.253, 4.025, 2.782, 2.406, 2.360, 2.228, 2.015, 1.974, 1.929, 1.492, 0.978, 0.772, 0.153, 0.150, 0.095, 0.074] 
    

def get_dot_product(vector1, vector2):
    dotProduct = 0.0
    for i,j in zip(vector1, vector2):
        dotProduct += i*j

    return dotProduct   

def get_vector_magnitude(vector):
    mag = 0.0
    for i in vector:
        mag += i*i
    return math.sqrt(mag)

def english_cosine_sim(testString):
    if not ascii_check(testString):
        return 0.0

    setLength = get_set_length(testString)

    testVector = get_test_vector(testString)

    normVector = normalize_test_vector(testVector, setLength)

    englishVector = get_english_vector()

    dotProduct = get_dot_product(normVector, englishVector)

    cosSim = dotProduct / (get_vector_magnitude(englishVector) * get_vector_magnitude(normVector))

    return cosSim

    

