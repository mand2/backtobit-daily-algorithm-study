num = list(map(int, input().split()))
a = filter(lambda x: x % 2 == 0, num)
print(*a, sep='\n')



"""
6065 : [기초-조건/선택실행구조] 정수 3개 입력받아 짝수만 출력하기(설명)
3개의 정수(a, b, c)가 입력되었을 때, 짝수만 출력해보자.


예시
a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

if a%2==0 :  #논리적으로 한 단위로 처리해야하는 경우 콜론(:)을 찍고, 들여쓰기로 작성 한다.
  print(a)

if b%2==0 :
  print(b) 

if c%2==0 :
  print(c) 

참고 
if 조건식 :
  실행1  #조건식의 평가값이 True 인 경우 실행시킬 명령을 들여쓰기를 이용해 순서대로 작성한다.
  실행2
실행3  #들여쓰기를 하지 않은 부분은 조건식에 상관이 없음 

python 에서는 논리적 실행단위인 코드블록(code block)을 표현하기 위해 들여쓰기를 사용한다.
들여쓰기 방법은 탭(tab), 공백(space) 4개 등 여러 가지 방법을 사용할 수 있지만
한 소스코드 내에서 들여쓰기 길이와 방법은 똑같아야 한다.

a%2==0 은 (a%2)가 먼저 계산된 후 그 결과를 정수 0과 비교한 결과값이다.
a를 2로 나눈 나머지가 0, 즉 짝수이면 True 가 되고, 아니면 False 로 계산된다.
따라서,
if a%2==0 : #a가 짝수라면 ... 
와 같은 의미가 된다. 짝수가 아니라면 들여쓰기로 작성된 부분들은 실행되지 않는다.
"""
