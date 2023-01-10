import os
import random

class Main():

    def __init__(self, tentativas = 7, acertos = 0):

        self.tentativas = tentativas # Total de tentativas 
        self.acertos = acertos # Total de Acertos
        self.enforcou = False # Vai ser True se o jogador gastar as tentativas
        self.acertou = False # Vai ser True se o jogador ganhar

    def __Titulo(self): # Titulo do jogo

        print("======================================================")
        print("-------        Welcome Jogo da Forca       -----------")
        print("======================================================")

    def __Enforcou(self, palavrasAcertadas, tentativas): # Caso o jogador perca

        Main().__Titulo()

        print(f"Palavra: {palavrasAcertadas}                 {tentativas} tentativas restante")

        print("\n\n======================================================")
        print("-------             Você Perdeu            -----------")
        print("======================================================")

    def __Acertou(self, palavrasAcertadas, tentativas): # Caso o jogador ganhe

        Main().__Titulo()

        print(f"Palavra: {palavrasAcertadas}                 {tentativas} tentativas restante")

        print("\n\n======================================================")
        print("-------             Você Ganhou            -----------")
        print("======================================================")

    def __EscolhePlavraSecreta(self):

        with open('frutas.txt', 'r') as reader:

            palavras = reader.read().splitlines()

        reader.close()

        return str(palavras[random.randrange(0,len(palavras))].upper())


    def __Loop(self):

        palavraSecreta = Main().__EscolhePlavraSecreta()

        palavrasAcertadas = '-' * len(palavraSecreta)
        while (not self.enforcou and not self.acertou): # Vai executar o for enquanto o jagador não acertar ou perder

            acertouaPalavra = False # Caso o jogador acerte alguma palavra vai ser True
            
            print(f"Palavra: {palavrasAcertadas}                 {self.tentativas} tentativas restante")
            print("======================================================")

            print("\n\n\n\n======================================================")
            letraDigitada = str(input("Adivinhe uma letra: ")).upper().strip() #obtem a letra a ser digitada pelo jogador
            
            posicaoLetra = 1 # Será utilizado para saber a posição da letras


            for ltr in palavraSecreta: # For para ferificação das letras
                
                if (letraDigitada == ltr and self.tentativas > 0): # verifica se a letra é compativel com o que foi digitado
                   
                    acertouaPalavra = True # Indica que o jogador acertou alguma palavra

                    self.acertos += 1 #Incrementa o total de acertos
                    
                    palavrasAcertadas = palavrasAcertadas[:posicaoLetra] + letraDigitada + palavrasAcertadas[posicaoLetra+1:] #Com base na posição substitui _ pela letra digitada
                
                else:

                    exit


                posicaoLetra += 1 # incrementa a posição da letra

            
            if (self.acertos == len(palavraSecreta)): #verifica se o jogador acertou todas as letras
                
                self.acertou == True

                os.system('clear')


                Main().__Acertou(palavrasAcertadas, self.tentativas) # mensagem de parabens

                quit()

            elif (not acertouaPalavra and self.tentativas > 1): # Verifica se o jogador fez alguma tentativa errada
                
                self.tentativas -= 1 # Em caso de tentativa errada decrementa o total de tentativas

                os.system('clear')


                Main().__Titulo()

            elif (not acertouaPalavra and self.tentativas == 1): # Verifica se o jogador fez alguma tentativa errada
                

                self.enforcou == True

                os.system('clear')

                Main().__Enforcou(palavrasAcertadas, 0) # Informa que o jogador perdeu

                quit()


            elif (acertouaPalavra and self.acertos < len(palavraSecreta)): # verifica se o jogador atingiu alguma letra porém não acertou todas as letras
                
                

                os.system('clear')

            
                Main().__Titulo()

            else: # caso o jogador esgote as suas tentaticas
                
                os.system('clear')

                self.enforcou == True

                Main().__Enforcou(palavrasAcertadas, 0) # Informa que o jogador perdeu

                quit()



            
    def Jogar(self):

        os.system('clear')

        Main().__Titulo()

        Main().__Loop()



jogo = Main()

if (__name__ == '__main__'):

    jogo.Jogar()