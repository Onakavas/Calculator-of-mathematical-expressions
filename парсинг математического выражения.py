def replace_space(expression):
    tmp = '' 
    for i in range(len(expression)):
        if expression[i] != ' ':
            tmp+=expression[i]
    return tmp


def is_digit(a):
    if a <= '9' and a>='0':
        return True
    return False


def is_sign(b):
    if b == '+' or b=='-' or b=='*' or b=='/' or b =='^':
        return True
    return False


def count(expression):
    nmb = []
    sign = []
    buf = ''
    if expression[0] == '-':
        modif = -1
    else:
        modif = 1
    for i in range(int(abs(modif*0.5-0.5)), len(expression)): #формула 
        if is_digit(expression[i]) or expression[i] == '.':
            buf +=expression[i]
        elif is_sign(expression[i]):
            if expression[i] =='-' and is_sign(expression[i-1]):
                modif = -1
                continue
            sign.append(expression[i])
            #print(modif)
            nmb.append(float(buf)*modif)
            modif = 1
            buf = ''
        else:
            pass
    nmb.append(float(buf)*modif)
    buf = ''
    #print(sign,' ', nmb)
    x = len(sign)-1

    while x >= 0:
        if sign[x] =='^':
            nmb[x] = nmb[x]**nmb[x+1]
            nmb.pop(x+1)
            sign.pop(x)
        x-=1
    x = 0
    while x < len(sign):
        if sign[x] == '*':
            nmb[x] = nmb[x]*nmb[x+1]
            nmb.pop(x+1)
            sign.pop(x)
        elif sign[x] == '/':
            nmb[x] = nmb[x]//nmb[x+1]
            nmb.pop(x+1)
            sign.pop(x)
        else:
            x+=1

        
    for i in range(len(sign)):
        if sign[0] == '+':
            nmb[0] = nmb[0]+nmb[1]
            nmb.pop(1)
            sign.pop(0)
        elif sign[0] == '-':
            nmb[0] = nmb[0]-nmb[1]
            nmb.pop(1)
            sign.pop(0)
    return nmb[0]


def allcount(expression):
    expression = replace_space(expression)
    print(expression)
    max_brackets = 1
    while max_brackets != 0:
        brackets = 0
        max_brackets = 0
        index = ArithmeticError
        for i in range (0, len(expression)):
            if expression[i] == '(':
                brackets+=1
                if brackets > max_brackets:
                    max_brackets= brackets
                    index = i
            elif expression[i] ==')':
                brackets-=1
        if brackets != 0:
            print('Неправильное выражение')
            return None
        #print(max_brackets, ' max_brackets')
        i = index
        if max_brackets == 0:
            return count(expression)
        while expression[i] != ')':
            i+=1
        expression_in_brackets = expression[index+1:i]
        #print(expression_in_brackets)
        tmp = count(expression_in_brackets)
        expression_in_brackets = ''
        expression = expression[:index] + str(tmp) + expression[i+1:]
        


while True:
    print('Чтобы начать программу - напишите 1')
    print('Чтобы выйти - нажмите 2')
    choice = input()
    if choice == '1':
        expression = input('Введите выражение')
        result = allcount(expression)
        print(result)
    elif choice == '2':
        exit()
    

        
    
        





