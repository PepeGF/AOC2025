import sys
import traceback
from pathlib import Path

from read_data import read_data_file, read_data_web, save_data


class Calculator:
    def __init__(self, data: str) -> None:
        self.data = data
        self.lines_raw = self.data.split("\n")
        operations = self.lines_raw[-1].split()
        self.numbers: list[int] = []
        total = 0
        for line in self.lines_raw[:-1]:
            numbers = list(map(int, line.split()))
            self.numbers.append(numbers)
        for i in range(len(operations)):
            if operations[i] == "+":
                parcial = 0
                for j in range(len(self.numbers)):
                    parcial += self.numbers[j][i]
            elif operations[i] == "*":
                parcial = 1
                for j in range(len(self.numbers)):
                    parcial *= self.numbers[j][i]
            total += parcial
        print(f"Total: {total}")
        # print(f"Operations: {operations}")


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
    Calculator(data)


if __name__ == "__main__":
    main()
