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
    supply_decay = 5.7327557121556496e-12
    start_year = 2018
    circulating_supply_year = []
    year_ms = timedelta(days=365).total_seconds() * 1000
    for i in range(start_year, 2048):
        exponent = -supply_decay * (i-start_year) * float(year_ms)
        supply = genesis_supply + \
            (0.10594132556065439 / supply_decay * (1.0 - math.pow(2, exponent)))
        circulating_supply_year.append(supply)
    return circulating_supply_year


def main():
    plt.plot(range(2018, 2048), pow_supply(), label='pow')
    plt.plot(range(2018, 2048), pos_supply(), label='pos')
    plt.ylabel('Supply')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
