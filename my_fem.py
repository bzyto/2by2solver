import numpy as np
## This is my stupid code to solve 2 by 2 linear equation
## Use of OOP is excessive, however I am learning
class eq2var:
    def __init__(self, equation):
        equation=np.array(equation)
        self.rhs=np.array([equation[2], equation[5]])
        self.lhs=np.array([equation[0], equation[1], equation[3], equation[4]])
        self.xmatrix=np.array([self.rhs[0], self.lhs[1], self.rhs[1], self.lhs[3]])
        self.ymatrix=np.array([self.lhs[0], self.rhs[0], self.lhs[2], self.rhs[1]])
    def determinant(self, matrix):
        det=matrix[0]*matrix[3]-matrix[1]*matrix[2]
        return det
    def solve(self):
        x=self.determinant(self.xmatrix)/self.determinant(self.lhs)
        y=self.determinant(self.ymatrix)/self.determinant(self.lhs)
        print(f"The equation is solved by x={x}, y={y}")
        return np.array(x, y)
