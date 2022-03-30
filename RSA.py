"""#RSA: Algoritmo de encriptación asimetrico (con dos llaves)
se centra en el principio de que encontrar 2 factores de un número grande
es dificil, mas si son primos
Pasos:
1. Seleccionar 2 números primos P y Q
2. n=P*Q Public Key
3. Elegir un exponente entero e, que no sea factor de n y que sea menor que Phi
4. Phi(n) = (P-1)(Q-1)
5. d=(k*fi(n)+1)/e para algun entero k Private Key

Para encriptar:
c=data^e mod n
Para desencriptar:
data=c^d mod n

Para el algoritmo se recibe como parametro un intervalo en el que se deben generar
los números primos P y Q, y debe imprimir los parametros de la Public (n y e) y la
Private (d) Key

Calcular tiempos de ejecución"""

import random
import time
start_time = time.time()
 
primeros_primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                     31, 37, 41, 43, 47, 53, 59, 61, 67,
                     71, 73, 79, 83, 89, 97, 101, 103,
                     107, 109, 113, 127, 131, 137, 139,
                     149, 151, 157, 163, 167, 173, 179,
                     181, 191, 193, 197, 199, 211, 223,
                     227, 229, 233, 239, 241, 251, 257,
                     263, 269, 271, 277, 281, 283, 293,
                     307, 311, 313, 317, 331, 337, 347, 349]

# 
def numeroAleatorio(a,b):
    return random.randrange(a,b)
 
def primoPrueba(a,b):

    while True:
        # Obtain a random number
        primo = numeroAleatorio(a,b)
 
         # Test divisibility by pre-generated
         # primes
        for divisor in primeros_primos:
            if primo % divisor == 0 and divisor**2 <= primo:
                break
        else: return primo
 
def millerRabin(mrc):
    '''Run 20 iterations of Rabin Miller Primality test'''
    maxDivisionsByTwo = 0
    ec = mrc-1
    while ec % 2 == 0:
        ec >>= 1
        maxDivisionsByTwo += 1
    assert(2**maxDivisionsByTwo * ec == mrc-1)
 
    def trialComposite(round_tester):
        if pow(round_tester, ec, mrc) == 1:
            return False
        for i in range(maxDivisionsByTwo):
            if pow(round_tester, 2**i * ec, mrc) == mrc-1:
                return False
        return True
 
    # Set number of trials here
    numberOfRabinTrials = 20
    for i in range(numberOfRabinTrials):
        round_tester = random.randrange(2, mrc)
        if trialComposite(round_tester):
            return False
    return True
 
"""
if __name__ == '__main__':
    while True:
        n = (1000,100000000000)
        prime_candidate = primoPrueba(n(0),n(1))
        if not millerRabin(prime_candidate):
            continue
        else:
            print(prime_candidate)
            break
"""
def mcd(a, b):
    if b<a: #10,5
        temp=a
        a=b
        b=temp 
    while b != 0:
        (a, b) = (a, a%b)
    return a

def generar_llaves(a,b):
    #Se generan 2 primos, P y Q que esten dentro del rango
    while True:
        primo=primoPrueba(a,b)
        print("primo de prueba A")
        if not millerRabin(primo):
            print("Iteracion A")
            continue
        else:
            p=primo
            print("Paso A")
            break
    while True:
        primo=primoPrueba(a,b)
        print("primo de prueba B")
        if not millerRabin(primo):
            print("Iteracion B")
            continue
        else:
            q=primo
            print("Paso B")
            break
    n=p*q
    e=3 #se inicia e en el menor valor que puede tener
    phi=(p-1)*(q-1)
    while(e<phi):
        if (mcd(e,phi)==1):
            break
        else:
            print(e)
            e+=2
    d = (1 + (2*phi))/e

    #Generar parametro n
    
    return n,e,d

generar_llaves(10000,10000000000)
print("--- %s seconds ---" % (time.time() - start_time))