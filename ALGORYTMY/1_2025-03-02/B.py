# https://www.codewars.com/kata/59342039eb450e39970000a6

def odd_count(n):
    counter = 0
    for i in range(n):
        if i%2 != 0:
            counter += 1
    return counter;

odd_count(7)

# https://www.codewars.com/kata/57ab2d6072292dbf7c000039

def correct_polish_letters(st): 
    letters = {'ą':'a','ć':'c','ę':'e','ł':'l','ń':'n','ó':'o','ś':'s','ź':'z','ż':'z'}
    string = ""
    for i in st:
        if i in letters:
            string += letters[i]
        else:
            string += i
    return string

print(correct_polish_letters("Jędrzej Błądziński"))

# https://www.codewars.com/kata/57fb09ef2b5314a8a90001ed

def replace_exclamation(st):
    letters = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    string = ""
    for i in st:
        if i in letters:
            string += '!'
        else:
            string += i
    st = string
    return st

print(replace_exclamation("ABCDE"))

# https://www.codewars.com/kata/565f5825379664a26b00007c

def get_size(w,h,d):
    area = 2*w*h + 2*d*h + 2*w*d
    volume = w*h*d
    return [area, volume]

print(get_size(12.4, 44.5, 44.1))

# https://www.codewars.com/kata/59dd3ccdded72fc78b000b25

def whatday(num):
    days = { 1:"Sunday", 2:"Monday", 3:"Tuesday", 4:"Wednesday", 5:"Thursday", 6:"Friday", 7:"Saturday" }
    if num < 8:
        return days[num]
    else:
        return "Wrong, please enter a number between 1 and 7"

print(whatday(5))