## 1~ 1000까지 자연수 중 3의 배수의 합 (while)
## 함수
i = 1
hap = 0
while i <= 1000 :
    if i % 3 == 0 :
        hap = hap + i
    i = i + 1
print(hap)


## 전역

## 메인