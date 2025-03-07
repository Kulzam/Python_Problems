w = [12, 15, 14, 10, 18, 20, 22, 24, 17, 19]
l = len(w)
total = sum(w)
wsort = sorted(w)
if l % 2 == 0:
    median_x = (wsort[l // 2 - 1] + wsort[l // 2]) / 2
else:
    median_x = wsort[l // 2]
mean = total / l
print(f"mean: {mean}")
print(f"median_x: {median_x}")
