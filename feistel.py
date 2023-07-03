def number_to_string(number: int) -> str:
    stack = []
    while number > 0: 
        stack.append(number % 2)
        number //= 2
    
    return ''.join(map(str, reversed(stack)))

def format_string(number: str) -> str:
    return number.zfill(4)

def xor_str(number1: str, number2: str) -> str:
    result = []
    for bit1, bit2 in zip(number1, number2):
        result.append(str(int(bit1) ^ int(bit2)))
    
    return ''.join(result)

functions = dict()
functions['f1'] = ['0000', '0010', '0011', '0011', 
                   '0001', '0001', '0001', '0010', 
                   '0010', '0001', '0010', '0011', 
                   '0000', '0000', '0000', '0000']

functions['f2'] = ['0010', '0011', '0000', '0011',
                   '0010', '0011', '0001', '0001', 
                   '0001', '0011', '0010', '0000', 
                   '0010', '0011', '0001', '0000']

functions['f3'] = ['0010', '0000', '0000', '0001',
                   '0001', '0001', '0010', '0011', 
                   '0001', '0011', '0000', '0010', 
                   '0011', '0010', '0011', '0001']

functions['f4'] = ['0011', '0010', '0001', '0010',
                   '0000', '0010', '0000', '0000', 
                   '0010', '0001', '0000', '0010', 
                   '0001', '0011', '0010', '0011']

def fn1(number: str) -> str: 
    return functions['f1'][int(number, 2)]

def fn2(number: str) -> str: 
    return functions['f2'][int(number, 2)]

def fn3(number: str) -> str: 
    return functions['f3'][int(number, 2)]

def fn4(number: str) -> str: 
    return functions['f4'][int(number, 2)]

def feistel(number: str) -> str:
    m = 2
    A = number[:m] # 2 bits in A
    B = number[m:] # 4 bits in B

    h = 4 # number of steps 
    funct_dict = {1: fn1, 2: fn2, 
                  3: fn3, 4: fn4}

    for i in range(h):
        A, B = B, xor_str(A, funct_dict[i+1](B))

    return A + B





if __name__ == "__main__": 

    print(feistel('101101'))
    print(feistel('101100'))