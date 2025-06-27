
count = 0
def hanoi(n, start, mid, end):
    global count
    count += 1

    if n == 1:
        move(start, end)
    else :
        hanoi(n-1, start, end, mid)
        move(start, end)
        hanoi(n-1, mid, start, end)
    return count

def move(from_, to):
    print(from_, "->", to)

print(hanoi(3,"A","B","C"))

"""
n=3 일 때
    하노이 호출 - else 앞재귀(n=2) - else 앞(n=1)
                                       move
                                       뒤 (n=1)

                else의 move

                else의 뒤재귀(n=2) - else 앞(n=1)
                                        move
                                        뒤 (n=1)

    위 3줄이 2개 내리는, else의 move가 가장 아래 원판 옮기는, 아래 3줄은 2개 올리는 경우

앞/뒤재귀에 한번 들어가면 그 재귀의 else문 앞,뒤에서 전부 n=1이 될 때까지 돌고 빠져나온다.
(n=1이 될 때까지 앞재귀 -> move  -> n=1이 될 때까지 뒤재귀 순서)
"""