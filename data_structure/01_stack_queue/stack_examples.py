import stack as s

"""
괄호 유효성 검사 (Valid Parentheses) : () {} []
"""

def vp(string):
    stack = s.Stack()
    pairs = {')': '(', '}': '{', ']': '['}

    for i in string:
        if i in pairs.values():
            stack.push(i)
        elif i in pairs:
            if stack.is_empty() or stack.pop() != pairs[i]:
                return False

    return stack.is_empty()

print(vp( "(20-9)+[{30+(22-11)*7}-45]" )) # True
print(vp( "{30+(22-11)*7}-45]" )) # False
print(vp( "()[]{}" ))  # True
print(vp( ")()" ))     # False



""" 
가장 긴 유효 괄호 길이 검사
  입력 : 소괄호로만 이루어진 문자열 
  출력 : 유효한 괄호 구간 중 가장 긴 길이 반환, 아래 ''친 구간이 가장 긴 부분
        '(()()))' -> 6 , ))'()()') -> 4 , '()')('()' -> 2
"""

def lp(string):
    stack = s.Stack()
    max_len =0
    last = -1

    for i, v in enumerate(string):
        if v =="(":
            stack.push(i)
        else :
            if stack.is_empty():
                last = i
            else :
                stack.pop()
                max_len = max(max_len, i - (last if stack.is_empty() else stack.peek()) )

    return max_len

print("가장 긴 괄호 :", lp( "(()()" ), end=" ") # 4
print(lp( ")()())" ), end=" ") # 4
print(lp( "())(()" ), end=" ") # 2
print(lp( "" )) # 0
print(lp( "(()))(((()" )) # 0



"""
nearest smaller element
  입력 : 자연수로 이루어진 리스트 
  출력 : 각 원소에 대해 왼쪽 가장 가까이 위치한 '자신보다 작은 값'을 저장한 list
        왼쪽 값이 모두 기준 값보다 크다면 -1 
"""

def nse(lst):
    res = []
    stack = s.Stack()
    for i in lst:
        while stack and stack.peek() >= i:
            stack.pop()
        if stack.is_empty():
            res.append(-1)
        else:
            res.append(stack.peek())
        stack.push(i)
    return res

print(nse([4, 10, 6, 3, 12, 5, 12]))  # [-1, 4, 4, -1, 3, 3, 5]



"""
탑 신호 받기
  입력 : 리스트 heights (탑의 높이)
  출력 : 각 탑이 왼쪽으로 신호를 보낼 때 가장 먼저 수신할 수 있는-높거나 같은- 탑의 번호(index + 1)를 리스트로 반환
        왼쪽에 낮은 탑밖에 없다면 신호를 받을 수 있는 탑은 없다 (0)
        [6, 7, 5, 7, 4] -> [0, 0, 2, 2, 4]
"""

def top_signal(heights):
    stack = s.Stack()
    res =[]
    for i, v in enumerate(heights):
        while stack and heights[stack.peek()] < v:
            stack.pop()
        if stack.is_empty():
            res.append(0)
        else:
            res.append(stack.peek()+1)
        stack.push(i)
    return res

print("탑 신호 받기 :", top_signal([6, 3, 5, 6, 4]))
print("탑 신호 받기 :", top_signal([2, 9, 7, 6, 3, 5, 6, 4, 3, 6, 4]))



"""
next greater elements
  입력 : 자연수 리스트
  출력 : 각 원소에 대해 오른쪽 방향으로 가장 가까이 위치한 '자신보다 큰 값'을 담은 리스트
        첫번째 원소와 마지막 원소가 이어져 있다고(순환) 가정, 모든 값이 기준 값보다 작다면 -1
  예시 : 입력 [7, 3] → 출력 [-1, 7]
"""
def nge(nums):
    answer = [-1 for _ in range(len(nums)) ]
    stack = s.Stack()
    for i in range(len(nums)*2):
        idx = i % len(nums)
        while not stack.is_empty() and nums[stack.peek()] < nums[idx]:
            answer[stack.pop()] = nums[idx]
        stack.push(idx)
    return answer


print(nge([1,2,3,4,3])) #[2,3,4,-1,4]



"""
처음으로 작아지는 수
  입력 : 자연수 리스트
  출력 : 오른쪽 방향으로, 처음으로 자신보다 작은 수가 나왔을 때를 찾는다. 
        그 숫자와 자신과의 거리(몇 칸 떨어져 있는지)를 저장한다. 
        모든 수가 자신보다 크다면 마지막 원소와의 거리를 담은 '공백으로 구분된 문자열' 반환
  예시 : 입력 [5,4,3,2,3] → 출력 1 1 1 1 0
"""

def sol(lst):
    answer = [0] * len(lst)
    stack = s.Stack()

    for i in range(len(lst)):
        while not stack.is_empty() and lst[stack.peek()] > lst[i]:
            idx = stack.pop()
            answer[idx] = i-idx
        stack.push(i)

        if i == len(lst) - 1:
            while not stack.is_empty() :
                idx = stack.pop()
                answer[idx] = i-idx

    return ' '.join(map(str, answer))


print(sol([3, 5, 2, 7])) # 2 1 1 0
print(sol([5, 4, 4, 6, 3])) # 1 3 2 1 0
