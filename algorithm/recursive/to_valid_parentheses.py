"""
균형 잡힌 괄호 문자열 → 올바른 괄호 문자열로 변환
  입력 : 균형 잡힌(열고 닫는 괄호의 개수가 같은) 괄호 문자열 p
  출력 : 아래와 같이 변환한 문자열
    1. 입력이 빈 문자열인 경우, 빈 문자열을 반환
    2. 문자열을 두 "균형잡힌 괄호 문자열" u(가능한 최소 길이), v(빈 문자열 가능)로 분리
    3. 문자열 u가 "올바른 괄호 문자열" 이라면
      3-1. 문자열 v에 대해 1단계부터 수행한 결과를 u에 이어 붙인 후 반환
    4. 문자열 u가 "올바른 괄호 문자열"이 아니라면
      4-1. 빈 문자열에 첫 번째 문자로 '('를 붙이고
      4-2. 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 붙이고 ')'를 붙임
      4-3. u의 첫 번째와 마지막 문자 제거, 나머지의 괄호 방향을 바꿔 뒤에 붙여 반환
"""

def to_valid_parentheses(string):
    if string == "" :
        return ""

    idx = split(string)
    u = string[:idx]
    v = string[idx:]

    if check(u) :
        return u + to_valid_parentheses(v)
    else :
        return "(" + to_valid_parentheses(v) + ")" + "".join(["(" if p==")" else ")" for p in u[1:-1]])


def split(string):
    left=0
    right=0
    for i, char in enumerate(string):
        if char == "(":
            left += 1
        elif char == ")":
            right += 1
        if left==right :
            return i+1
    return


def check(string):
    stack = []
    for char in string:
        if char == "(":
            stack.append(char)
        else :
            if not stack:
                return False
            stack.pop()

    return stack == []



print(to_valid_parentheses( "(()())()"))
print(to_valid_parentheses("()))((()"))
print(to_valid_parentheses("))()(("))
print(to_valid_parentheses(")("))
