'''
Problem
입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자. (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)
※ 평균 값을 구할 때 len 함수를 사용해 보자.
len(s): 입력값 s의 길이개수를 돌려주는 함수
'''

'''------------------------------------- Functions'''

def Average(x):
    sum = 0
    for num in x:
        sum += int(num)
    result = sum / len(x)
    print("개수: %d" % len(x))
    print("합: %d" % sum)
    print("평균: %f" % result)

'''-------------------------------------'''

'''------------------------------------- Start'''

while True:
    a = []
    print("0 이상의 정수를 모두 입력하고 '='를 입력하면 평균을 출력합니다.")
    while True:
        n = input()
        if n == "=":
            if len(a) == 0:
                print("1개 이상의 정수를 입력해야 합니다.")
            else:
                Average(a)
                break
        elif n.isdigit() == 0:
            print("다시 입력하세요.")
        else:
            a.append(n)
    retry = input("다시 시도하려면 'y'를 입력하세요. 그 외의 키를 입력하면 종료합니다.\n")
    if retry == "y": continue
    else:
        print("프로그램을 종료합니다.")
        break
123

'''------------------------------------- End'''
