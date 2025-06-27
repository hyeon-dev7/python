
"""
부분 집합
 백트래킹(backtracking) 알고리즘
  가능한 해를 구성하면서 조건을 만족하지 않는 경우 그 해를 포기하고 이전 단계로 돌아가는 방식
  종료 조건, 재귀 호출을 활용 -> 시간 복잡도 큰 편
  부분 집합 문제의 경우 각 원소마다 두가지 선택 -> O(2^n)
  부분 집합, 조합, 순열 등에 사용
"""


def subset(lst):
    res = []

    def backtrack(start, sub):

        if start == len(lst):
            res.append(sub[:])
            return

        backtrack(start + 1, sub) # b1
        sub.append(lst[start])
        backtrack(start + 1, sub) # b2
        sub.pop()

    backtrack(0, [])
    return res


print(subset([1, 2]))
print(subset([3, 2, 3]))

"""
 부분 집합 
1. subset 함수 호출, 그 안에서 backtrack 호출
2. b1에 의해 [] -> start=1 [] -> start=2 [] -> 저장 후 return(start=1 으로) 
3. start=1 b1 아래부터 실행 : append(2) -> b2에 의해 [2] 저장 후 return,
   pop() -> sub=[], backtrack 함수 다 돌았으니 상위 호출인 start=0으로 돌아옴 
4. start=0인 상태에서 b1 아래부터 실행 (sub.append(1))
5. b2에 의해 재귀 start=1, sub = [1]
6. b1에 의해 start=2, [1] 저장 후 return
7. append -> [1,2], b2에 의해 start=2 -> 저장 후 리턴
8. start=1 -> pop (sub=[1]), 함수 다 돌았으니 b2 start=0으로 return
9. pop -> sub=[], 모든 처리 끝 -> backtrack 함수 종료, subset 함수 종료(return res)
"""



# 아래 방법은 조합에, 위와 같은 이진 분기 방식은 부분 집합에 더 어울린다고 한다.
# 실행 결과 보면 집합 만들어지는 순서가 달라서 참고 용으로 남겨 놓음
def subsets(nums):
    result = []

    def backtrack(start, sub):
        result.append(sub[:])  # 현재까지 만든 부분 집합 저장

        for i in range(start, len(nums)):
            sub.append(nums[i])         # 원소 선택
            backtrack(i + 1, sub)       # 다음 단계로 진행
            sub.pop()                   # 백트래킹 (선택 취소)

    backtrack(0, [])
    return result

print(subsets([1, 2, 3]))



"""
  Backtracking - 조합(combination) 
  조합 : 서로 다른 n개의 원소를 가지는 집합에서 '순서 상관 없이' r개의 원소 선택


def combination(nums, r):
    def backtrack(start, comb):
        if len(comb) == r:
            result.append(comb[:])
            return
        for i in range(start, len(nums)):
            comb.append(nums[i])
            backtrack(i+1, comb)
            comb.pop()

    result = []
    backtrack(0, [])
    return result

print(combination([1, 2, 3], 2))


1. for 문에서 comb에 [1]
2. start+1하고 [1]을 넘겨서 nums[1]인 2를 append -> 이제 comb는 [1 , 2]
3. 다시 백트랙 재귀하는데 r=2라서 rex에 [1,2] 저장 ([:] 슬라이싱, 리스트 전체 복사)
4. return 반환값 없이 다시 backtrack 자리에 와서 다음줄 실행 (2를 pop -> [1])
5. 지금까지 i=0이었으니 (재귀 안의 i는 각 함수 호출의 지역변수라서 서로 영향을 주지 않음) 
   이제 i=1로 comb.append(2)
6. 재귀 i=2, append(3) -> [2,3]
7. 재귀 i=3 -> len()=r -> 저장, return
8. pop -> (2)
9. i=2 -> for문 조건에 걸려서 빠져 나옴, 리턴
"""

"""
동전 거스름돈 (중복 조합)
 입력 : 거스름돈, 동전 종류
 출력 : 최소 동전 개수(모든 동전은 충분히 있다), 사용한 동전 리스트


def coin_change(money, coin_lst):
    best = [float("inf")]
    choice = []
    used_coins = []
    coin_lst.sort(reverse=True)

    def dfs(money, start):
        if money < 0 or best[0] <= len(choice):
            return

        elif money == 0 :
            if len(choice) < best[0]:
                best[0] = len(choice)
                used_coins.clear()
                used_coins.append(choice[:])
            return

        for i in range(start, len(coin_lst)):
            choice.append(coin_lst[i])
            dfs(money - coin_lst[i], i)
            choice.pop()

    dfs(money, 0)
    return best[0] if best[0] != float("inf") else -1, used_coins

# coin_list = [10, 50, 100, 400, 500]
# money = 800
coin_list = [10, 540, 500, 900]
money = 2740
print(coin_change(money, coin_list))
print(coin_change(3, [2])) # 불가능 , -1
"""