# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к
# уже подсчитанной сумме. Но если вместо числа вводится специальный символ, выполнение программы
# завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.

def sum_func(str_list,int_list):
    for el in str_list:
        int_list.append(int(el))
    return sum(int_list)

int_list = []
while True:
    user_var = input('Вводите числа через пробел и нажмите ENTER для ввода\n'
                     'Для выхода введите Q: ').lower()
    user_list = user_var.split()
    if 'q' in user_list:
        user_list.remove('q')
        print(sum_func(user_list, int_list))
        break
    else:
        print(sum_func(user_list, int_list))

