z = []
lowest = 0
for child in range(10):
    for i in range(8):
        if child == i:
            z.append(child)
    if child in z:
        continue
    print(child)
