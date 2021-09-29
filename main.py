import csv


# Функция 1
def option1(count, d):
    """Функция принимает пустой словарь и счетчик, затем считаывает все строки из файла и выводит словарь с
    департаментами и отделами в нем """
    with open("Corp Summary.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        # Функция 1
        for row in file_reader:
            if count == 0:
                pass
            else:
                if row[1] not in d:
                    d[row[1]] = list()
                    d[row[1]].append(row[2])
                else:
                    if row[2] in [x for v in d.values() for x in v]:
                        pass
                    else:
                        d[row[1]].append(row[2])
            count += 1
            
        for key, value in d.items():
            print("{0}: {1}".format(key, value))


# Функция 2
def option2(count, workers_num, s):
    """ Функция принимает пустой словарь и два счетчика, затем считывает все строки из файла и выводит словарь с
    каждым из департаментов и статистику по нему """
    with open("Corp Summary.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        # Функция 1
        for row in file_reader:
            if count == 0:
                pass
            else:
                if row[1] not in s:
                    s[row[1]] = list()
                    s[row[1]].append(workers_num + 1)
                    s[row[1]].append(row[5])
                    s[row[1]].append(row[5])
                    s[row[1]].append(int(row[5]))
                    s[row[1]].append(0)
                else:
                    (s.get(row[1]))[0] += 1
                    (s.get(row[1]))[3] += int(row[5])
                    (s.get(row[1]))[4] = round((s.get(row[1]))[3] / (s.get(row[1]))[0])
                    if int(row[5]) > int((s.get(row[1]))[1]):
                        (s.get(row[1]))[1] = int(row[5])
                    if int(row[5]) < int((s.get(row[1]))[2]):
                        (s.get(row[1]))[2] = int(row[5])
            count += 1

        for v in s.values():
            del (v[3])

    for key, value in s.items():
        print(f"{key} – Численность: {value[0]}; Макс зарплата: {value[1]}; Мин зарпалата: {value[2]}; "
              f"Средняя зп: {value[3]}")


# Функция 3
def option3(count, workers_num, k):
    """Функция принимает пустой словарь и счетчик, затем считаывает все строки из файла, собирает словарь со
    статистикой по отделам и записывает ее в csv файл """
    with open("Corp Summary.csv", encoding='utf-8') as r_file:
        file_reader = csv.reader(r_file, delimiter=";")
        for row in file_reader:
            if count == 0:
                pass
            else:
                if row[1] not in k:
                    k[row[1]] = list()
                    k[row[1]].append(workers_num + 1)
                    k[row[1]].append(row[5])
                    k[row[1]].append(row[5])
                    k[row[1]].append(int(row[5]))
                    k[row[1]].append(0)
                else:
                    (k.get(row[1]))[0] += 1
                    (k.get(row[1]))[3] += int(row[5])
                    (k.get(row[1]))[4] = round((k.get(row[1]))[3] / (k.get(row[1]))[0])
                    if int(row[5]) > int((k.get(row[1]))[1]):
                        (k.get(row[1]))[1] = int(row[5])
                    if int(row[5]) < int((k.get(row[1]))[2]):
                        (k.get(row[1]))[2] = int(row[5])
            count += 1

        for v in k.values():
            del (v[3])

    with open('final.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['Департамент', 'Численность', 'Макс зарплата', 'Мин зарплата', 'Средняя зп'])
        [f.write('{0},{1},{2},{3},{4}\n'.format(key, value[0], value[1], value[2], value[3])) for key, value in k.items()]
    print ('csv файл сохранен')


opt = input('Введите ваш выбор цифрой: ')
if opt == '1':
    option1(0, {})
elif opt == '2':
    option2(0, 0, {})
elif opt == '3':
    option3(0, 0, {})
else:
    print('Такого варианта нет:(')
