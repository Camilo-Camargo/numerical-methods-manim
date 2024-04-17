import numpy as np
from manim import *

def P(w, h):
    w2 = w*w 
    h2 = h*h
    #print(f"({w2}-({2}/{h2}))")
    return w2 - (2/h2)

def M(h):
    return 1 / h**2 

def _h(a, b, n):
    return (b - a) / (n-1)

def homogenius_dx2(alpha, alpha_prime,w,a,b, n):
    h = _h(a, b, n)
    p = P(w, h)  
    m = M(h) 

    matrix = [[0 for i  in range(n-1)] for i in range(n-1)]
    vector = [0 for i in range(n-1)]

    for i in range(len(matrix)):
        for j in range(n-1):
            if(i == j):
                matrix[i][j] = m 
            if(i == j and i == 0 and j == 0):
                matrix[i][j] = 2*matrix[i][j]

            if(i == j+1):
                matrix[i][j] = p
            if(i-j == 2):
                matrix[i][j] = m

    matrix = np.array(matrix) 


    return (h,p,m, matrix, vector) 

def matrix_to_tex(a):  
    """Returns a LaTeX bmatrix
    :a: numpy array
    :returns: LaTeX bmatrix as a string
    """
    if len(a.shape) > 2:
        raise ValueError('bmatrix can at most display two dimensions')
    lines = str(a).replace('[', '').replace(']', '').splitlines()
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + ' & '.join(l.split()) + r'\\' for l in lines]
    rv +=  [r'\end{bmatrix}']

    return '\n'.join(rv)
            


class DifferentialEquation(MovingCameraScene):
    def construct(self): 
        title = Title("Differential Equation Homogenious") 

        alpha = 1 
        alpha_prime = 0
        w = 2
        a = 0
        b = 6
        n = 21

        #alpha       = int(input("Alpha: "))
        #alpha_prime = int(input("Alpha Prime: "))
        #w = int(input("w: "))
        #a = int(input("a: "))
        #b = int(input("b: "))
        #n = int(input("n: "))  

        # values
        (h,p,m,matrix, vector) = homogenius_dx2(alpha,alpha_prime, w,a,b,n) 

        # Constraints
        alpha = MathTex(f"\\alpha = {alpha}")  
        alpha_prime = MathTex(f"\\alpha\\prime = {alpha_prime}") 
        w = MathTex(f"w = {w}")
        a = MathTex(f"a = {a}")
        b = MathTex(f"b = {b}")
        n = MathTex(f"n = {n}")  
        constraints = Group(alpha, alpha_prime, w, a, b, n).arrange(DOWN, buff=0.5) 


#        h = MathTex(f"h = {h}")
#        p = MathTex(f"p = {p}")
#        m = MathTex(f"m = {m}")  

#        values = Group(h,p,m).arrange(DOWN, buff=0.5)
#
        self.play(Create(title))
#        for i,constraint in enumerate(constraints):
#            self.play(Create(constraint)) 

#        self.play(*[constraint.animate.shift(4*LEFT) for constraint in constraints]) 

#        for value in values:
#            self.play(Create(value)) 

        matrix = Matrix(matrix)
        self.play(Create(matrix))


        

#homogenius_dx2(1, 0, 2, 0, 6, 21)
