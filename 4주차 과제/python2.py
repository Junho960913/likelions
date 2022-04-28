a = {}

a['이름'] = '장준호'
a['나이'] = '27살'
a['학번'] = '2017xxxxxx'
a['학과'] = '전기전자공학부'
a['생일'] = '19960913'

print(a)
print(len(a))
print()

del a['이름']
del a['나이']
del a['학번']
del a['학과']
del a['생일']

print(a)
print(len(a))
print()

a = dict(이름 = '장준호', 나이 = '27살', 학번 = '2017xxxxxx', 학과 = '전기전자공학부', 생일 = '19960913')

print(a)
print(len(a))
print()

a.clear()
print(a)
print(len(a))