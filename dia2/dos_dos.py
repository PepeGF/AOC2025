from pathlib import Path

from read_data import read_data_file, read_data_web, save_data


def main():
    # check if file input.txt exists
    file = Path("dia2/input.txt")
    if not file.exists():
        data = read_data_web()
    else:
        data = read_data_file("2")

    rangos: list[tuple[int, int]] = []
    partes = data.split(",")
    partes[-1] = partes[-1].strip("\n")
    for parte in partes:
        temp = parte.split("-")
        rangos.append((int(temp[0]), int(temp[1])))

    suma = 0
    for r in rangos:
        for i in range(r[0], r[1] + 1):
            string = str(i)
            longitud = len(string)
            for sublong in range(1, longitud // 2 + 1):
                substr = [string[j : j + sublong] for j in range(0, longitud, sublong)]
                if all(x == substr[0] for x in substr):
                    print(f"{i} \t\t--> {sublong} \t {substr}", file=f)
                    suma += i
                    break
    print(suma)


if __name__ == "__main__":
    main()
