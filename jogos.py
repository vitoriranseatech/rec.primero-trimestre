# import forca 
# import adivinhação
def escolha_jogo():
    print("escolha o seu jogo")
    print("(1) forca (2) adivinhação")
    
    jogo = int(input("qual jogo"))
    
    if(jogo== 1):
        print("jogando forca")
        # forca.jogar()
    elif(jogo == 2):
        print("jogando adivinhação")
        # adivinhação.jogar()
        
if(__name__ == "__main__"):
    escolha_jogo()