def append_to_file(some_text: str, file_name: str):

    with open(file_name, "a", encoding="utf-8") as file:
        file.write(f"{some_text}\n")

    with open(file_name, "r", encoding="utf-8") as file2:
        strs = file2.readlines()
        for n in range(len(strs)):
            strs[n] = strs[n].rstrip("\n")

    for str in strs[1:len(strs):2]:
        print(str)


inputted_text = input("Введите текст: ")
inputted_file = input("Введите имя файла: ")
append_to_file(inputted_text, inputted_file)