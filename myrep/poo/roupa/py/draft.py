class Roupa:
    def __init__(self):
        self.__tamanhoroupa : str = ""

    def getTamanho(self):
        return self.__tamanhoroupa    
    def setTamanho(self, valor : str):
        if valor in ["PP", "P", "M", "G", "GG", "XG"]:
            self.__tamanhoroupa = valor 
        else:
            print("fail: valor invalido, tente PP, P, M, G, GG ou XG")

def main():
    roupa = Roupa()
    
    while roupa.getTamanho() == "":
        line = input()
        print("$" + line)
        args : list[str] = line.split()

        if len(args) == 0: 
            continue 
        if args[0] == "end":
            break
        elif args[0] == "show":
            print("size:", roupa.getTamanho())
        elif args [0] == "size":
            if len(args) > 1:
                roupa.setTamanho(args[1])

        else: 
            print("fail: valor invalido, tente PP, P, M, G, GG ou XG")    

main()