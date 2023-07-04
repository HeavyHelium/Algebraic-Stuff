from utils import find_prime_factors, inverse_element_ring

class RSA: 
    def __init__(self, n, e, d): 
        self.n = n
        self.e = e
        self.d = d

    def encrypt(self, message):
        return pow(message, self.e, self.n)
    
    def decrypt(self, message):
        return pow(message, self.d, self.n)
    
    @staticmethod
    def transf_message(message): 
        tm = []
        for i in range(0, len(message), 2):
            tm.append(RSA.to_z26(message[i]) + 
                      26 * RSA.to_z26(message[i + 1]))

        return tm

    @staticmethod
    def rev_transf_message(message):
        tm = RSA.to_char(message % 26) + \
             RSA.to_char(message // 26)

        return tm

    @staticmethod
    def to_z26(char) -> int:
        return ord(char) - ord('A')

    @staticmethod
    def to_char(z26) -> str:
        return chr(z26 + ord('A'))


if __name__ == "__main__": 
    #print(find_prime_factors(899)) # {29: 1, 31: 1}
    #print(inverse_element_ring(611, 840)) # 11

    rsa = RSA(899, 611, 11)

    for i in [106, 680, 303]: 
        print(RSA.rev_transf_message(rsa.decrypt(i)), end="")
    print()