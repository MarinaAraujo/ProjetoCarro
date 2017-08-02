from Carro import Carro
class Hibrido (Carro) :
     def __init__(self, cor, modelo, ano):
         Carro.__init__(self, cor, modelo, ano)

     def CarregarBateria (self) :
         print("bateria carregando")
