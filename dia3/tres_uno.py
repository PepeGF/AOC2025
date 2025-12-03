from pathlib import Path

from read_data import read_data_file, read_data_web, save_data


def main():
    dia = 3
    # check if file input.txt exists
    file = Path(f"dia{dia}/input.txt")
    if not file.exists():
        data = read_data_web()
    else:
        data = read_data_file(str(dia))

    raw_list = data.split("\n")
    # digits = [int(char) for char in raw_list[0]]
    # print(digits[max_pos] * 10 + digits[max_pos + 1 + max_pos2])
    suma = 0
    i = 0
    with open("dia3/debug.txt", "w") as f:
        for string in raw_list:
            digits: list[int] = [int(char) for char in string]
            i += 1
            for subdigits in digits:
                try:
                    max_pos = digits.index(max(digits))
                    if max_pos == len(digits) - 1:
                        max_pos = digits[:max_pos].index(max(digits[:max_pos]))
                    max_pos2 = digits[max_pos + 1 :].index(max(digits[max_pos + 1 :]))
                    number = digits[max_pos] * 10 + digits[max_pos + 1 + max_pos2]
                except ValueError as e:
                    print(e.with_traceback())
                    print(f"Error en la línea {i} con dígitos {digits}")
                    exit()
            f.write(
                f"Linea {i}: {max_pos}, {max_pos2 + max_pos} -> {digits[max_pos]} | {digits[max_pos + max_pos2 + 1]} = {number}\n"
            )
            suma += number

    print(f"suma: {suma}")


if __name__ == "__main__":
    main()
