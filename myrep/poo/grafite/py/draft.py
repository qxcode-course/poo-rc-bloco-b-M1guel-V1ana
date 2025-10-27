class GrafiteLead:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usePerSheet(self):
        gastos = {"HB": 1, "2B": 2, "4B": 4, "6B": 6}
        return gastos.get(self.hardness, 0)
    
    def __str__(self):
        return f"{self.thickness}:{self.hardness}:{self.size}"

    

class Pencil:
    def __init__(self, thickness : float):
        self.__thickness = thickness
        self.__tip = None 


    def hasGrafite(self) -> bool:
        return self.__tip is not None

    def insert(self, ponta: GrafiteLead) -> bool:
        if self.hasGrafite():
            print("fail: ja existe grafite")
            return False 
        if ponta.thickness != self.__thickness:
            print("fail: calibre incompativel")
            return False
        self.__tip = ponta 
        return True 

    def __str__(self):
        if self.hasGrafite():
            return f"calibre: {self.__thickness}, grafite: [{self.__tip}]"

        else:
            return f"calibre: {self.__thickness}, grafite: null"

    
    def remove(self):
        if not self.hasGrafite():
            print("fail: nao existe grafite")
            return 

        remover = self.__tip
        self.__tip = None
        return remover

    def writePage(self):
        if not self.hasGrafite():
            print ("fail: nao existe grafite")
            return False
        
        grafite = self.__tip


        gasto = grafite.usePerSheet()

        if gasto < 0 :
            print("fail: dureza invalida")
            return False

        if grafite.size <= 10:
            print("fail: tamanho insuficiente")
            return False
        
        grafite.size -= gasto
        if grafite.size < 10:
            grafite.size = 10
        print("fail: folha incompleta")
        return True

def main():
    lapiseira = None

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
            if lapiseira:
                esp = float(args[1])
                dur= str(args[2])
                tam = int(args[3])
                grafite = GrafiteLead(esp, dur, tam)
                lapiseira.insert(grafite)
            else:
                print("lapiseira nao inicializada")
        if args[0] == "remove":
            lapiseira.remove()
        if args[0] == "write":
            if lapiseira:
                lapiseira.writePage()


        


main()