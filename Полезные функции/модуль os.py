import os

print(os.name)  # имя текущей ОС
print(os.environ)  # сведения, которые касаются конфигурации компьютера
print(os.getenv("TMP"))  #C:\Users\Alex\AppData\Local\Temp
print(os.getcwd())  # сведения о текущей директории C:/Py/py pro/
os.chdir('C:/Py/py pro/inout/')  # смена текущей директории
print(os.getcwd())  # C:/Py/py pro/inout/
print(os.path.exists('C:/Py/py pro/inout/data.pkl'))  # проверка существования пути
print(os.path.isfile('C:/Py/py pro/inout/data.pkl'))  # это файл?
print(os.path.isdir('C:/Py/py pro/inout/data.pkl'))  # это директория?
# os.mkdir('C:/Py/tmp')  # создать директорию
# os.makedirs('C:/Py/tmp1/tmp2/tmp3') # создать цепочку директорий, кажд пред является родительской для след
# os.remove('C:/Py/py pro/inout/data3.pkl')  # удаление документа
# os.rmdir('C:/Py/py pro/inout/')  # но программа не позволит удалить директорию, в которой хранятся другие объекты
# os.removedirs('C:/Py/tmp1/tmp2/tmp3') # удалить цепочку ПУСТЫХ директорий, кажд пред является родительской для след
# os.startfile(r"C:\Py\enumerate.txt")  # открыть файл, какой программой определяется автоматом
print(os.path.basename("C:/Py/py pro/inout/data.pkl"))  # получить только имя файла без пути
print(os.path.dirname("DC:/Py/py pro/inout/data.pkl"))  # получить только путь к файлу без имени
print(os.path.getsize("C:\\Py\\enumerate.txt"))  # получить размер в байтах (файла или папки)
# os.rename('C:/Py/py pro/inout/data3.pkl', 'C:/Py/py pro/inout/data2.pkl')  # переименовать файл
# os.renames('C:/Py/tmp1/tmp2/tmp3', 'C:/Py/tmp4/tmp5/tmp6')  # переименовать каскад папок
print(os.listdir('C:/Py/py pro/inout/'))  # возвращает список имен файлов и папок в указанном каталоге (без путей)

for root, directories, files in os.walk('C:/Py/py pro/inout/books'):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)
# доступ к названиям и путям всех подпапок и файлов, относящихся к заданному каталогу

print(os.stat('C:/Py/py pro/inout/'))  # основные сведения об объекте
print(os.path.split(r'C:\Py\enumerate.txt'))  # ('C:\\Py', 'enumerate.txt')
print(os.path.join('C:\\Py', 'enumerate.txt'))  # C:\Py\enumerate.txt
