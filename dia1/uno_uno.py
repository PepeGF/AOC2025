from typing import Literal

from read_data import read_data_file, read_data_web, save_data


def main():
    data: str = read_data_file("1")
    lines: list[str] = data.splitlines()

    inicio = 50
    contador_ceros = 0
    for line in lines:
        sentido: Literal[1] | Literal[-1] = 1 if line[0] == "R" else -1
        pasos: int = int(line[1:]) % 100
        posicion: int = (inicio + sentido * pasos) % 100
        if posicion == 0:
            contador_ceros += 1
        inicio = posicion
    print(contador_ceros)


if __name__ == "__main__":
    main()
