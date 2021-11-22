from sympy import symbols
from sympy.matrices import Matrix

a, m, p = symbols('a m p')
M = Matrix([[0, 0, 0, -1 / p, 0, 0, 0, 0, 0], [0, 0, 0, 0, -1 / p, 0, 0, 0, 0], [0, 0, 0, 0, 0, -1 / p, 0, 0, 0],
            [-(a + 2 * m), 0, 0, 0, 0, 0, 0, 0, 0], [0, -m, 0, 0, 0, 0, 0, 0, 0], [0, 0, -m, 0, 0, 0, 0, 0, 0],
            [-a, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [-a, 0, 0, 0, 0, 0, 0, 0, 0]])
print(M.eigenvals())  #returns eigenvalues and their algebraic multiplicity