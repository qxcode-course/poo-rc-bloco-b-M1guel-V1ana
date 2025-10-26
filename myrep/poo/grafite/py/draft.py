class GrafiteLead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.__thickness = thickness
        self.__hardness = hardness
        self.__size = size 

    def getSize(self):
        return self.__size
    
    def setSize(self, tamanho: int):
        self.__size -= tamanho

        if self.__size <= 0:
            self.__size = 0 


    def usagePerSheet(self):
        if self.__hardness == "HB":
            return 1
        elif self.__hardness == "2B":
            return 2 
        elif self.__hardness == "4B":
            return  4
        elif self.__hardness == "6B":
            return 6 
        else:
            return 0 

    def __str__(self):
        return f"{self.__thickness}:{self.__hardness}:{self.__size}mm"

class Pencil:
    def __init__(self, thickness : float):
        self.__thickness = thickness
        self.__tip = None 

    
    def hasGrafite(self):
        return self.__tip is not None 
    
    def insert(self, thickness: float, hardness: str, size : int):
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return 
        if thickness != self.__thickness:
            print("fail: calibre incompativel")
            return    
        self.__tip = GrafiteLead(thickness, hardness, size)

    
    def remove(self):
        if not self.hasGrafite():
            print("fail: nao exite grafite")
            return
        remover = self.__tip 
        self.__tip = None 
        print(f"grafite removido: {remover}")

    def writePage(self):
        if not self.hasGrafite():
            print("fail: nao tem grafite")
            return 
        
        usar = self.__tip.usagePerSheet()

        if self.__tip.getSize() <= 10:
            print("fail: tamanho insuficiente")
            return
        if self.__tip.getSize() - usar < 10:
            usar = self.__tip.getSize - 10
            self.__tip.setSize(usar)
            
            print (f"fail: folha incompleta, gastou {usar}mm")
        else:
            self.__tip.setSize(usar)
            print("folha completa")

    def __str__(self):
        if self.hasGrafite():
            return f"calibre: {self.__thickness}, grafite{self.__tip}"
        else:
            return f"calibre: {self.__thickness}, grafite: null"

def main():

    lapiseira = Pencil

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(lapiseira)
        if args[0] == "init":
            calibre = float(args[1])
            lapiseira = Pencil(calibre)
        if args[0] == "insert":
            tamanho_grafite = float(args[1])
            espessura = str(args[2])
            tamanho = int(args[1])
            lapiseira.insert(GrafiteLead(thickness, hardness, size))

main()