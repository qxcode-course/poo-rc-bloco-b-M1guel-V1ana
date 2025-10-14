class Watch:
    def __init__(self, hora: int = 0 , minuto: int=0 , segundo: int=0):
        self.hora = hora 
        self.minuto = minuto 
        self.segundo =  segundo
    

    def __str__(self):
        return f"{int(self.hora):02d}:{int(self.minuto):02d}:{int(self.segundo):02d}"
    


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
main()