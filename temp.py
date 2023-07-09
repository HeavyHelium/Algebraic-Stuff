class Polynomial:
    '''
    Клас за работа с полиноми.
    '''
    def __init__(self, quotients = [], _class = None):
        self.poly = {}
        if not _class:
            if not quotients:
                _class = int
            else:
                try:
                    _class = quotients[0][1].__class__
                except TypeError:
                    _class = int
        self._class = _class
        for monome in quotients:
            power, coefficent = monome
            self.poly[power] = _class(coefficent) + self.poly.get(power, _class(0))
 
    def normalize(self):
        [self.poly.pop(pow) for pow, coef in self if coef == self._class(0)]
        return self
 
    def __add__(self, other):
        p = Polynomial(_class = self._class)
        p.poly = {}
        for power, coefficent in self.poly.items():
            p.poly[power] = coefficent
        for power, coefficent in other.poly.items():
            p.poly[power] = coefficent + p.poly.get(power, self._class(0) )
        return p.normalize()
 
    def __mul__(self, other):
        p = Polynomial(_class = self._class)
        for p1, c1 in self.poly.items():
            for p2, c2 in other.poly.items():
                p.poly[p1+p2] = c1*c2 + p.poly.get(p1+p2, self._class(0) )
        return p.normalize()
 
    def __div__(self, other):
        return self.__divmod__(other)[0]
 
    def __mod__(self, other):
        return self.__divmod__(other)[1]
 
    def __divmod__(self, other):
        other = Polynomial([(pow, coef) for pow, coef in other])
        rem = Polynomial([(pow, coef) for pow, coef in self])
        res = Polynomial(_class = self._class)
        while len(rem) >= len(other):
            coef = rem[len(rem)] / other[len(other)]
            deg_dif = len(rem) - len(other)
            res[deg_dif] = coef
            old_rem_deg = len(rem)
            rem = rem - other * Polynomial([(deg_dif, coef)])
            assert rem[old_rem_deg] == rem._class(0), "BAD"
        return (res, rem)
 
    def __neg__(self):
        return Polynomial(
                [(power, -coefficent) for power, coefficent in self.poly.items()],
                _class = self._class)
 
    def __sub__(self, other):
        return (self + (-other)).normalize()
 
    def __str__(self):
        @memoize
        def helper(coef, power):
            if coef == self._class(0):
                if power == 0:
                    return "0"
                return None
            if power == 0:
                return "%s" % coef
            if power == 1:
                if coef == self._class(1):
                    return "x"
                return "%s*x" % coef
            if coef == self._class(1):
                return "x^%s" % power
            return "%s*x^%s" % (coef, power)
 
        # sorted(self.poly.items) ?
        poly = " + ".join([ helper(coef, power) for power, coef
                in reversed(self.poly.items())
                if helper(coef, power) != None])
        if len(self.poly) == 0:
            poly = "0"
        return "Polynomial %s" % poly
 
    def __repr__(self):
        return self.__str__()
 
    def __len__(self):
        if len(self.poly) == 0:
            return 0
        return max(pow for pow, coef in self if coef != 0)
 
    def __getitem__(self, ind):
        if ind in self.poly:
            return self.poly[ind]
        return self._class(0)
 
    def __setitem__(self, power, coef):
        self.poly[power] = self._class(coef)
 
    def __iter__(self):
        for power, coef in self.poly.items():
            yield (power, coef)
 
    def __call__(self, x):
        '''
        Връща f(x), където f е текущият полином.
        '''
        return sum(coef * (x**power) for power, coef in self)
 
    def __pow__(self, other):
        ans = Polynomial([(pow, coef) for pow, coef in self])
        for x in range(1, other):
            ans = ans * self
        return ans
 
    def __hash__(self):
        return str(self).__hash__()
 
class GaloaField:
    '''
    Полето на Галоа.
    Известно още като поле за сметки по модул 2.
    '''
    def __init__(self, coef):
        if coef.__class__ == GaloaField:
            self.coef = coef.coef % 2
        else:
            self.coef = coef % 2
    def __add__(self, other):
        return GaloaField(self.coef + other.coef)
    def __sub__(self, other):
        return GaloaField(self.coef - other.coef)
    def __mul__(self, other):
        return GaloaField(self.coef * other.coef)
    def __div__(self, other):
        return GaloaField(self.coef / other.coef)
    def __str__(self):
        return str(self.coef)
    def __divmod__(self, other):
        return self / other, self % other
    def __mod__(self, other):
        return GaloaField(self.coef % other.coef)
    def __neg__(self):
        return GaloaField(self.coef)
    def __eq__(self, other):
        return self.coef == other.coef
    def __hash__(self):
        return str(self).__hash__()
    
 
def calculate_secret_key(b_poly, a_key, modulo):
    '''
    Изчислява тайния ключ при комуникация между A и B,
    ако B праща полинома b_poly, а A праща ключа a_key.
    Използва се схемата на Diffie-Hellman.
    Резултатът всъщност е равен на (b_poly ** a_key) % modulo.
    b_poly е списък от двойки (степен, коефицент).
    '''
    return (b_poly ** a_key) % modulo
 
def poly_to_bin(poly, digits):
    def helper(a):
        if a == a.__class__(0):
            return "0"
        else:
            return "1"
    return "".join([helper(poly[pow]) for pow in range(digits)])
 
if __name__ == "__main__":
    #GaloaField просто е полето съставено от {0, 1}
    secret_key = calculate_secret_key(
                Polynomial([[1,1],[5,1],[7,1]], GaloaField),
                2,
                Polynomial([[10,1],[3,1],[0,1]], GaloaField)
            )
    print(secret_key)
    print(poly_to_bin(secret_key, 10))