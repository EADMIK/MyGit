'''
DashInsert 함수는 숫자로 구성된 문자열을 입력받은 뒤 문자열 안에서 홀수가 연속되면 두 수 사이에 - 를 추가하고,
짝수가 연속되면 * 를 추가하는 기능을 갖고 있다. DashInsert 함수를 완성하시오.

입력 예시: 4546793
출력 예시: 454*67-9-3
'''

def DashInsert(x):
    i = 0
    form = []
    while i < len(x):
        form.append(x[i])
        if i == len(x) - 1:
            break
        if int(x[i]) % 2 == 1 and int(x[i+1]) % 2 == 1:
            form.append('-')
        if int(x[i]) % 2 == 0 and int(x[i+1]) % 2 == 0:
            form.append('*')
        i += 1
    print("".join(form))

data = list(input("숫자를 입력하세요: "))
DashInsert(data)