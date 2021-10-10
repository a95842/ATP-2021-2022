def intro():
    turno = input("Jogo dos 21 fosforos! Escreve 'jogador 1' ou 'jogador 2' caso pretendas ser o jogador 1 ou o jogador 2:") 
    if turno == "jogador 1" :
        jogadas_humano_primeiro()
    elif turno == "jogador 2" :
        jogadas_cpu_primeiro()
    else :
        print('Palavras incorretas!')
        intro()
            
        
def jogadas_humano_primeiro ():
    fosforos = 21
     
    while fosforos >= 1 :
        retirar = int(input("Quanto fosforos pretendes retirar?"))
        
           
        if retirar >= 5 or retirar <= 0 :
                    print ("Relembrar que so e possivel tirar entre 1-4 fosforos por jogada!")
            
        else:
              
                fosforos = fosforos - retirar
                if fosforos == 0:
                    print("0 fosforos restam! Computador vence!")
                elif fosforos <0:
                    print("Impossivel tirar tantos fosforos e por isso o computador vence!")
                else:
                    cpu_retirar = 5 - retirar
                    fosforos = fosforos - cpu_retirar
                    print ("O computador retirou:" , cpu_retirar)
                    print("Quantidade de fosforos restantes:" , fosforos)
   
        
    return fosforos



def jogadas_cpu_primeiro():
    import random

    fosforos =21
    retirar_inicial =  random.randint(1 , 4)
    fosforos = fosforos - retirar_inicial
    print ("O computador retirou:" , retirar_inicial)
    print("Quantidade de fosforos restantes:" , fosforos)
    
    retirar = int(input("Quanto fosforos pretendes retirar?"))
    
    if retirar >= 5 or retirar <= 0 :
                print ("Relembrar que so e possivel tirar entre 1-4 fosforos por jogada!")
        
    else:
        fosforos = fosforos - retirar
        
        
        if retirar_inicial + retirar != 5 :
            while fosforos >= 1 :
                        
                        if fosforos <= 5 :
                            retirar_cpu = fosforos - 1
                            fosforos = fosforos - retirar_cpu
                            print ("O computador retirou:" , retirar_cpu)
                            print("Quantidade de fosforos restantes:" , fosforos)
                            
                            print("Tu tiras o ultimo fosforo e o computador ganhou!")
                            import sys

                            sys.exit()
                            
                        else:
                            retirar_cpu = 5 - retirar
                            fosforos = fosforos - retirar_cpu
                            print ("O computador retirou:" , retirar_cpu)
                            print("Quantidade de fosforos restantes:" , fosforos)
            
                        retirar = int(input("Quanto fosforos pretendes retirar?"))
                    
                    
                        if retirar >= 5 or retirar <= 0 :
                                print ("Relembrar que so e possivel tirar entre 1-4 fosforos por jogada!")
                        
                        else:
                            fosforos = fosforos - retirar
                            print("Quantidade de fosforos restantes:" , fosforos)
                        
                        
                        
                        
        if retirar_inicial + retirar == 5:
            while fosforos > 1 :
                retirar_inicial =  random.randint(1 , 4)
                fosforos = fosforos - retirar_inicial
                print ("O computador retirou:" , retirar_inicial)
                print("Quantidade de fosforos restantes:" , fosforos)
            
                retirar = int(input("Quanto fosforos pretendes retirar?"))
            
                if retirar >= 5 or retirar <= 0 :
                        print ("Relembrar que so e possivel tirar entre 1-4 fosforos por jogada!")
                
                else: 
                    
                    fosforos = fosforos - retirar
                    if fosforos < 0 :
                        print("impossivel retirar tantos fosforos")
                    
                    else:
                        print("Quantidade de fosforos restantes:" , fosforos)
            
            if fosforos == 1 :
                print("O computador tirou o ultimo fosforo e tu ganhaste!")
        
        
        
intro()
