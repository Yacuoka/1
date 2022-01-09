#Задание 2
file_name = 'res_1.txt'
lst = ['первая строка\n', 'строка номер два\n', 'третья строка\n', '4 строка']

def get_line(lt):
    lt = list(map(str, lt))
    return ' '.join(lt)

with open(file_name, 'w') as f:
    f.write(get_line(lst))

with open(file_name, 'r') as f:
    file_lst = f.read().split('\n')
    file_lst = list(file_lst)
    print(file_lst)
    print(len(file_lst))

with open(file_name, 'r') as f:
    file_lst = f.read().split('\n')
    file_lst = list(file_lst)
    for i in range(len(file_lst)):
        print(file_lst[i],':')
        print(len(lst[i].split(' '), ), 'слова')
        print(len(file_lst[i]), 'символов')
print()


#Задание 1
text = 'Первый файл.'

with open('one.txt', 'w') as f:
    f.write(text)

text1 = 'Второй файл.'

with open('two.txt', 'w') as s:
    s.write(text1)


read_file = 'one.txt'
write_file = 'two.txt'
res_file = 'three.text'
with open(read_file, 'r') as fr, open(write_file, 'r') as fw, open(res_file, 'w') as fs:
    for line in fr:
        fs.write(line)
    for line2 in fw:
        fs.write(line2)

with open(res_file, 'r') as fs:
    for line in fs:
        print('Третий файл = ', line, end='')


