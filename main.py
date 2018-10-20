class ChangeCalculator:

    def calculateSmallestChange(total):
        coins = [200, 100, 50, 20, 10, 5, 2, 1]
        remainder = total

        change = []
        while remainder > 0:
            for coin in coins:
                if remainder - coin >= 0:
                    remainder = remainder - coin
                    change.append(coin)
                    break

        return change