class Watch:
    def __init__(self, hora: int = 0 , minuto: int=0 , segundo: int=0):
        self.__hora = hora 
        self.__minuto = minuto 
        self.__segundo =  segundo
    
    def getHoras(self):
        return self.hora 
    def getMinutos(self):
        return self.minuto 
    def getSegundos(self):
        return self.segundo
    
    def setHoras(self, h : int):
        if h >23 or h>0:
            self.__hora = h
            return
        else:
            print("horas invalidas")
    def setMin(self, m: int):
        if m > 0 or m < 60 :
            self.__minuto  = m 
            return
        else:
            print("minutos invalidos")
    def setSeg(self, s : int):
        if s > 0 or s < 60:
            self.__segundo = s 
            return
        else:
            print("segundos invalidos")        

    
            

    def __str__(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"
    


def main():
    relogin = Watch()

    while True:
        line = input()
        print("$" + line)
        args = list[args] = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(relogin)
        if args[0] == "set":
            

main()