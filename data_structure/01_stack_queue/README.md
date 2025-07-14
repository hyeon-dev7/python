# 📁 01_stack_queue
자료 구조 **스택(Stack)**, **큐(Queue)** 구현 및 예제 모음입니다.
```
01_stack_queue/ 
├── stack.py              # 스택 클래스 구현 
├── stack_examples.py     # 스택 활용 예제 6가지 
├── stack_class.py        # MinStack 및 스택 기반 큐 클래스 
├── queue_josephus.py     # 큐를 활용한 요세푸스 문제 풀이 
└── circular_queue.py     # 원형 큐 구현 (덮어쓰기 가능, 불가 2종) 
``` 
---

## 📄 `stack_example.py` : 스택을 활용한 예제 6가지

<table>
  <thead>
    <tr>
      <th>분류</th>
      <th>문제 이름</th>
      <th>설명</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td rowspan="2">괄호 처리</td>
      <td>올바른 괄호 판별</td>
      <td> () {} [] 형태가 올바른지 확인</td>
    </tr>
    <tr>
      <td>가장 긴 유효 괄호 길이</td>
      <td>괄호 문자열 중 가장 긴 유효 구간 길이 계산</td>
    </tr>
    <tr>
      <td rowspan="2">단조 스택 <br> (왼쪽에서 찾기)</td>
      <td>Nearest Smaller Element</td>
      <td>왼쪽에서 가장 가까운 작은 수 찾기</td>
    </tr>
    <tr>
      <td>탑 신호 받기</td>
      <td>왼쪽에서 수신 가능한 높은 탑 번호 찾기</td>
    </tr>
    <tr>
      <td rowspan="2">단조 스택 <br> (오른쪽에서 찾기)</td>
      <td>Next Greater Element (순환)</td>
      <td>오른쪽(순환)에서 가장 가까운 큰 수 찾기</td>
    </tr>
    <tr>
      <td>처음으로 작아지는 수</td>
      <td>오른쪽에서 처음으로 작아지는 값과의 거리 계산</td>
    </tr>
  </tbody>
</table>
   
<br>

### 단조 스택(Monotonic Stack)이란?

원소들이 오름차순 또는 내림차순으로 정렬된 상태를 유지하도록 구성한 스택 자료구조입니다. <br>
주로 왼쪽 또는 오른쪽으로 **단방향 탐색**을 하면서 기준 원소보다 **작거나 큰 값을 빠르게 찾는 문제**에 사용합니다.<br>
<br>
각 원소는 스택에 한 번만 push, 한 번만 pop 되기 때문에, 시간복잡도는 일반적으로 **O(n)** 입니다.

---

### 참고 문제 및 출처
- `가장 긴 유효 괄호 길이` → [LeetCode #32 “Longest Valid Parentheses”](https://leetcode.com/problems/longest-valid-parentheses/description/?utm_source=chatgpt.com)
- `단조 스택 (왼쪽)` → [백준 2493 “탑”](https://www.acmicpc.net/problem/2493)
- `단조 스택 (오른쪽)` → [LeetCode #503 “Next Greater Element II”](https://leetcode.com/problems/next-greater-element-ii/submissions/?utm_source=chatgpt.com)  
- `요세푸스` → [백준 1158 "요세푸스 문제"](https://www.acmicpc.net/problem/1158)

