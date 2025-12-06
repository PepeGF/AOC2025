import sys
import traceback
from pathlib import Path

from read_data import read_data_file, read_data_web, save_data


class Calculator:
    def __init__(self, data: str) -> None:
        self.data = data
        self.lines_raw = self.data.split("\n")
        self.reversed_lines: list[list[str]] = []
        for line in self.lines_raw:
            line_list = list(line)
            line_list.reverse()
            self.reversed_lines.append(line_list)
        self.reversed_lines = list(map(list, zip(*self.reversed_lines)))
        self.string_lines: list[str] = []
        for line in self.reversed_lines:
            self.string_lines.append("".join(line).strip())
        self.total = 0
        self.temp_list = []
        for line in self.string_lines:
            temp_result = 0
            if len(line) != 0:
                try:
                    self.temp_list.append(int(line))
                except ValueError:
                    self.temp_list.append(int(line[:-1]))
                    operator = line[-1]
                    if operator == "+":
                        temp_result = sum(self.temp_list)
                    if operator == "*":
                        temp_result = 1
                        for num in self.temp_list:
                            temp_result *= num
                    self.total += temp_result
            else:
                self.temp_list.clear()
                continue


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
    calc = Calculator(data)
    print(f"Total: {calc.total}")


if __name__ == "__main__":
    main()
