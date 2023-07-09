class GF2: 
    def __init__(self, coef): 
        self.coef = coef % 2

    def __add__(self, other): 
        return GF2(self.coef + other.coef)
    
    def __mul__(self, other): 
        return GF2(self.coef * other.coef)
    
    def __truediv__(self, other): 
        if other.coef == 0:
            raise ZeroDivisionError("Division by zero")
        
        return GF2(self.coef * other.coef)
    
    def __str__(self):
        return f"{str(self.coef)}"
    
    def __repr__(self):
        return str(self.coef)
    
    def __mod__(self, other):
        return GF2(self.coef % other.coef)
    
    def __divmod__(self, other):
        return self.__div__(other), self.__mod__(other)
    
    def __eq__(self, other):
        return self.coef == other.coef
    
    def __neg__(self):
        return GF2(self.coef) # In GF2, -1 = 1 
    
    def __hash__(self): 
        return repr(self).__hash__()
    
    def __pow__(self, other):
        return GF2(self.coef ** other.coef)
    
    def __radd__(self, other):
        return self.__add__(other)
    

class Polynomial:
    """
    Simple class for polynomials over GF(2)
    """ 
    def __init__(self, coef): 
        self.coef = coef
    
    def __add__(self, other): 
        res = dict()
        for k in self.coef: 
            if k in other.coef: 
                res[k] = self.coef[k] + other.coef[k]
            else: 
                res[k] = self.coef[k]
        
        for k in other.coef:
            if k not in res: 
                res[k] = other.coef[k]

        return Polynomial(res)

    def __str__(self) -> str:
        return f"{str(self.coef)}"

    def normalize(self): 
        return Polynomial({k: self.coef[k] for k 
                           in self.coef if self.coef[k] != GF2(0)})

    def __mul__(self, other): 
        p = Polynomial({0: GF2(0)})
        for p1, c1 in self.coef.items():
            for p2, c2 in other.coef.items():
                p.coef[p1 + p2] = p.coef.get(p1 + p2, GF2(0)) + c1 * c2

        return p.normalize()
    
    def __pow__(self, other):
        res = Polynomial({0: GF2(1)})
        for _ in range(other):
            res *= self
        return res
    
    def __len__(self):
        self = self.normalize()
        return max(self.coef.keys())

    def __divmod__(self, other):
        res = Polynomial({0: GF2(0)})  # Initialize quotient as zero polynomial
        rem = Polynomial(self.coef)  # Start with the dividend as the remainder

        while len(rem) >= len(other):
            deg_diff = len(rem) - len(other)
            coef = rem.coef[len(rem)] / other.coef[len(other)]
            res.coef[deg_diff] = coef
            rem = rem + other * Polynomial({deg_diff: coef})


        return res.normalize(), rem.normalize()

    def __mod__(self, other):
        return self.__divmod__(other)[1]


    def __truediv__(self, other):
        quotient, remainder = divmod(self, other)
        return quotient


    def __eq__(self, other):
        return self.coef == other.coef

    def __str__(self) -> str:
        temp = sorted(self.coef.items(), key=lambda x: x[0], reverse=True)
        return " + ".join([f"x^{p}" for p, c in temp if c != GF2(0)])        

    def to_binary(self) -> str: 
        last_pow = max(self.coef.keys())
        return "".join([str(self.coef.get(i, GF2(0))) for i in range(last_pow + 1)])


if __name__ == "__main__":
    p1 = Polynomial({5: GF2(1), 4: GF2(1), 0: GF2(1)})
    p2 = Polynomial({3: GF2(1)})
    print(p1 + Polynomial({5: GF2(1)}))
    print(p1 / p2)
    print(p1 % p2)
    #temp = Polynomial({0: GF2(0)})
    #print(temp + Polynomial({5: GF2(1)}))