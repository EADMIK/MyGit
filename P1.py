'''
다음과 같은 문자열이 있다.

a:b:c:d

문자열의 split와 join 함수를 사용하여 위 문자열을 다음과 같이 고치시오.

a#b#c#d
'''

print("#".join(("a:b:c:d").split(':')))