def sum_of_intervals(intervals):
    result = 0
    intervals = sorted(intervals)
    start = intervals[0][0]
    end = intervals[0][1]

    for i in intervals:
        if i[0] <= end:
            end = max(i[1], end)
        else:
            result += abs(end - start)
            start = i[0]
            end = i[1]
    return result + abs(end - start)


def main():
    print(sum_of_intervals([(1, 5)]))  # result should be 4
    print(sum_of_intervals([(1, 5), (6, 10)]))  # result should be 8
    print(sum_of_intervals([(1, 5), (1, 5)]))  # result should be 4
    print(sum_of_intervals([(1, 4), (7, 10), (3, 5)]))  # result should be 7
    # Large numbers
    print(sum_of_intervals([(-1_000_000_000, 1_000_000_000)]))  # result should be 2_000_000_000
    print(sum_of_intervals([(0, 20), (-100_000_000, 10), (30, 40)]))  # result should be 100_000_030


if __name__ == "__main__":
    main()
