
"""
피보나치 재귀 vs 반복문
  시간 복잡도
   - 메모 쓰는 재귀 / 반복문 : O(n)
   - 메모 안쓰는 재귀 : O(2^n)
  공간 복잡도
   - 반복문 O(1) .. 변수 2개 사용
   - 재귀 O(n)..재귀 콜 스택 (+ 값 저장용 메모리)
반복문이 더 효율적
"""

dic = {1: 1, 2: 1}
def fib(n): # 재귀 + 메모
    if not n in dic:
        dic[n] = fib(n-1) +fib(n-2)
    return dic[n]


def fib2(n): # 반복
    if n==1 or n==2:
        return 1
    a, b = 1, 1

    for _ in range(3, n+1):
        a, b = b, a+b
    return b


print(fib(5))
print(fib2(5))