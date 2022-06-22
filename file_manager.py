from tkinter import filedialog
from tkinter import Tk
import os
import shutil

Tk().withdraw()

def choose_file():
    filename = filedialog.askopenfilename(
            title="Выберите файл",
            filetypes=(("All Files", "*.*"),
                        ("Text files", "*.txt"))
            )
    return filename

def choose_directory():
    dirname = filedialog.askdirectory(title="Вебрите директорию.")
    return dirname

def rename_file(from_file, to_file):
    ext = os.path.splitext(from_file)[-1]
    dirname = os.path.dirname(from_file)
    new_file = os.path.join(dirname, to_file+ext)
    os.rename(from_file, new_file)

def main():
    print("Выберите опцию:")
    print("1 - Oткрытие файла")
    print("2 - Копирование файла")
    print("3 - Удаление файла")
    print("4 - Переименовать файл")
    print("5 - Переместить файл")
    print("6 - Создать папку")
    print("7 - Удалить папку")
    print("8 - Показать все документы в папке")
    

    options = [i for i in range(1, 9)]
    choice = ""
    while choice not in options:
        choice = int(input("Нажмите цифру (1-8):> "))

    if choice == 1:
        file = choose_file()
        os.startfile(file)

    if choice == 2:
        to_copy = choose_file()
        to_location = choose_directory()
        shutil.copy(to_copy, to_location)

    if choice == 3:
        file = choose_file()
        os.remove(file)

    if choice == 4:
        file = choose_file()
        new_name = input("Укажите новое название:> ")
        rename_file(file, new_name)

    if choice == 5:
        file = choose_file()
        to_location = choose_directory()
        shutil.move(file, to_location)

    if choice == 6:
        folder = choose_directory()
        name = input("Придумайте название папке:> ")
        folder_name = folder + "/" + name
        os.mkdir(folder_name)

    if choice == 7:
        folder = choose_directory()
        shutil.rmtree(folder)

    if choice == 8:
        folder = choose_directory()
        items = os.listdir(folder)
        print("Это папки или файлы в этом каталоге")
        for item in items:
            print(item)

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)

        cont = input("Для выхода нажмите любую кнопку:")
        if cont != "":
            break
    