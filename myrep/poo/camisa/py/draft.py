class Camisa:
    def __init__(self):
        self.__tamanhoroupa:  str = ""

    def getTamanho(self):
        return  self.__tamanhoroupa
    
    def setTamanho(self, valor: str):
        if valor in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanhoroupa = valor
        else:
            print("Tamanho da roupa não encontrado!") 
            
        
def main():
    blusa = Camisa()
    while blusa.getTamanho() == "":
        tamanho= input(": ")  
        blusa.setTamanho(tamanho)    
    print("Parabens você comprou uma roupa de tamanho", blusa.getTamanho())

main()