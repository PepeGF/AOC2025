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
    suma = 0
    indexes = []
    j = 0
    raw_list = data.split("\n")


    with open("dia3/debug2.txt", "w") as f:
        for string in raw_list:
            digits: list[int] = [int(char) for char in string]
            inicio = 0
            indexes.clear()
            for k in range(12, 1, -1):
                index = digits[inicio:-k].index(max(digits[inicio:-k]))
                indexes.append(index)
                inicio = index + 1
            index = digits[inicio:].index(max(digits[inicio:]))
            indexes.append(index + inicio)

            """ 
            digits: list[int] = [int(char) for char in string]
            index_1 = digits[:-11].index(max(digits[:-11]))
            indexes.append(index_1)
            inicio = index_1 + 1
            index_2 = digits[inicio : -10].index(max(digits[inicio : -10]))
            indexes.append(index_2 + inicio)
            inicio = index_2 + inicio + 1
            index_3 = digits[inicio : -9].index(max(digits[inicio : -9]))
            indexes.append(index_3 + inicio)
            inicio = index_3 + inicio + 1
            index_4 = digits[inicio : -8].index(max(digits[inicio : -8]))
            indexes.append(index_4 + inicio)
            inicio = index_4 + inicio + 1
            index_5 = digits[inicio : -7].index(max(digits[inicio : -7]))
            indexes.append(index_5 + inicio)
            inicio = index_5 + inicio + 1
            index_6 = digits[inicio : -6].index(max(digits[inicio : -6]))
            indexes.append(index_6 + inicio)
            inicio = index_6 + inicio + 1
            index_7 = digits[inicio : -5].index(max(digits[inicio : -5]))
            indexes.append(index_7 + inicio)
            inicio = index_7 + inicio + 1
            index_8 = digits[inicio : -4].index(max(digits[inicio : -4]))
            indexes.append(index_8 + inicio)
            inicio = index_8 + inicio + 1
            index_9 = digits[inicio : -3].index(max(digits[inicio : -3]))
            f.write(f"index_9: {str(digits[inicio : -3])}\n")
            indexes.append(index_9 + inicio)
            inicio = index_9 + inicio + 1
            index_10 = digits[inicio : -2].index(max(digits[inicio : -2]))
            f.write(f"index_10: {str(digits[inicio : -2])}\n")
            indexes.append(index_10 + inicio)
            inicio = index_10 + inicio + 1
            index_11 = digits[inicio : -1].index(max(digits[inicio : -1]))
            f.write(f"index_11: {str(digits[inicio : -1])}\n")
            indexes.append(index_11 + inicio)
            inicio = index_11 + inicio + 1
            index_12 = digits[inicio : ].index(max(digits[inicio : ]))
            f.write(f"index_12: {str(digits[inicio : ])}\n")
            
            indexes.append(index_12 + inicio)
            inicio = index_12 + inicio + 1
             """
            texto = (
                f"{''.join([str(digits[i]) for i in indexes])}"
            )
            # f.write(f"{j+1}: {str(indexes)} -> {texto}\n")
            suma += int(texto)
            print(f"{j+1}: {str(indexes)} -> {texto}")
            # indexes = []
            if j == 2:
                exit()
            j += 1
    print(f"suma: {suma}")



if __name__ == "__main__":
    main()