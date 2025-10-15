class Watch:
    def __init__(self, hora: int = 0, minuto: int = 0, segundo: int = 0):
        self.__hora = 0
        self.__minuto = 0
        self.__segundo = 0
        
        self.setHoras(hora)
        self.setMin(minuto)
        self.setSeg(segundo)
    
    def getHoras(self):
        return self.__hora 

    def getMinutos(self):
        return self.__minuto 

    def getSegundos(self):
        return self.__segundo
    
    def setHoras(self, h: int):
        if h >= 0 and h <= 23:
            self.__hora = h
        else:
            print("fail: hora invalida")
        
    def setMin(self, m: int):
        if m >= 0 and m <=59:
            self.__minuto = m
        else:
            print("fail: minuto invalido")

    def setSeg(self, s: int):
        if s >=0 and s<= 59 :
            self.__segundo = s
        else:
            print("fail: segundo invalido")   
        
    def nextSecond(self):
        self.__segundo += 1
        if self.__segundo > 59:
            self.__segundo = 0
            self.__minuto += 1
        if self.__minuto > 59:
            self.__minuto = 0
            self.__hora += 1
        if self.__hora > 23:
            self.__hora = 0

    def __str__(self):
        return f"{self.__hora:02d}:{self.__minuto:02d}:{self.__segundo:02d}"
    

def main():
    relogin = Watch()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break

        if args[0] == "show":
            print(relogin)

        if args[0] == "init":
            h, m, s = map(int, args[1:])
            relogin = Watch(h, m, s )
            

        if args[0] == "set":
            h, m, s = map(int, args[1:])
            relogin.setHoras(h)
            relogin.setMin(m)
            relogin.setSeg(s)

        if args[0] == "next":
            relogin.nextSecond()


main()
