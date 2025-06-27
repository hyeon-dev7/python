
"""
숫자 변환 : 자연수 x를 y로 변환
 사용할 수 있는 연산 : x*2, x*3, x+n
 입력 : (x, y, n)
 출력 : 1. x를 y로 변환하기 위해 필요한 최소 연산 횟수, 만들 수 없다면 -1
       2. x에서 y로 변환되는 과정
"""

class ConvertNum :
    def __init__(self):
        self.x = None
        self.n = None
        self.memo = {}
        self.path = {}

    def convert(self, x, y, n):
        self.x = x
        self.n = n
        self.memo = {}
        self.path = {}
        return self._dfs(y), self._get_path(y)

    def _dfs(self, y):
        tmp = [] # 경로 저장용 임시 리스트
        if y < self.x :
            return -1
        elif y == self.x:
            return 0
        elif y in self.memo :
            return self.memo[y]
        else :
            mul_2 = self._dfs(y // 2) if y % 2 == 0 else -1
            # x 기준으로 생각해서 mul, add로 했는데 연산은 나누기.. 변수명 정하기 어렵다.
            mul_3 = self._dfs(y // 3) if y % 3 == 0 else -1
            add_n = self._dfs(y- self.n) if y - self.n >= self.x else -1

            tmp.append((1 + mul_2 if mul_2 != -1 else float('inf'), y // 2))
            tmp.append((1 + mul_3 if mul_3 != -1 else float('inf'), y // 3))
            tmp.append((1 + add_n if add_n != -1 else float('inf'), y - self.n))

            best, path = min(tmp, key=lambda x: x[0])
            self.memo[y] = best
            if best != float('inf'):
                self.path[y] = path

            return best if best != float('inf') else -1

    def _get_path(self, y):
        path = [y]
        while y in self.path:
            path.append(self.path[y])
            y = self.path[y]
        path.reverse()
        return path



conv = ConvertNum()
print( conv.convert(3,2,5) ) # -1
print( conv.convert(2,12,8) ) # 2
print( conv.convert(2,24,3) ) # 3
print( conv.convert(3,12,5) ) # 2
print( conv.convert(3,100,10) ) # -1
count, path = conv.convert(6, 38, 2)
print(count, path)

# print( conv.convert(1,1000000,1) ) # 19 - 재귀 오류, 숫자가 큰 경우에는 사용할 수 없다



"""
재귀 흐름 정리 
 입력 (2,12,8)
1. y=12 시작, mul_2 -> y=6, 재귀 2 -> y=3, mul_2 불가 -> mul_2=-1 
2. y=3 인 상태에서 아랫줄(재귀3) 실행 -> y=1 -> x > y 조건에 의해 -1 리턴, mul_3=-1
3. add_n 실행 불가 (3<8) -> add_n=-1
4. res 3개 다 float('inf') -> best, memo[3] => inf
5. return best -> y=6의 mul_2 = -1
7. mul_3 실행 -> y=2 -> x==y 0리턴 -> y=6의 mul_3=0
8. mul_n 실행 불가 -> -1
9. best =1, memo[6]=1
10. return best -> y=12의 mul_2= 1
11. mul_3 실행 -> y=4, mul_2 -> y=2 -> x==y return 0 -> y=2의 mul_2=0
12. y=2 mul_3, add_n 실행 불가 -> -1
13. y=2의 best=1, memo[2]=1
14. return best -> y=4의 mul_2=1
15. mul_3, add_n 실행 불가
16. y=4의 best=2, memo[4]=2
17. return best -> y=12의 mul_3=2
18. y=12의 add_n -> y=4 -> memo[4]에 의해 return 2
19. y=12의 add_n=2
20. y=12의 res 값 중 최소값=2 -> return 2, 종료
"""
