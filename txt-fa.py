while True:
    file_name = str(input('Введите название файла: '))
    file = open(f'your_files/{file_name}.txt', 'w')
    file.close()
    file = open(f'your_files/{file_name}.txt', 'a')
    str_count = int(input('введите количество строк которые вы хотите прописать: '))
    for i in range(str_count):
        txt = ('Введите строку #' + str(i + 1) + ': ')
        file.write(input(txt))
        file.write('\n')
    file.close()    


    txt2 = ('хотите создать еще файл?' + '\n' + '\t' + 'Y or N' + '\n')
    user_choice = str(input(txt2))
    if user_choice == 'y':
        True
    elif user_choice == 'n':
        False
        print('спасибо за использование :3')    
       


