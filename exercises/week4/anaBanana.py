s1='apple'
s2='p'

first = s1.find(s2)
second = s1.find(s2, s1.find(s2)+1)


print('first:', first, 'second:', second)


