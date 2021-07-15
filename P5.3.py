'''
Problem
다음과 같이 실행할 때 입력값을 모두 더하여 출력하는 스크립트(C:\doit\myargv.py)를 작성해 보자.

C:\> cd doit
C:\doit> python P5.3.py 1 2 3 4 5 6 7 8 9 10
55
※ 외장 함수 sys.argv를 사용해 보자.
'''

'''------------------------------------- Functions'''



'''-------------------------------------'''

'''------------------------------------- Start'''

import sys
print(sys.argv)
del sys.argv[0]
for i in sys.argv:
    sum += i
print(sum)

'''------------------------------------- End'''
