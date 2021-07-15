'''
사용자로부터 2~9의 숫자 중 하나를 입력받아 해당 숫자의 구구단을 한 줄로 출력하는 프로그램을 작성하시오.
실행 예)
구구단을 출력할 숫자를 입력하세요(2~9): 2
2 4 6 8 10 12 14 16 18
'''

def table(x):
    result = []
    multi = 1
    while multi <= 9:
        y = int(x) * multi
        result.append(str(y))
        multi += 1
    print(" ".join(result))

num = input("구구단을 출력할 숫자를 입력하세요: ")
table(num)