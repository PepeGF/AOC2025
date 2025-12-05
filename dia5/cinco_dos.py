import sys
import traceback
from pathlib import Path

from read_data import read_data_file, read_data_web, save_data


class Cafeteria:
    def __init__(self, data: str) -> None:
        self.data = data
        self.rangos_str, self.numeros_str = self.data.split("\n\n")
        self.rangos: list[list[int]] = sorted(
            [list(map(int, rango.split("-"))) for rango in self.rangos_str.split("\n")]
        )
        for i in range(len(self.rangos) - 1):
            if self.rangos[i + 1][0] <= self.rangos[i][1]:
                self.rangos[i + 1][0] = self.rangos[i][1]
        indices_eliminar = []
        for i in range(len(self.rangos) - 1):
            if self.rangos[i][1] < self.rangos[i][0]:
                indices_eliminar.append(i)
        for index in reversed(indices_eliminar):
            del self.rangos[index]
        contador = 0
        for i in range(len(self.rangos) - 1):
            contador += self.rangos[i][1] - self.rangos[i][0]
            if self.rangos[i][1] < self.rangos[i + 1][0]:
                contador += 1
        contador += 1  # para el ultimo numero
        print(f"Numeros: {contador}")


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
