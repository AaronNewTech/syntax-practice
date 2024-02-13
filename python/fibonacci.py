
def make_fibonacci():
    print("Enter a number for the length of the fibonacci sequence")
    length = int(input())
    num = 1
    result = []
    result.append(num)
    if length == 0:
        print("Enter a number for the length of the fibonacci sequence")
        make_fibonacci()
    elif length == 1 or length == 2:
        print('fibonaccit result:', num)
    else:
        for i in range(0, length -2):
            # print(i)
            num = result[i]
            result.append(result[i - 1] + num)

            
        print('fibonaccit result: ', result[-1])
            
            
make_fibonacci()
