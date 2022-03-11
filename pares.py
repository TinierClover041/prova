# -*- coding: utf-8 -*-
"""
Crie um programa que leia uma lista de strings separadas por vírgulas e
mostre uma lista de pares. Caso a lista possua um número ímpar de 
elementos, inclua a string vazia como segundo elemento do par final

* while: 1
* lst: 1
"""

frase = input(">>> ").lower()

freqs = {}
for c in frase:
    freqs[c] = freqs.get(c, 0) + 1
def key_fn(par):
    letra, n = par
    return n
    
pares = sorted(freqs.items(), key=key_fn)
pares = pares.reverse()
    
for c, n in pares:
    print(f"{c!r}: {n}")
    
#return -n
#return n, letra
#return -n, letra
#pares.reverse()
