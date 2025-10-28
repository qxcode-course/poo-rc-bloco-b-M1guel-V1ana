class Pessoa:
    def __init__(self, nome: str, dinheiro: int ):
        self.__nome = nome 
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome
    def getDinheiro(self):
        return self.__dinheiro

    def recebeDinheiro(self, valor: int ):
        self.__dinheiro += valor 

    def pagarMotorista(self, valor: int ):
        if valor > self.__dinheiro:
            valor = self.__dinheiro
        self.__dinheiro -= valor 
        return valor 

    def __str__(self):
        return f"{self.__nome}:R$: {self.__dinheiro:.2f}"



class Moto:
    def __init__(self ):
         self.__custo = 0
         self.__motorista = None  
         self.__passageiro = None
    def setMotorista(self, motoca: Pessoa):
        self.__motorista = motoca
    
    def setPassageiro(self, passageiro : Pessoa):
        self.__passageiro = passageiro

    def entrarMotorista(self, pessoa : Pessoa):
        if self.__motorista is None:
            self.__motorista = pessoa
            print(f"{pessoa.getNome()} é o novo motorista")
        else:
            print("já existe um motorista na moto")

    def embarcarPassegeiro(self, pessoa: Pessoa ):
        if self.__motorista is None:
            print("nao é possivel embarcar um passageiro sem motorista")
        if self.__passageiro is None:
            self.__passageiro = pessoa
            self.__custo = 0

            print(f"{pessoa.getNome()} entrou na moto")
        else:
            print("ja exite passageiro na moto")

    def dirigir(self, km : int):
        if self.__passageiro is None:
            print("nao ha passageiro para embarcar")
            return
        self.__custo += 1 *km 

    def desembarcar(self):
        if self.__passageiro is None:
            print("nao ha passageiro para embarcar")
            return 
        
        dinheiro_passageiro = self.__passageiro.getDinheiro()


        if dinheiro_passageiro >= self.__custo:
            self.__passageiro.pagarMotorista(self.__custo)
            self.__motorista.recebeDinheiro(self.__custo)
            print(f"{self.__passageiro.getNome()}:{int(self.__passageiro.getDinheiro())} left")
        else:
           print("fail: Passenger does not have enough money")
           self.__motorista.pagarMotorista(dinheiro_passageiro)
           print(f"{self.__passageiro.getNome()}:0 left")
           self.__motorista.recebeDinheiro(self.__custo)            
        self.__passageiro = None 
        self.__custo = 0
    
    def __str__(self):
        driver = f"{self.__motorista.getNome()}:{int(self.__motorista.getDinheiro())}"if self.__motorista else "None"
        passa = f"{self.__passageiro.getNome()}:{int(self.__passageiro.getDinheiro())}" if self.__passageiro else "None"
        return f"Cost: {self.__custo}, Driver: {driver}, Passenger: {passa}"

def main():
    motinha = Moto()

    while True:
        line = input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        if args[0] == "show":
            print(motinha)
        if args[0] == "setDriver":
            nome = str(args[1])
            din = int(args[2])
            driver = Pessoa(nome, din)
            motinha.setMotorista(driver)
        if args[0] == "setPass":
            nome = str(args[1])
            dinheiro = int(args[2])
            passageiro = Pessoa(nome, dinheiro)
            motinha.setPassageiro(passageiro)
        if args[0] == "drive":
            valor = int(args[1])
            motinha.dirigir(valor)
        if args[0] == "leavePass":
            motinha.desembarcar()
main()

