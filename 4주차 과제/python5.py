import random
from time import sleep

print('5개의 메뉴를 추가해주세요! 5개가 입력되면 오늘의 메뉴를 추천해드려요')
print('동일한 메뉴는 안돼요!')
print()

menus = []
count = 0
while count < 5:
    menu = input('메뉴 추가: ')
    if menu in menus:
        del menus[menus.index(menu)]
        menus.append(menu)
        print('이미 있는 메뉴예요! 다른 메뉴를 입력해주세요')
    else:
        menus.append(menu)
        count += 1
    print(f'현재 메뉴 수 = {count}', end='\n\n')

for i in range(3,0,-1):
    print(i)
    sleep(1)

print()
print(menus)
print('과연 오늘의 메뉴는?', end='\n\n')

for i in range(3,0,-1):
    print(i)
    sleep(1)
print()

choose = random.choice(menus)
print(f'오늘의 메뉴는 {menus.index(choose)+1}번째 메뉴, {choose}입니다.')