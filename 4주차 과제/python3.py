words = []

while True:
    print('Enter anything: ', end='')
    a = input()
    if a == 'q':
        break
    words.append(a)

print(words)