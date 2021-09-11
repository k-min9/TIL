def solution(n, k):
     def convert(num, base):	
          multi = 1
          result = 0          
          while 0 < num:
               result += num % base * multi
               multi *= 10
               num = num // base
               
          return str(result)
     
     
     # 소수 체크
     def is_prime(num):
          if num == 1:
               return False
          for i in range(2, int(num**0.5) + 1):
               if num % i == 0:
                    return False
          return True

     # 진수 바꾸기
     words = convert(n, k)

     # split 기준 잡고, split
     while '00' in words:
          words = words.replace('00', '0')
     words = words.rstrip('0')
     answers = words.split('0')

     # 소수 체크 및 계산
     cnt = 0
     if answers:
          for answer in answers:
               if is_prime(int(answer)):
                    cnt+=1
          return cnt
     else:
          return 0

# print(solution(437674, 3)) # 3
# print(solution(110011, 10)) # 2

print(solution(3,3))