from sympy import Function, lambdify, sympify
from sympy import exp as e
from sympy import pprint
from sympy.abc import x,y, z
print = pprint

EPSILON = 10e-10

def approx_error(old, new):
    if(old == new): return 1
    numerator = new - old
    denominator = new
    return abs(numerator / denominator)


class NewtonRaphson:
    def __init__(self, f):
        self.f = f
        # get the first unknown variable
        var = f.free_symbols.pop()
        # First derivative
        self.df  = f.diff(var)
        # Newton Raphson
        self.equ = var - (f/self.df)

    def eval(self, xi):
        equ = self.equ.subs(x, xi)
        return sympify(equ).evalf()

    def compute(self,x0):
        vars = {
            "x0": x0
        }
        # first iteration
        vars["x1"] = self.eval(vars["x0"])
        print(self.f)  
        print(self.df)
        print(vars)
        i = 1
        while(approx_error(vars[f"x{i-1}"],vars[f"x{i}"]) > EPSILON):
            i += 1
            vars[f"x{i}"] = self.eval(vars[f"x{i-1}"])

        return vars


class NewtonRaphsonRoots(NewtonRaphson):
    def __init__(self,f):
        super()
        self.f = f
        # get the first unknown variable
        var = f.free_symbols.pop()
        # First derivative
        self.df  = f.diff(var)
        df = self.df
        self.df2 = self.df.diff(var)
        df2 = self.df2
        # Newton Raphson
        self.equ = var - (f*df)/(df**2 - (f*df2))

# test
f = (x-3)*(x-1)

method = NewtonRaphsonRoots(f)
print(method.f)
print(method.df)
print(method.df2)
print("\n")
print(method.equ)

print(method.compute(4))

#method = NewtonRaphson(f) 
#print(method.compute(0))






