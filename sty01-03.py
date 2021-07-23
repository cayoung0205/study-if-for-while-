## A 학급 인원 : 10 명 # 평균 구하기 (for)
## 중간고사 점수 : [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

hap = 0
Ascores = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
for score in Ascores :
    std = len(Ascores)
    hap = hap + score
print(hap/std)

