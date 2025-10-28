class Carregador:
    def __init__(self, capacidade : int):
        self.__potencia = capacidade

    def getPotencia(self):
        return self.__potencia
    def __str__(self):
        return f"Potencia: {self.__potencia}"

class Bateria:
    def __init__(self, capacidade: int):
        self.__carga = capacidade
        self.__capacidade= capacidade
    
    def getCarga(self):
        return self._carga 
    def getCapacidade(self):
        return self.__capacidade
    
    def descarregar(self, tempo : int):
        self.__carga -= tempo
        if self.__carga < 0:
            self.__carga = 0 

    def carregar(self, tempo: int):
        self.__carga += tempo
        if self.__carga > self.__capacidade:
            self.__carga = self.__capacidade

    def __str__(self):
        return f"({self.__carga}/{self.__capacidade})"

class Not:
    def __init__(self):
        self.__ligado = False
        self.__bateria : Bateria None | None
        self.__carregador : Carregador None | None

    def ligar(self):
        if self.__ligado:
            print("fail: notebook ja esta ligado")
        elif self.__bateria is None and self.__carregador is None :
            print("fail: nao foi possivel ligar")
        elif self.__bateria is not None and self.__bateria.getCarga() >0:
            self.__ligado = True
            print("notebook ligado")
        elif self.__bateria is None and self.__carregador is not None:
            self.__ligado = True 
            print("notebook ligado")
        else:
            print("fail: nao foi possivel ligar o notebook")
    
    def deligar(self):
        if not self.__ligar:
            print("fail: notebook ja esta ligado")
        else:
            self.__ligado = False
            print("notebook desligado")
    def usar(self, tempo : int):
        if not self.__ligado:
            print("fail: ligue o notebook primeiro")
            return
        print(f"usado por {tempo} minutos")

        if self.__bateria and self.__carregador:
            ganho = self.__carregador.getPotencia * tempo
            self.__bateria.carregar(ganho)

        elif self.__bateria:
            self.__bateria.descarregar(tempo)
            if self.__bateria.getCarga() == 0:
                print("notebook descarregou")
                self.__ligado = False
    
    def mostrar(self):
        status = "ligado" if self.__ligado else: "deslogado"
        bateria = str(self.__bateria) if self.__bateria else: "nenhuma"
        carregador = str(self.__carregador) if self.__carregador else: "desconectado"
        print(f"Status:{status}, Bateria:{bateria}, Carregador: {carregador}")

    def setBateria(self, capacidade : int):
        self.__bateria = Bateria(capacidade)
        print("bateria adicionada")

    def rmBateria(self):
        if self.__bateria:
            print("bateria removida")
            temp = self.__bateria
            self.__bateria = None 
            return temp
        else:
            print("fail: sem bateria")
            return None 

    def setCarregador(self, potencia : int):
        self.__carregador = Carregador(potencia)
        print("carregador conectado")

    def rmCarregador(self):
        if self.__carregador:
            print("carregador desconectado")
            self.__carregador = None 
        else:
            print("fail: sem carregador")



