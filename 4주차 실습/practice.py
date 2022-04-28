for i in range(5):
    for j in range(i+1):
        print('*', end='')
    print()

print()

for i in range(5):
    for j in range(4-i):
        print(' ', end='')
    for k in range(i+1):
        print('*', end='')
    print()

print()

for i in range(5):
    for j in range(4-i):
        print(' ', end='')
    for k in range((i)*2+1):
        print('*', end='')
    for l in range(4-i):
        print(' ', end='')
    print()

print()
for i in range(5):
    for j in range(i):
        print(' ', end='')
    for k in range((4-i)*2+1):
        print('*', end='')
    for l in range(i):
        print(' ', end='')
    print()