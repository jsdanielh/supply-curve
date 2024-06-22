import matplotlib.pyplot as plt
import math
from datetime import timedelta


def pow_supply():
    start_year = 2018
    circulating_supply = 2520000000
    circulating_supply_year = []
    for i in range(start_year, 2048):
        if i == start_year:
            circulating_supply_year.append(circulating_supply)
        else:
            for j in range(525600):
                block_reward = (
                    21000000000 - circulating_supply) / math.pow(2, 22)
                circulating_supply += block_reward
            circulating_supply_year.append(circulating_supply)
    return circulating_supply_year


def pos_supply():
    genesis_supply = 2520000000.0
    supply_decay = 4.792821935e-12
    start_year = 2018
    circulating_supply_year = []
    year_ms = timedelta(days=365).total_seconds() * 1000
    for i in range(start_year, 2048):
        exponent = -supply_decay * (i-start_year) * float(year_ms)
        print(1.0 - math.exp(exponent))
        supply = genesis_supply + \
            (0.0875 / supply_decay * (1.0 - math.exp(exponent)))
        # print(supply)
        circulating_supply_year.append(supply)
    return circulating_supply_year


def main():
    pow_values = pow_supply()
    # for i, _val in enumerate(pow_values):
    #    if i == 0:
    #        continue
    #    diff = (pow_values[i] - pow_values[i-1])/pow_values[i-1] * 100
    #    print(diff)

    plt.plot(range(2018, 2048), pow_supply(), label='pow')
    plt.plot(range(2018, 2048), pos_supply(), label='pos')
    plt.ylabel('Supply')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
