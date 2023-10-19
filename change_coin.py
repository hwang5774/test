# !/usr/bin/env python
# coding:utf-8

"""이 모듈은 https://github.com/qiwsir/algorithm의 파이썬 프로젝트의 일부입니다.

문제:

인민폐의 동전을 예로 들어, 동전 수량이 충분합니다. 일정 금액의 돈을 동전으로 교환해야합니다. 동전 교환 수는 최소화해야합니다.

접근 방법:

이것은 탐욕 알고리즘의 전형적인 응용입니다. 이 예에서는 파이썬을 사용하여 구현하며, 주요 아이디어는 통화 금액을 일부 동전 단위로 나눈 다음 정수로 반올림하여 해당 동전의 수를 얻는 것입니다. 나머지는 다음 반복 계산의 통화 금액으로 사용됩니다.

이 알고리즘의 문제는 결과가 항상 최적이 아닐 수 있다는 것입니다. 예를 들어, 동전 단위가 [1,4,6]이고 8을 동전으로 교환해야하는 경우, 동전 수량을 최소화하는 원칙에 따라 두 개의 4(단위) 동전으로 교환해야하지만, 이 알고리즘에 따라 6 단위와 두 개의 1 단위 동전을 얻게됩니다. 이것은 이 알고리즘의 한계입니다. 탐욕 알고리즘은 결과를 찾기만 하면 된다는 것입니다.

"""

def change_coin(money):
    """주어진 금액을 동전으로 교환하는 함수입니다.

    Args:
        money (float): 교환할 금액

    Returns:
        dict: 교환된 동전의 수를 나타내는 딕셔너리

    """
    coin = [1, 2, 5, 10, 20, 50, 100]  # 1분, 2분, 5분, 1십원, 2십원, 5십원, 1원
    coin.sort(reverse=True)
    money = money * 100  # 센트 단위로 계산
    change = {}

    for one in coin:
        num_coin = money // one  # 나눗셈, 몫을 취하여 해당 동전의 수를 얻습니다.
        if num_coin > 0:
            change[one] = num_coin
        num_remain = money % one  # 나머지를 얻어 남은 금액을 계산합니다.
        if num_remain == 0:
            break
        else:
            money = num_remain
    return change


# 아래의 방법은 동적으로 최소 동전 수를 제공합니다. 탐욕 방법의 문제를 피할 수 있습니다.
def coinChange(centsNeeded, coinValues):
    minCoins = [[0 for j in range(centsNeeded + 1)] for i in range(len(coinValues))]
    minCoins[0] = range(centsNeeded + 1)

    for i in range(1, len(coinValues)):
        for j in range(0, centsNeeded + 1):
            if j < coinValues[i]:
                minCoins[i][j] = minCoins[i - 1][j]
            else:
                minCoins[i][j] = min(minCoins[i - 1][j], 1 + minCoins[i][j - coinValues[i]])
    return minCoins[-1][-1]


if __name__ == "__main__":
    money = 3.42
    coin = [1, 2, 5, 10, 20, 50, 100]  # 1분, 2분, 5분, 1십원, 2십원, 5십원, 1원
    num_coin = change_coin(money)
    result = [(key, num_coin[key]) for key in sorted(num_coin.keys())]
    print("You have %s RMB" % money)
    print("I had to change you:")
    print("    Coin    Number")
    for i in result:
        if i[0] == 100:
            print("Yuan    %d    %d" % (i[0] / 100, i[1]))
        elif i[0] < 10:
            print("Fen    %d    %d" % (i[0], i[1]))
        else:
            print("Jiao    %d    %d" % (i[0] / 10, i[1]))
    num2 = coinChange(5, coin)
    print(num2)
# 실행 결과
# You have 3.42 RMB
# I had to change you:
#    Coin    Number
#    Fen    2    1
#    Jiao    2    2
#    Yuan    1    3

