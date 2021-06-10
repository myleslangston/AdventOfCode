def day2(arr):
    count = 0
    for i in arr:
        for l in arr:
            if i in arr and l == range(i):
                count += 1
                print(count)

day2([["1-3", "a", "abcde"], ["1-3", "b", "cdefg"], ["2-9", "c", "ccccccccc"]])