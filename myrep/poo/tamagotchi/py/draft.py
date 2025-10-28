class Tamagotchi:
    def __init__(self, energyMax: int, cleanMax : int ):
        self.energyMax = energyMax
        self.cleanMax = cleanMax
        self.energy = energyMax
        self.clean = cleanMax
        self.age = 0 
        self.alive = True 

    def set_energy(self, valor: int):
        if valor <= 0 :
            self.energy = 0 
            self.alive = False 
            return "fail: pet morreu de fraqueza"
        elif valor > self.energyMax:
            self.energy = self.energyMax
        else:
            self.energy = valor 
            return None

    def set_clean(self, valor: int):
        if valor <= 0:
            self.clean = 0
            self.alive = False
            return "fail: pet morreu de sujeira"
        elif valor > self.cleanMax:
            self.clean = self.cleanMax
        else:
            self.clean = valor 
            return None 
    
    def isalive(self):
        return self.alive
    
    def __str__(self):
        status = "vivo" if self.alive else "morto"
        return f"E:{self.energy}/{self.energyMax}, L:{self.clean}/{self.cleanMax}, I:{self.age}"



class Game:
    def __init__(self):
        self.pet = None
    

    def init(self, energyMax, cleanMax):
        self.pet = Tamagotchi(energyMax, cleanMax)
    

    def jogar(self):
        if not self.pet.isalive():
            return "fail: pet esta morto"
        
        m_energy = self.pet.set_energy(self.pet.energy - 2)
        m_clean = self.pet.set_clean(self.pet.clean -3 )
        self.pet.age += 1
        
        if m_energy :
            return m_energy
        if m_clean:
            return m_clean
        
        return None


    def dormir(self):
        if not self.pet.isalive():
            return "fail: pet esta morto"
        
        if self.pet.energy > self.pet.energyMax - 5:
            return "fail: nao esta com sono"


        turnos = self.pet.energyMax - self.pet.energy
        men = self.pet.set_energy(self.pet.energyMax)


        if men:
            return men
        self.pet.age += turnos
        return None
    
    def shower(self):
        if not self.pet.isalive():
            return "fail: pet esta morto"
        
        
        msg_energy = self.pet.set_energy(self.pet.energy - 3)
        msg_clean = self.pet.set_clean(self.pet.cleanMax)
        self.pet.age += 2


        if msg_energy:
            return msg_energy
        if msg_clean:
            return msg_clean
        return None 

    def show(self):
        return str(self.pet)


def main():

    game = Game()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "init":
            energy = int(args[1])
            clean = int(args[2])
            game.init(energy, clean)
        if args[0] == "show":
            print(game.show())
        if args[0] == "play":
            msg = game.jogar()
            if msg:
                print(msg)
        if args[0] == "sleep":
            msg = game.dormir()
            if msg:
                print(msg)

        if args[0] == "shower":
            msg = game.shower()
            if msg:
                print(msg)
main()
