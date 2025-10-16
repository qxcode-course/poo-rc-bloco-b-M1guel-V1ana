class Notebook:
    def __init__(self):
        self.__ligar : bool = False
    

    def getLigar(self):
        return self.__ligar
    
    def setLigar(self, valor : bool):
        self.__ligar = valor 
        return
    
    def Ligar(self):
        if not self.__ligar:
            self.ligar = True
            print("notebook ligado.")
        else:
            print("notebook já está ligado.")

    

def main():
    pc = Notebook()

    while True:
        line = input()
        print("$" + line)
        args: list[args] = line.split()

        if args[0] == "end":
            break
        if args[0] == "mostrar":
            print(pc)
main()