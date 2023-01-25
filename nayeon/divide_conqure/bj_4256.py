tc = int(input())

def matching(root, start, end):
    for i in range(start, end):
        if inorder[i] == preorder[root]:
            matching(root + 1, start, i)  # left subtree
            matching(root + i + 1 - start, i + 1, end)  # right subtree
            print(preorder[root], end=" ")


for _ in range(tc):
    n = int(input())
    # preorder = [map(int, input().split())]
    # inorder = [map(int, input().split())]
    preorder = list(map(int, input().split()))
    inorder = list(map(int, input().split()))
    matching(0, 0, n)
    print()  # 없으면 출력형식 오류로 실패.


"""
리프노드 (루트노드가 유일한 이진트리일 경우, 나머지 노드는 모두 자식이 없)


        3
    6       7
  5   4   1
     8     2 
예를 들어, 위의 그림을 
    전위 순회하면 3,6,5,4,8,7,1,2 
    중위 순회하면 5,6,8,4,3,1,2,7  
    후위 순회하면 5,8,4,6,2,1,7,3  
=> () 루트 / [] left / 그냥 right
    전위 순회 (3),[6,5,4,8],7,1,2 
    중위 순회 [5,6,8,4],(3),1,2,7  
    후위 순회 [5,8,4,6],2,1,7,(3)  

=> [6,5,4,8] 만 따로 본다면   
        (6),[5],4,8
        [5],(6),8,4
        [5],8,4,(6)
    
    
2
4
3 2 1 4
2 3 4 1
8
3 6 5 4 8 7 1 2
5 6 8 4 3 1 2 7
=>
2 4 1 3
5 8 4 6 2 1 7 3
"""
