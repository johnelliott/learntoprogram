import math
def bigeggs(eggs):
    if eggs % 12 == 0:
        return False
    else:
        return True

def smalleggs1(eggs):
    return not eggs % 12 == 0

def smalleggs2(eggs):
    return eggs % 12 != 0

def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'

def fruit_color(fruit):
    if fruit == 'apple':
        return 'red'
    elif fruit == 'banana':
        return 'yellow'
    elif fruit == 'pear':
        return 'green'

def grade_report(grade):
    if grade >= 80:
        return 'excellent'
    elif grade >= 50:
        return 'pass'
