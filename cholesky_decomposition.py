import numpy as np
import math

m_dada = np.matrix('4 12 -16; 12 37 -43; -16 -43 98')
m_test = np.matrix('4 10 -16; 5 30 -43; -16 -41 95')


def cholesky_decomposition(matrix_to_decompose):
    len_matrix = len(matrix_to_decompose)
    m_op = np.zeros((len_matrix, len_matrix))    
    len_matrix_to_for = len(matrix_to_decompose) - 1
    
    # U11 = Raíz de A11
    m_op[0, 0] = math.sqrt(matrix_to_decompose[0, 0])

    # Para i > 0 até n, m_op[1, j] = m_dada[1, j]/m_op[1, 1]
    for i in range(len_matrix_to_for):
        m_op[0, i + 1] = matrix_to_decompose[0, i + 1]/ m_op[0, 0]

    # Se 𝑛≠2.
    # Para j > 1 até len(m_op -2) 
    # Calculando linhas do meio
    if  len(m_op) != 2:
        for j in range(len(m_op)):
            if (j > 0) and (j < len_matrix_to_for):

                ## Calculando somatório para determinante
                summatory_todet = 0
                for k in range(j): 
                    summatory_todet = summatory_todet + m_op[k, j]
                    
                m_op[j, j] = math.sqrt(matrix_to_decompose[j, j] - math.pow(summatory_todet, 2))
                summatory_todet = 0
                
                for l in range(j):                                        
                    ## Calculando somatório para os lados
                    summatory_tosides = 0                
                    for m in range(j):
                        summatory_tosides = m_op[m, j]*m_op[m, l + 2]
                        
                m_op[j, l + 2] = (matrix_to_decompose[j, l + 2] - summatory_tosides)/m_op[j, j]

    # Calculando último canto da matriz[n, n]
    ## Calculando somatório para n, n
    summatory_tonn = 0
    for i in range(len_matrix_to_for):
        summatory_tonn = summatory_tonn + math.pow(m_op[i, len(m_op) - 1], 2)
        
    m_op[len_matrix_to_for, len_matrix_to_for] = math.sqrt(matrix_to_decompose[len_matrix_to_for, len_matrix_to_for] - summatory_tonn)
    return m_op

    
chol = cholesky_decomposition(m_dada)
print(chol)

#print(np.linalg.cholesky(m_dada))
