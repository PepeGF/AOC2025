from pathlib import Path

from read_data import read_data_file, read_data_web, save_data


def main():
    # check if file input.txt exists
    file = Path("dia2/input.txt")
    if not file.exists():
        data = read_data_web()
    else:
        data = read_data_file(2)


if __name__ == "__main__":
    main()
