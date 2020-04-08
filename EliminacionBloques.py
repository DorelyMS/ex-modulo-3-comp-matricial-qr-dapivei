#  Esta es la función para la creación de bloques usando un arreglo de numpy

import numpy as np
import sys

def bloques(A, n1=False, n2=False):

	# Primero definimos el n
	m,n = A.shape

	# Si no se dan los n deseados, se intentan hacer los bloques casi iguales
	if  not (n1&n2):
		n1 = n//2
		n2 = n - n1
	# Los bloques deben cumplir la condicion de tamaño
	elif n1+n1 != n:
		sys.exit('n1 + n2 debe ser igual a n')
	else:
		None

	A11 = A[:n1,:n1]
	A12 = A[:n1,n1:n]
	A21 = A[n1:m,:n1]
	A22 = A[n1:m,n1:n]

	# A11,A12,A21,A22 = (A.reshape(n1,2,-1,2)
	# 	.swapaxes(1,2)
	# 	.reshape(-1,2,2))

	return A11,A12,A21,A22


A = np.random.normal(20,size=(5,4))

A11,A12,A21,A22 = bloques(A)

print(A)
print("--------------")
print(A11)
print("--------------")
print(A12)
print("--------------")
print(A21)
print("--------------")
print(A22)

