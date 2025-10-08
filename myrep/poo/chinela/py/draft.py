class Slipper:
    def __init__(self):
        self.__tamanho : int = 0

    def get_size(self) -> int :
          return self.__tamanho
    def setTamnho(self, valor: int ):
          if valor > 19 and valor < 51: 
              self.__tamanho = valor 
              return
          else: 
              print("fail: o valor digitado não corresponde a um par de chinela ")
              return 

def main():
     chinelin = Slipper()
     while chinelin.get_size() == 0:
          tamanho = int(input(": ")) 
          chinelin.setTamnho(tamanho)
     print("parabens, você comprou uma chinela de tamanho ", chinelin.get_size())
main()     
              