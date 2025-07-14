from collections import deque

"""
요세푸스 문제
1번부터 N 번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
K 번째 사람을 제거하고 남은 사람들로 이루어진 원을 따라 이 과정을 반복한다.
"""
def josephus(n, k):
    answer =[]
    dq = deque([i for i in range(1, n+1)])

    # collections.deque 로 queue (FIFO) 구현한 풀이
    count=1
    while dq :
        if count==k or len(dq)==1:
            answer.append(dq.popleft())
            count=1
            continue
        x = dq.popleft()
        dq.append(x)
        count+=1

    # deque rotate를 이용한 풀이
    # while dq :
    #     dq.rotate(-(k-1))
    #     answer.append( dq.popleft() )

    return "<"+ ", ".join(str(i) for i in answer)+ ">"

print(josephus(7, 3))
print(josephus(10, 7))