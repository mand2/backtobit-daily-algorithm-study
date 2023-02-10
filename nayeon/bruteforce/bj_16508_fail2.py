import sys;inp = sys.stdin.readline

t = inp().rstrip()
n = int(inp().rstrip())
book = [list(inp().rstrip().split()) for _ in range(n)]

# 단어가 알파벳 몇개씩 할당되었는지 체크
dic = [0] * 26
for word in t:
    dic[ord(word) - 65] += 1  # ord('A') = 65

price_list=[]
for i in range(1 << len(book)):  # 1개 ~ n개 뽑을 때의 각조합의 총 개수는 비트연산으로 쌉가능.. 와우내
    # 망할 무한루프 돔. flag 없으면 0만 나옴;
    mix_word, mix_price, flag = '', 0, 1
    while flag:
        for j in range(len(book)):
            # 이제 실제 조합을 해준다
            if i & (1 << j):
                mix_word += book[j][1]  # 조합에 들어갈 모든 문자열을 다 더해준다.
                mix_price += int(book[j][0])  # 조합에 들어갈 전공책 값을 다 더해준다.
        for w in t:
            if mix_word.count(w) < dic[ord(w) - 65]:  # break/continue 가 안먹혀서 flag로 대체
                # print('1', mix_price, mix_word)
                flag=0
        # print('2', mix_price, mix_word)
        price_list.append(mix_price)

print(-1) if len(price_list)==0 else print(min(price_list))

