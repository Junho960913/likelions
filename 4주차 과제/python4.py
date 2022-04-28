magic_dic = {}

while True:
    print('Enter a fruit type (q to quit): ', end='')
    type_ = input()
    if type_ == 'q':
        break
    print('Enter the weight in kg: ', end='')
    weight = input()
    magic_dic[type_] = weight

print(magic_dic)