'''
다음은 딕셔너리의 a에서 'C'라는 key에 해당하는 value를 출력하는 프로그램이다.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'C'
a 딕셔너리에는 'C'라는 key가 없으므로 위와 같은 오류가 발생한다.
'C'에 해당하는 key 값이 없을 경우 오류 대신 70을 얻을 수 있도록 수정하시오.
'''

a = {'A':90, 'B':80}
try:
    a['C']
except KeyError as e:
    print("C에 해당하는 값이 없습니다. C에 70를 입력합니다.")
    a['C'] = 70
    print(a['C'])