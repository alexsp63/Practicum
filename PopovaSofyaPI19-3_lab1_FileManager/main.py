import os, sys
from settings import *
from folder import *

def help():
    print()
    print("""*****Справка по командам*****
       show - показать содержимое директории;
       createdir <name> - создание папки c именем <name> в текущей директории;
       removedir <name> - удаление папки с именем <name> в текущей директории;
       go <name> - перемещение в папку с именем <name>, . - на уровень выше, .. - в корневой каталог;
       createfile <name> - создание файла с указанием имени;
       write <name> <text> - запись текст <text> в файл с именем <name>;
       read <name> - просмотр содержимого текстового файла;
       removefile <name> - удаление файла по имени;
       copyfile <filename> <folder>/<newfilename> - копирование файла <filename> в директорию <folder> 
                                                    с сохранением имени или в файл <newfilename>;
       movefile <filename> <folder>/<newfilename> - перемещение файла <filename> в директорию <folder> 
                                                    или в файл <newfilename> с сохранением информации;
       renamefile <oldfilename> <newfilename> - переименование файла из <oldfilename> во <new file name>.
       """)
    print()

while True:
    try:
        main_directory = input("\033[34mВведите рабочую папку (она будет восприниматься программой как корневая) >> \033[0m")
        home = MainDirectory(main_directory)
        root_directory = os.getcwd()
        print("\033[33mВ качестве корневой установлена директория \033[0m" + root_directory)
        break
    except FileNotFoundError:
        print("\033[31mНельзя установить директорию в качестве корневой, так как её не существует! Попробуйте снова!\033[0m")
        continue
    except (EOFError, KeyboardInterrupt):
        print()
        print("\033[31mРабота программы завершена\033[0m")
        sys.exit(0)

help()
nested_folder = ""
#начинаем мы с объявленной нами корневой директории
current_directory = Folder(root_directory)
aviable_commands = ("createdir", "show", "removedir", "go", "createfile", "write", "read", "removefile", "copyfile", "movefile", "renamefile")
while True:
    try:
        command = input("\033[32m" + current_directory.name + nested_folder + " >> \033[0m")
        list_of_command = command.split(' ')
        if list_of_command[0] in aviable_commands:
            name = ' '.join(list_of_command[i] for i in range(1, len(list_of_command)))

            #команда отображения содержимого директории
            if (list_of_command[0] == "show"):
                if len(list_of_command) == 1:
                    current_directory.show(current_directory.name)
                    continue
                else:
                    try:
                        current_directory.show(current_directory.name + "\\" + name)
                        continue
                    except OSError:
                        current_directory.show(name)
                        continue

            #команды создания/удаления папок
            if list_of_command[0] in ("createdir", "removedir") and len(list_of_command) != 1:
                if list_of_command[0] == "createdir":
                    current_directory.createdir(name)
                    continue
                if list_of_command[0] == "removedir":
                    current_directory.removedir(name)
                    continue

            #переход в другие директории
            if list_of_command[0] == "go" and len(list_of_command) != 1:
                name = name.replace("/", "\\")
                if name == "..":
                    current_directory.go(root_directory)
                    continue
                elif name == ".":
                    if current_directory.name != root_directory:
                        d = current_directory.name.split("\\")
                        d = d[:-1]
                        fd = "\\".join(d)
                        current_directory.go(fd)
                        continue
                    else:
                        print("\033[31mВы не можете выйти из корневой директории!\033[0m")
                        continue
                else:
                    try:
                        current_directory.go(current_directory.name + "\\" + name)
                        continue
                    except OSError:
                        if root_directory in name:
                            current_directory.go(name)
                            continue
                        else:
                            print("\033[31mВы не можете выйти из корневой директории!\033[0m")
                            continue

            #создание файла
            if list_of_command[0] == "createfile" and len(list_of_command) == 2:
                current_directory.createfile(name.replace("/", "\\"))
                continue

            #запись текста в файл
            if list_of_command[0] == "write" and len(list_of_command) >= 3:
                file_name = list_of_command[1]
                file_text = ' '.join(list_of_command[i] for i in range(2, len(list_of_command)))
                current_directory.write(file_name.replace("/", "\\"), file_text)
                continue

            #чтение содержимого файла
            if list_of_command[0] == "read" and len(list_of_command) == 2:
                current_directory.read(name.replace("/", "\\"))
                continue
            
            #удаление файла по имени
            if list_of_command[0] == "removefile" and len(list_of_command) == 2:
                current_directory.removefile(name.replace("/", "\\"))
                continue

            #копирование файла
            if list_of_command[0] == "copyfile" and len(list_of_command) == 3:
                what_to_copy = list_of_command[1]
                where_to_copy = list_of_command[2]
                current_directory.copyfile(what_to_copy.replace("/", "\\"), where_to_copy.replace("/", "\\"))
                continue

            #перемещение файла
            if list_of_command[0] == "movefile" and len(list_of_command) == 3:
                what_to_move = list_of_command[1]
                where_to_move = list_of_command[2]
                current_directory.movefile(what_to_move.replace("/", "\\"), where_to_move.replace("/", "\\"))
                continue

            #переименование файла
            if list_of_command[0] == "renamefile" and len(list_of_command) == 3:
                old_name = list_of_command[1]
                new_name = list_of_command[2]
                current_directory.movefile(old_name.replace("/", "\\"), new_name.replace("/", "\\"))
                continue

            else:
                print("\033[31mИмя папки/файла не может быть пустым, а имя файлов не должно содержать пробелов!\033[0m")
                continue

        else:
            raise Exception
    except (EOFError, KeyboardInterrupt):
        print()
        print("\033[31mРабота программы завершена\033[0m")
        sys.exit(0)
    except Exception:
        print("\033[31mТакой команды не существует или она уже была выполнена!\033[0m")
        continue

