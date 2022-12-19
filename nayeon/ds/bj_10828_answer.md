# [문제번호] 문제 제목

## 1. 적용 알고리즘 간단 설명
- 큐(queue)를 만들어서 넣어준다. 혹은 스택(list)로 해서 체크해도 된다.

## 2. 접근방식
1. 입력받은 값을 명령어 구문으로 나눠서 처리

## 3. 답안 코드

## 4. 답안 코드에 대한 설명
- 시간 복잡도 : O(n)
- 공간 복잡도 : O(1)
- 사용 라이브러리 : deque, stdin
- 코드 설명 

## 5. 코드 리뷰 후, 개선한 코드에 대한 설명


## 6. 기타
- sysout.write()로 썼다가 엔터를 치지 않아서 계속 '틀렸습니다!'가 떴다 주의해야 함.
- deque 에서는 제일 위에 있는 스택 보여주기만 (pop 이 아닌) 하는 기능이 없어서 조금 더러워 졌다.
- 문제에 나와있지 않은 명령어를 쓰지 않는다고 하여 마지막 명령어 else로 처리. 


----
### 문제
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령은 총 다섯 가지이다.

push X: 정수 X를 스택에 넣는 연산이다.
pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.


### 입력
첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

### 출력
출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

**예제입력 1**
```
14
push 1
push 2
top
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
top
```

**예제출력 1**
```
2
2
0
2
1
-1
0
1
-1
0
3
```