from typing import Literal

from read_data import read_data_file


def main() -> None:
    data = read_data_file("1")
    lines: list[str] = data.splitlines()
    posicion = 50
    contador_pasos_0 = 0
    for line in lines:
        sentido: Literal[1] | Literal[-1] = 1 if line[0] == "R" else -1
        if sentido == 1:
            for paso in range(int(line[1:])):
                posicion += 1
                if posicion % 100 == 0:
                    contador_pasos_0 += 1
                posicion = posicion % 100
        else:
            for paso in range(int(line[1:])):
                posicion -= 1
                if posicion % 100 == 0:
                    contador_pasos_0 += 1
                posicion = posicion % 100
    print(contador_pasos_0)


if __name__ == "__main__":
    main()
