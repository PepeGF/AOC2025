from pathlib import Path
import sys
import traceback

from read_data import read_data_file, read_data_web, save_data


class ScrollsLibrary:
    def __init__(self, lines: list[str]) -> None:
        self.lines = lines
        self.number_lines = len(lines)
        self.long_line = len(lines[0])
        self.scrolls_count: int = 0
        self.current_line: int = 0
        # self.count_scrolls()
        self.removable_scrolls = []
        self.removed_scrolls = 0
        while self.count_scrolls() > 0:
            self.remove_scrolls()
        print(f"Total removed scrolls: {self.removed_scrolls}")
    
    def count_scrolls(self) -> int:
        scrolls = 0
        for i in range(0, self.number_lines):
            self.current_line = i
            for j in range(0, self.long_line):
                if self.lines[i][j] != "@":
                    continue
                scrolls = 0
                self.current_column = j
                scrolls += self.check_same_line()
                if i > 0:
                    scrolls += self.check_prev_line()
                if scrolls > 3:
                    continue
                if i < self.number_lines - 1:
                    scrolls += self.check_next_line()
                if scrolls > 3:
                    continue
                self.removable_scrolls.append((i, j))
                self.scrolls_count += 1
        return self.scrolls_count

    def remove_scrolls(self) -> None:
        for i, j in self.removable_scrolls:
            self.lines[i][j] = "."
            self.removed_scrolls += 1
            # self.lines[i] = "".join(line)
        self.removable_scrolls.clear()
        self.scrolls_count = 0

    def check_same_line(self) -> int:
        count = 0
        for k in [self.current_column - 1, self.current_column + 1]:
            if k == -1 or k == self.long_line:
                continue
            if self.lines[self.current_line][k] == "@":
                count += 1
        return count
    
    def check_prev_line(self) -> int:
        count = 0
        for k in [self.current_column - 1, self.current_column, self.current_column + 1]:
            if k == -1 or k == self.long_line:
                continue
            if self.lines[self.current_line - 1][k] == "@":
                count += 1
        return count
    
    def check_next_line(self) -> int:
        count = 0
        for k in [self.current_column - 1, self.current_column, self.current_column + 1]:
            if k == -1 or k == self.long_line:
                continue
            if self.lines[self.current_line + 1][k] == "@":
                count += 1
        return count


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
    lineas = data.split("\n")
    library = ScrollsLibrary(lineas)



if __name__ == "__main__":
    main()
