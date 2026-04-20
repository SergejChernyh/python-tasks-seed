"""
Sortings performance analysis: Complexity vs Array Size
"""

import random
import time
import matplotlib.pyplot as plt
from counting_container import CountingList, CountingOrdered
import sortings

if __name__ == "__main__":
    sizes = list(range(0, 1001, 100))
    fig, axs = plt.subplots(3, 1)

    axs[0].set_title("Time")
    axs[1].set_title("Comps")
    axs[2].set_title("Swaps")

    for name, sort_alg in sortings.sorting_algs:
        times, swaps, comps = [], [], []

        for size in sizes:
            raw_data = list(range(size))
            random.seed(1234567)
            random.shuffle(raw_data)

            data = CountingList(list(map(CountingOrdered, raw_data)))

            start = time.time()
            sort_alg(data)
            end = time.time()

            times.append(end - start)
            comps.append(CountingOrdered.comparisons())
            swaps.append(CountingList.likely_swaps())

            CountingList.reset_stats()
            CountingOrdered.reset_stats()

        axs[0].plot(sizes, times, label=name)
        axs[1].plot(sizes, comps, label=name)
        axs[2].plot(sizes, swaps, label=name)

    fig.subplots_adjust(hspace=0.5)

    for ax in axs:
        ax.set_yscale("log")

    axs[-1].set_xlabel("Array size")
    axs[0].legend()

    plt.show()
