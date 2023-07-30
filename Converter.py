nums = "XC"
list = [*nums]
numeral = 0
for i, letter in enumerate(list):
    print(letter)
    if letter == 'I':
        try: 
            if(list[i+1] == 'V' or list[i+1] == 'X'):
                numeral -= 1
            else: 
                numeral += 1
            continue
        except: 
            numeral += 1
            continue
    elif letter == 'V':
        numeral += 5
        continue
    elif letter == 'X':
        try:
            if(list[i+1] == 'L' or list[i+1] == 'C'):
                numeral -= 10
            else: 
                numeral += 10
            continue
        except: 
            numeral += 10
            continue
    elif letter == 'L':
        numeral += 50
    elif letter == 'C':
        try: 
            if(list[i+1] == 'D' or list[i+1] == 'M'):
                numeral -= 100
            else: 
                numeral += 100
            continue
        except: 
            numeral += 100
            continue
    elif letter == 'D':
        numeral += 500
        continue
    elif letter == 'M':
        numeral += 1000
        continue
    else:
        break
print(numeral)