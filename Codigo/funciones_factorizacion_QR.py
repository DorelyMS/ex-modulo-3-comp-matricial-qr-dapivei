#!/usr/bin/env python
# coding: utf-8

import numpy as np
import copy
import codecs




def busca_ayuda(cadena):
    """
    Función que devuelve el texto de ayuda correspondiente a la funcion
    que se pase como parámetro, obtenida de un unico archivo .txt
    donde están documentadas las "ayudas" de todas las funciones asociadas
    a la factorización QR (contenidas en este .py)
    
    params: cadena  nombre de la función de la que se desea obtener ayuda
                    
    return: help    ayuda de la función buscada en forma de texto
    
    """
    l=len(cadena)
    help=codecs.open('Help_funciones_factorizacion_QR.txt', "r", "utf-8").read()
    p_inicio=help.find("****i****" + cadena)
    p_final=help.find("****f****" + cadena)
    help=help[(p_inicio+9+l):p_final]
    return help






def crear_matriz_aleatoria(renglones,columnas,maximo_valor,minimo_valor,entero=False):
    """
    Función de apoyo para genear matrices aleatorias

    params: renglones       no. de renglones de la matriz
            columnas        no. de columnas de la matriz
            maximo_valor    valor máximo de las entradas de la matriz
            minimo_valor    valor mínimo de las entradas de la matriz
            entero          Indica si las entradas serán enteras (True) o no
            
    return: M               Matriz con numeros al azar
    """
    #Se inicializa una matriz llena de ceros con las dimensiones deseadas (mxn)
    M=np.zeros((renglones, columnas))
    for i in range(renglones):
        for j in range(columnas):
            #Si entero es verdadero se obtiene el maximo entero menor o igual a 1 (//1)
            if entero:
                M[i][j]=(np.random.rand(1)*(maximo_valor+1-minimo_valor)+minimo_valor)//1
            else:
                M[i][j]=np.random.rand(1)*(maximo_valor-minimo_valor)+minimo_valor
    return M

crear_matriz_aleatoria.__doc__ =busca_ayuda("crear_matriz_aleatoria")






def house(x):
    """
    Función que calcula vector de householder
    
    params: x       vector al que se le hará la reflexión householder
                    
    return: Beta    factor para obtener matriz de reflexión householder Rf
            v       vector de householder
    """
    #longitud del vector x=(x_0,x_1,x_2,...,x_(m-1))
    m=len(x)
    norm_2_m=x[1:m].dot(np.transpose(x[1:m]))
    #Se hace v=x=(1,x_1,x_2,...,x_(m-1))
    v=np.concatenate((1,x[1:m]), axis=None)
    Beta=0
    #con las siguientes condiciones se checa si x es múltiplo del vector canónico e_1 
    #y el signo de x[0]
    if (norm_2_m==0 and x[0]>=0):
        Beta=0
    elif (norm_2_m==0 and x[0]<0):
        Beta=2
    else:
        norm_x=np.sqrt(pow(x[0],2)+norm_2_m)
        if (x[0]<=0):
            v[0]=x[0]-norm_x
        else:
            v[0]=-norm_2_m/(x[0]+norm_x)
        Beta=2*pow(v[0],2)/(norm_2_m+pow(v[0],2))
        v=v/v[0]
    return Beta, v

house.__doc__ =busca_ayuda("house")






def matriz_auxiliar_Arv(A):
    """
    Función que genera una matriz que contiene los elementos r distintos de cero de la 
    matriz R y las entradas de los vectores householder v (excepto la primera), con los 
    cuales se puede calcular la matriz Q. Ambas matrices componentes de la factorización QR
    
    params: A      Matriz (mxn) de la que se desea obtner factorización QR
            
    return: Arv    Matriz (mxn) que incluye las componentes distintas de cero de la matriz R 
                   y los vectores householder con los que se puede obtener la matriz Q, y 
                   con ello la factorización QR
    """
    #m contiene el numero de renglones y n el de columnas
    m=A.shape[0]
    n=A.shape[1]
    #se crea una matriz con los valores de A
    Arv=copy.copy(A)
    for j in range(n):
        beta, v=house(Arv[j:m,j])
        #Con esta multiplicación se van generando las componentes r de la matriz R
        Arv[j:m,j:n]=Arv[j:m,j:n]-beta*(np.outer(v,v)@Arv[j:m,j:n])
        #se guarda en cada columnas los valores de v d, excepto la primer componente (que vale 1)
        Arv[(j+1):m,j]=v[1:(m-j)]
    return Arv

