from django.shortcuts import render
import random

# Create your views here.


def calculate(request, number_1, number_2):

    num_sum = number_1 + number_2
    num_sub = number_1 - number_2
    num_mul = number_1 * number_2
    num_div = number_1 / number_2

    context = {
        "number1": number_1,
        "number2": number_2,
        "num_sum": num_sum,
        "num_sub": num_sub,
        "num_mul": num_mul,
        "num_div": num_div,
    }

    return render(request, "calculate.html", context)


def is_odd_even(request, number_1):

    if number_1 % 2 == 1:
        text_1 = "홀수"
    elif number_1 == 0:
        text_1 = "0"
    else:
        text_1 = "짝수"

    context = {
        "number": number_1,
        "text": text_1,
    }

    return render(request, "is_odd_even.html", context)


def name_input(request):

    return render(request, "name_input.html")


def past_result(request):

    peoples = [
        "고양이",
        "강아지",
        "거북이",
        "토끼",
        "뱀",
        "사자",
        "호랑이",
        "표범",
        "치타",
        "하이에나",
        "기린",
        "코끼리",
        "코뿔소",
        "하마",
        "악어",
        "펭귄",
        "부엉이",
        "올빼미",
        "곰",
        "돼지",
        "소",
        "닭",
        "독수리",
        "타조",
        "고릴라",
        "오랑우탄",
        "침팬지",
        "원숭이",
        "코알라",
        "캥거루",
        "고래",
        "상어",
        "칠면조",
        "직박구리",
        "쥐",
        "청설모",
        "메추라기",
        "앵무새",
        "삵",
        "스라소니",
        "판다",
        "오소리",
        "오리",
        "거위",
        "백조",
        "두루미",
        "고슴도치",
        "두더지",
        "우파루파",
        "맹꽁이",
        "너구리",
        "개구리",
        "두꺼비",
        "카멜레온",
        "이구아나",
        "노루",
        "제비",
        "까치",
        "고라니",
        "수달",
        "당나귀",
        "순록",
        "염소",
        "공작",
        "바다표범",
        "들소",
        "박쥐",
        "참새",
        "물개",
        "바다사자",
        "살모사",
        "구렁이",
        "얼룩말",
        "산양",
        "멧돼지",
        "카피바라",
        "도롱뇽",
        "북극곰",
        "퓨마",
        "",
        "미어캣",
        "코요테",
        "라마",
        "딱따구리",
        "기러기",
        "비둘기",
        "스컹크",
        "돌고래",
        "까마귀",
        "매",
        "낙타",
        "여우",
        "사슴",
        "늑대",
        "재규어",
        "알파카",
        "양",
        "다람쥐",
        "담비",
    ]
    people = random.choice(peoples)

    print(request)
    ball = request.GET.get("ball")
    context = {
        "name": ball,
        "people": people,
    }
    return render(request, "past_result.html", context)


def lorem_input(request):

    return render(request, "lorem_input.html")


def lorem_output(request):

    peoples = [
        "고양이",
        "강아지",
        "거북이",
        "토끼",
        "뱀",
        "사자",
        "호랑이",
        "표범",
        "치타",
        "하이에나",
        "기린",
        "코끼리",
        "코뿔소",
        "하마",
        "악어",
        "펭귄",
        "부엉이",
        "올빼미",
        "곰",
        "돼지",
        "소",
        "닭",
        "독수리",
        "타조",
        "고릴라",
        "오랑우탄",
        "침팬지",
        "원숭이",
        "코알라",
        "캥거루",
        "고래",
        "상어",
        "칠면조",
        "직박구리",
        "쥐",
        "청설모",
        "메추라기",
        "앵무새",
        "삵",
        "스라소니",
        "판다",
        "오소리",
        "오리",
        "거위",
        "백조",
        "두루미",
        "고슴도치",
        "두더지",
        "우파루파",
        "맹꽁이",
        "너구리",
        "개구리",
        "두꺼비",
        "카멜레온",
        "이구아나",
        "노루",
        "제비",
        "까치",
        "고라니",
        "수달",
        "당나귀",
        "순록",
        "염소",
        "공작",
        "바다표범",
        "들소",
        "박쥐",
        "참새",
        "물개",
        "바다사자",
        "살모사",
        "구렁이",
        "얼룩말",
        "산양",
        "멧돼지",
        "카피바라",
        "도롱뇽",
        "북극곰",
        "퓨마",
        "",
        "미어캣",
        "코요테",
        "라마",
        "딱따구리",
        "기러기",
        "비둘기",
        "스컹크",
        "돌고래",
        "까마귀",
        "매",
        "낙타",
        "여우",
        "사슴",
        "늑대",
        "재규어",
        "알파카",
        "양",
        "다람쥐",
        "담비",
    ]

    p = []
    ball1 = request.GET.get("ball_1")
    ball2 = request.GET.get("ball_2")
    people = random.choice(peoples)

    context = {
        "num1": ball1,
        "num2": ball2,
        "people": people,
    }

    return render(request, "lorem_output.html", context)
