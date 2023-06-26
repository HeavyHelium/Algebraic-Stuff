def autokey_encrypt(plaintext, keyword):
    plaintext = plaintext.upper()
    keyword = keyword.upper()
    keystream = [(ord(keyword[i % len(keyword)]) - 
                  ord('A')) % 26 for i in range(len(plaintext))]
    plaintext = [(ord(plaintext[i]) - ord('A')) % 26 for i in range(len(plaintext))]

    ciphertext = [chr((plaintext[i] + keystream[i]) % 26 + ord('A')) for i in range(len(plaintext))]
    
    return "".join(ciphertext)

def autokey_decrypt(ciphertext, keyword):
    ciphertext = ciphertext.upper()
    keyword = keyword.upper()
    keyword = [(ord(keyword[i]) - ord('A')) % 26 for i in range(len(keyword))]
    ciphertext = [(ord(ciphertext[i]) - ord('A')) % 26 for i in range(len(ciphertext))]

    prefix = [(ciphertext[i] - keyword[i]) % 26 for i in range(len(keyword))]
    for i in range(len(keyword), len(ciphertext)):
        prefix.append((ciphertext[i] - prefix[i - len(keyword)]) % 26)
    
    plaintext = "".join([chr(c + ord('A')) for c in prefix])

    return plaintext

def find_keyword(ciphertext, substring):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    # Brute force all keywords with length 6
    for i in range(26**6):
        keyword = "".join([alphabet[(i // (26**j)) % 26] for j in range(6)])
        
        plaintext = autokey_decrypt(ciphertext, keyword)
        if substring in plaintext:
            print(keyword)
    
    return None

if __name__ == "__main__":
    ciphertext = "GXILBGLQQJAIPWBMRKAZBWYKKKUCRKG"
    substring = "GESTURE"
    find_keyword(ciphertext, substring)


"""
OWLMLC
GLAUBE -- AMIRACLEISAGESTUREWHICHGODMAKES
QWTAUE

"""