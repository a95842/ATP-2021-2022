# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 14:48:18 2021

@author: Dinis Mesquita
"""

numero_pensado = input("introduzir numero pensado entre 0 a 100:")


n = 50
tentativa = 1



while n != int(numero_pensado) :
    print("o computador advinhou o numero:", n)
    maior_ou_menor = input("Escreve 'maior' ou 'menor', se o numero advinhado pelo computador e maior ou menor, respetivamente: ")
    
    if maior_ou_menor == "maior" :
        
        n = n + n//2
        
        
        
        tentativa = tentativa + 1
    
    
    elif maior_ou_menor == "menor":
            n = n - n//2
        
    tentativa = tentativa + 1
    
    
        
    
    

print("o numero pensado foi:" , numero_pensado )
print("o computador demorou" , tentativa , "tentativas")
        

        
