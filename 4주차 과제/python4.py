magic_dic = {}

while True:
    type_ = input('Enter a fruit type (q to quit): ')
    if type_ == 'q':
        break
    weight = input('Enter the weight in kg: ')
    magic_dic[type_] = weight

print(magic_dic)