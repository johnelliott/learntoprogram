#Exercise 2 test sheet
import math

###1
##dollars=8


###2
##cents=34
##
##print(cents == 34 and cents < 20)
##print(not not cents >= 33)
##print(not cents * 2 > 34)
##print(cents < 8 or cents > 3)

###3
##dollars=18
##cents=53
##
##print((not dollars == 18) or cents == 53)
##print(not (dollars < cents and dollars > 0))
##print(not dollars < 10 and cents > 15)
##print(not dollars == 18 or not cents == 53)


###4
##'''
## 3 <= x < 10
## x is greater than or equal to three and less than 10
##'''
##x=-101
##print(3 <= x or x < 10 == 3 <= x < 10)
##print(3 <= x and x < 10 == 3 <= x < 10)
##print(not (3 <= x and x < 10) == 3 <= x < 10)
##print(x >= 3 and x > 10 == 3 <= x < 10)


###6
##if eggs % 12 == 0:
##    return False
##else:
##    return True

###7
##age1 = input("How old are you? ")
##age2 = input("How old is your best friend? ")
##
##print(age1 + age2)
##print(int(age1 + age2))
##print(int(age1) + int(age2))
##
##x = int(age1)
##y = int(age2)
##print(str(x + y))

###10
##def fruit_color(fruit):
##    if fruit == 'apple':
##        return 'red'
##    elif fruit == 'banana':
##        return 'yellow'
##    elif fruit == 'pear':
##        return 'green'
##
##print(fruit_color('apple'))
##
###11
##def fruit_color(fruit):
##    if fruit == 'apple':
##        return 'red'
##    elif fruit == 'banana':
##        return 'yellow'
##    elif fruit == 'pear':
##        return 'green'
##
##print(fruit_color('peach'))

#12
def weather_report(temp):
    if temp >= 20:
        return 'warm enough for ice cream'
    elif temp >= 0:
        return 'above freezing'
    
print(weather_report(20))
print(weather_report(10))
print(weather_report(-5))
print(weather_report(30))


#13


