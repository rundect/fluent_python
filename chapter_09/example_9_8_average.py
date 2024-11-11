def make_averager():
    series = []
    def averager(new_value):
        series.append(new_value)
        total = sum(series)
        return total / len(series)
    return averager

avg = make_averager()
print(avg(10))
# 10.0
print(avg(11))
# 10.5
print(avg(15))
# 12.0
