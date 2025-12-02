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
    for parte in partes:
        temp = parte.split("-")
        rangos.append((int(temp[0]), int(temp[1])))
    
    for r in rangos:
        for i in range(r[0], r[1] + 1):
            pass

if __name__ == "__main__":
    main()
