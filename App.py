from Carro import  Carro
from Hibrido import Hibrido
def main():
    carro1 = Carro("preto", "fusca", "1997")
    carro1.acelerar()
    carro2 = Hibrido("vermelho", "fiesta", "2013")
    carro2.CarregarBateria()
if __name__ == "__main__":
    main()
