def get_median(data: list[float])-> float:
    data.sort()
    n = len(data)
    if n % 2 == 0:
        return (data[n//2 - 1] + data[n//2]) / 2
    else:
        return data[n//2]