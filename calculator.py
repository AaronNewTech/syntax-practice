def math_problem():

    print('Please enter a math problem in the format of number operator number')
    string = input()

    split = string.split(' ')
    # print(split[0])
    
    if len(split) > 3:
        print('Please enter a math problem with 2 numbers separated by an operator. i.e. 5 + 5') 
        math_problem()
    else:
        if split[1] == '+':
            result = int(split[0]) + int(split[2])
            print(result)
            return result
        elif split[1] == '-':
            result = int(split[0]) - int(split[2])
            print(result)
            return result
        elif split[1] == '*':
            result = int(split[0]) * int(split[2])
            print(result)
            return result
        elif split[1] == '/':
            result = int(split[0]) / int(split[2])
            print(result)
            return result

math_problem()