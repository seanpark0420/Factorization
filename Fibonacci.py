a = 1
b = 1 #피보나치 초기값의 정의
while True:
    if a>100: # a가 100을 넘으면 거기까지 출력하고 종료한다
        break
    print(a,b,b/a) #b/a값이 황금비에 가까워지는 것을 표현
    a = a + b #피보나치 수열의 규칙을 표현
    b = b + a #위 코드와 마찬가지
    if a>100: # a가 
        break