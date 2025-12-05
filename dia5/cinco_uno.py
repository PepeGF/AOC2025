from pathlib import Path
import sys
import traceback

from read_data import read_data_file, read_data_web, save_data

class Cafeteria:
    def __init__(self, data: str) -> None:
        self.data = data
        self.rangos_str, self.numeros_str = self.data.split("\n\n")
        self.rangos: list[list[int]] = sorted([list(map(int, rango.split("-"))) for rango in self.rangos_str.split("\n")])
        with open("rangos.txt", "w") as f:
            for rango in self.rangos:
                f.write(f"{rango}\n")
        self.numeros: list[int] = list(int(numero) for numero in self.numeros_str.split("\n"))
        print(len(self.rangos), len(self.numeros))
        self.checkfreshness()
        print(self.frescos)
    
    def checkfreshness(self):
        self.frescos = 0
        for numero in self.numeros:
            for rango in self.rangos:
                if rango[0] <= numero <= rango[1]:
                    self.frescos += 1
                    break


def main():
    dia = sys.argv[1]
    # check if file input.txt exists
    file = Path(f"dia{dia}/input.txt")
    if not file.exists():
        data = read_data_web()
        save_data(str(dia), data)
    else:
        data = read_data_file(str(dia))
    data = file.read_text()
    caf = Cafeteria(data)



if __name__ == "__main__":
    main()