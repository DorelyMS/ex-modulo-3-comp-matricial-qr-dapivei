#  Esta es la función para la creación de bloques usando un arreglo de numpy

import numpy as np
import sys

def bloques(A, b=False, n1=False, n2=False):

	# Primero definimos el n
	m,n = A.shape

	# Condiciones de A
	# Si no se dan los n deseados, se intentan hacer los bloques casi iguales
	if  not (n1&n2):
		n1 = n//2
		n2 = n - n1
	# Los bloques deben cumplir la condicion de tamaño
	elif n1+n1 != n:
		sys.exit('n1 + n2 debe ser igual a n')
	else:
		None

	# Condiciones de b
	if  b is False:
		b1 = None
		b2 = None
		print('condicion1')
	elif len(b) == m:
		b1 = b[:n1]
		b2 = b[n1:m]
	else:
		sys.exit('los renglones de A y b deben ser del mismo tamaño')


	A11 = A[:n1,:n1]
	A12 = A[:n1,n1:n]
	A21 = A[n1:m,:n1]
	A22 = A[n1:m,n1:n]


	# A11,A12,A21,A22 = (A.reshape(n1,2,-1,2)
	# 	.swapaxes(1,2)
	# 	.reshape(-1,2,2))

	return A11,A12,A21,A22,b1,b2


# Datos aleatoreros puebra
A = np.random.rand(10000,10000)
b = np.random.rand(10000)

# codigo para verificar bloques
#A11,A12,A21,A22,b1,b2 = bloques(A,b)
#print(A11)
#print(b1)

def eliminacion_bloques(A,b):

	## Sean A y A11 no singulares

	if np.linalg.det(A)==0:
		sys.exit('A debe ser no singular')

	A11,A12,A21,A22,b1,b2 = bloques(A,b)

	if np.linalg.det(A11)==0:
		ys.exit('A11 debe ser no singular')

	## 1. Calcular A11^{-1}A12 y A11^{-1}b1 teniendo cuidado en no calcular la inversa sino un sistema de ecuaciones lineales
	## Aquí se debe usar el método QR una vez que esté desarrollado

	## Definimos y = A11^{-1}b1, por tanto A11y=b1. Resolviendo el sistema anterior para y:
	y = np.linalg.solve(A11,b1)

	## Definimos Y = A11^{-1}A12
	Y = np.linalg.solve(A11,A12)

	## 2. Calcular el complemento de Schur del bloque A11 en A. Calcular b_hat
	S = A22 - A21@Y
	b_h = b2 - A21@y

	## 3. Resolver Sx2 = b_hat
	x2 = np.linalg.solve(S,b_h)

	## 4. Resolver A11x1 = b1-A12X2
	x1 = np.linalg.solve(A11,b1-A12@x2)

	return np.concatenate((x1,x2), axis=0)

print(eliminacion_bloques(A,b))
#print(np.linalg.solve(A,b))