matriz_auxiliar_Arv.__doc__ =busca_ayuda("matriz_auxiliar_Arv")






def matriz_R(A_r_v):
    """
    Función que devuelve la matriz R de la factorización QR de una matriz A, 
    apartir de la matriz Arv
    
    params: A_r_v   Matriz (mxn) que incluye elementos de la matriz R y Q, de la factorización QR

    return: R       Matriz (mxn) R de la factorización A=QR
    """
    m=A_r_v.shape[0]
    n=A_r_v.shape[1]
    R=np.zeros((m,n))
    #la matriz A_r_v ya tiene los elementos de r en el triangulo superior
    #por lo que únicamente se sustraen dichos valores y lo demás se deja en ceros
    for j in range(n):
        R[0:(j+1),j]=A_r_v[0:(j+1),j]
    return R

matriz_R.__doc__ =busca_ayuda("matriz_R")






def matriz_Q(A_r_v):
    """
    Función que devuelve la matriz R de la factorización QR de una matriz A,
    apartir de la matriz Arv
    
    params: A_r_v   Matriz (mxn) con la info escencial para la factorización

    return: Q       Matriz Q (mxm) de la factorización A=QR
    """
    m=A_r_v.shape[0]
    n=A_r_v.shape[1]
    Q=np.eye(m)
    I=np.eye(m)
    for j in range(n-1,-1,-1):
        #Se sustrae la información de los vectores de householder contenida
        #en la matriz Arv, agregando la primera entrada que no está en dicha matriz (y que es 1)
        v=np.concatenate((1,A_r_v[(j+1):m,j]), axis=None)
        #Se calcula el factor beta para obtener la matriz de reflexión
        beta=2/(1+A_r_v[(j+1):m,j].dot(A_r_v[(j+1):m,j]))
        #Aquí se va acumulando el producto de las Qj's para llegar a Q_(n-1)*Q(n-2)*...Q_2*Q_1*Q_0=Q
        #al final del ciclo
        Q[j:m,j:m]=(I[j:m,j:m]-beta*np.outer(v,v))@Q[j:m,j:m]
    #La Q_(n-1) es la matriz más chica y la última que calculamos para generar ceros en la última
    #columna de A, y la Q_1 es la matriz más grande y la primera que calculamos para generar ceros
    #en la 1era columna de A
    return Q

matriz_Q.__doc__ =busca_ayuda("matriz_Q")






def Q_j(A_r_v,j):
    """
    Función que calcula la matriz Qj (en el proceso de obtención de factorización QR se van 
    obteniendo n Qj's, que si se multiplican todas da por resultado Q=Q_1*Q_2*...*Q_n)
                            
    params: A_r_v   Matriz (mxn) con la info escencial
            C       Matriz (mxp) (si se pasa por ejemplo C=Identidad (mxm) la funcion 
                    devolverá Q)

    return: Qj      Matriz Q de la j-esima iteración del proceso iterativo de factorización QR
    """
    m=A_r_v.shape[0]
    n=A_r_v.shape[1]
    Qj=np.eye(m)
    #Para construir Q_j requerimos usar el vector v contenido en Arv contenido
    #en la j-1 columna (considerando que en Python la primer columna es la cero)
    v=np.concatenate((1,A_r_v[j:m,(j-1)]), axis=None)
    beta=2/(1+A_r_v[j:m,(j-1)].dot(A_r_v[j:m,(j-1)]))
    Qj[(j-1):m,(j-1):m]=np.eye(m-(j-1))-beta*np.outer(v,v)
    return Qj

Q_j.__doc__ =busca_ayuda("Q_j")