# 4의 배수: 윤년
# 4의 배수 and 100의 배수: 윤년 아님
# 4의 배수 and 100의 배수 and 400의 배수: 윤년
# 나머지: 윤년 아님

y, m, d = map(int, input().split())

# 1월: 31
# 2월: 윤년 따짐
# 3월: 31
# 4월: 30
# 1, 3, 5, 7, 8, 10, 12: 31
thirty_one = [1, 3, 5, 7, 8, 10, 12]
# 4, 6, 9, 11
thirty = [4, 6, 9, 11]
# 짝수월: 2월 확인


def get_season(m):
    if m // 3 == 1:
        return "Spring"
    elif m // 3 == 2:
        return "Summer"
    elif m // 3 == 3:
        return "Fall"
    elif m // 3 == 0 or m // 3 == 4:
        return "Winter"

def func(y, m, d):
    season = -1
    if m in thirty_one:
        if d <= 31:
            season = get_season(m)
        # else:
        #     print(-1)
    else:
        if y % 4 == 0:
            if y % 100 == 0:
                if y % 400 == 0:
                    if d <= 29:
                        season = get_season(m)
                    # else:
                    #     print(-1)
                else:
                    if d <= 28:
                        season = get_season(m)
                    # else:
                    #     print(-1)
            else:
                if d <= 29:
                    season = get_season(m)
                # else:
                #     print(-1)
        else:
            if d <= 28:
                season = get_season(m)
            # else:
            #     print(-1)
    print(season)

func(y, m, d)