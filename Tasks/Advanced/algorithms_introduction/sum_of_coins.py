def sum_coins(coins, target):
    coins.sort(reverse=True)
    count_per_coin = {}
    index = 0

    while target > 0 and index < len(coins):
        count_coins = target // coins[index]
        target %= coins[index]
        if count_coins > 0:
            count_per_coin[coins[index]] = count_coins
        index += 1

    if target != 0:
        return "Error"

    result = f"Number of coins to take: {sum(count_per_coin.values())}\n"
    for value, count in count_per_coin.items():
        result += f"{count} coin(s) with value {value}\n"

    return result.strip()


coin_list = [int(x) for x in input().split(", ")]
target_num = int(input())
print(sum_coins(coin_list, target_num))
