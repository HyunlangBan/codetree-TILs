# 가장 근 시일내에 비가 오는 날
n = int(input())

min_date = "2111-11-11"
min_weather = ""
min_day= ""

for _ in range(n):
    date, day, weather = input().split()
    if weather == "Rain":
        # print(min_date)
        if min_date > date:
            min_date = date
            min_day = day
            min_weather = weather

print(min_date, min_day, min_weather)