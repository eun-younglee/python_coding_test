# Q0002: Longest Common Prefix
# 📋 문제 설명
# 문자열 배열 strs가 주어집니다. 배열 내 모든 문자열의 가장 긴 공통 접두사(prefix)를 찾으세요.
# 공통 접두사가 없다면 빈 문자열 ""을 반환하세요.

# 입력
# strs: string[]    // 문자열 배열

# 출력
# string           // 가장 긴 공통 접두사

# 제약사항
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i]는 영문 소문자로만 이루어져 있습니다

# 💡 힌트
# 배열의 첫 번째 문자열을 기준으로 시작하세요
# 다른 문자열들과 비교하면서 공통 부분을 찾아나가세요
# 빈 문자열이 하나라도 있으면 공통 접두사는 빈 문자열입니다

def solve(strs):
  for i in range(len(strs[0]), 0, -1):
    base_word = strs[0][:i]
    flag = True;
    # print(base_word)

    for j in range(len(strs)):  
      if not strs[j].startswith(base_word):
        flag = False
        break;

    if flag == True: 
      return base_word

  return ""; 

print(solve(["flower", "flow", "flight"]))
print(solve(["dog", "racecar", "car"]))
print(solve(["interspecies", "interstellar", "interstate"]))
print(solve(["abc"]))