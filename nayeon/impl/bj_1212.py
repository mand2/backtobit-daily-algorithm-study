print(format(int(input(), 8), 'b'))

"""
8진수가 주어졌을 때, 2진수로 변환하는 프로그램을 작성하시오.
주어지는 수의 길이는 333,334을 넘지 않는다.

314
    11001100
    
X 진수 -> 10진수 변환
    int(number, 2) # 2진수->10진수 변환
    int(number, 8) # 8진수->10진수 변환
    int(number, 16) # 16진수->10진수 변환

10진수-> X 진수 변환
    1. 내장 => 앞에 2자리에 진수관련 문자열(접두어)이 붙음. 
        bin(), oct(), hex() 
    2. format (1의 단점을 해결)
        format(number, 'b')  # 2진수
        format(number, 'o')  # 8진수
        format(number, 'x')  # 16진수
        format(number, 'X')  # 16진수 대문자
        format(number, 'd')  # 10진수
        
        #b, #o, #x, #X 가능 (접두어 추가)
"""
