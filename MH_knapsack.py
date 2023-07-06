class MerkleHellman: 
    encoding = {'A': [0, 0, 0, 1, 1], 'B': [0, 0, 1, 0, 1], 'C': [0, 0, 1, 1, 0],
                'D': [0, 0, 1, 1, 1], 'E': [0, 1, 0, 0, 1], 'F': [0, 1, 0, 1, 0],
                'G': [0, 1, 0, 1, 1], 'H': [0, 1, 1, 0, 0], 'I': [0, 1, 1, 0, 1],
                'J': [0, 1, 1, 1, 0], 'K': [0, 1, 1, 1, 1], 'L': [1, 0, 0, 0, 1],
                'M': [1, 0, 0, 1, 0], 'N': [1, 0, 0, 1, 1], 'O': [1, 0, 1, 0, 0],
                'P': [1, 0, 1, 0, 1], 'Q': [1, 0, 1, 1, 0], 'R': [1, 0, 1, 1, 1],
                'S': [1, 1, 0, 0, 0], 'T': [1, 1, 0, 0, 1], 'U': [1, 1, 0, 1, 0],
                'V': [1, 1, 0, 1, 1], 'W': [1, 1, 1, 0, 0], 'X': [1, 1, 1, 0, 1],
                'Y': [1, 1, 1, 1, 0], 'Z': [1, 1, 1, 1, 1]}


    def __init__(self, modulo, t, super_inc_seq):
        self.modulo = modulo
        self.t = t
        self.super_inc_seq = super_inc_seq
        self.public_key = self.__generate_public_key()
        
    def __generate_public_key(self):
        return [t * ai % self.modulo for ai 
                in self.super_inc_seq]
    
    def __encrypt_block(self, block):
        return sum([x[0]*x[1] for x 
                    in zip(block, self.public_key)])
        
    def encrypt(self, message): 
        return [self.__encrypt_block(block) 
                for block in MerkleHellman.encode(message)]
            
    @staticmethod
    def encode(message):
        """
        it is assumed that the length of the message 
        is with accordance to the exmaple
        """ 
        enc_m = []
        for i in range(0, len(message), 2):
            enc_m.append(MerkleHellman.encoding[message[i]] + 
                         MerkleHellman.encoding[message[i+1]])
        return enc_m


if __name__ == "__main__":
    super_inc_seq = [2, 3, 7, 13, 27, 53, 
                     106, 213, 425, 851]
    modulo = 1529
    t = 64 # modulo and t are coprime

    mh = MerkleHellman(modulo, t, super_inc_seq)

    print(mh.public_key)
    print(mh.encode("LONDON"))
    print(mh.encrypt("LONDON"))
