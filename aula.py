import numpy as np
import math

# Decomposição de Cholesky
m_op = np.matrix('0 0 0; 0 0 0; 0 0 0')
m_dada = np.matrix('4 12 -16; 12 37 -43; -16 -43 98')

# U11 = Raíz de A11
m_op[0, 0] = math.sqrt(m_dada[0, 0])

# Para i > 0 até n, m_op[1, j] = m_dada[1, j]/m_op[1, 1]
for i in range(len(m_op) -1):
    m_op[0, i + 1] = m_dada[0, i + 1]/ m_op[0, 0]

# Se𝑛≠2.
# Para j > 1 até len(m_op -2) 
if  len(m_op) != 2:
    j = 2
    for j in range(len(m_op -2)):
        print(j)

