from polynomial import Polynomial, GF2

def get_secret_key(b, a_key, modulo): 
    return (b ** a_key) % modulo


if __name__ == "__main__": 
    b = Polynomial({7: GF2(1), 5: GF2(1), 1: GF2(1)})
    a_key = 2
    modulo = Polynomial({10: GF2(1), 3: GF2(1), 0: GF2(1)})
    print(get_secret_key(b, a_key, modulo))
    print(get_secret_key(b, a_key, modulo).to_binary()) # 10111001