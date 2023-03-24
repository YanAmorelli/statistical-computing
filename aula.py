import numpy as np
import math

m_op = np.matrix('0 0 0; 0 0 0; 0 0 0')
m_dada = np.matrix('4 12 -16; 12 37 -43; -16 -43 98')

# U11 = Raíz de A11
m_op[0, 0] = math.sqrt(m_dada[0, 0])

# Para i > 0 até n, m_op[1, j] = m_dada[1, j]/m_op[1, 1]
for i in range(len(m_op) -1):
    m_op[0, i + 1] = m_dada[0, i + 1]/ m_op[0, 0]

# Se 𝑛≠2.
# Para j > 1 até len(m_op -2) 
# Calculando linhas do meio
if  len(m_op) != 2:
    for j in range(len(m_op)):
        if (j > 0) and (j < len(m_op) -1):

            ## Calculando somatório para determinante
            summatory_todet = 0
            for k in range(j): 
                summatory_todet = summatory_todet + m_op[k, j]
                
            m_op[j, j] = math.sqrt(m_dada[j, j] - math.pow(summatory_todet, 2))
            summatory_todet = 0
            
            for l in range(j):                
                print("j", j)
                print("l", l + 1)
                    
                ## Calculando somatório para os lados
                summatory_tosides = 0                
                for m in range(j):
                    print("m", m)
                    summatory_tosides = m_op[m, j]*m_op[m, l + 2]
                    
            m_op[j, l + 2] = (m_dada[j, l + 2] - summatory_tosides)/m_op[j, j]

# Calculando último canto da matriz[n, n]
## Calculando somatório para n, n
summatory_tonn = 0
for i in range(len(m_op) - 1):
    summatory_tonn = summatory_tonn + math.pow(m_op[i, len(m_op) - 1], 2)
    
m_op[len(m_op) - 1, len(m_op) - 1] = math.sqrt(m_dada[len(m_dada) - 1, len(m_dada) - 1] - summatory_tonn)
print("m_op", m_op)
