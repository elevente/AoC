time = 61677571
distance = 430103613071150

smaller = 0
for i in range(round(time / 2)):
    if i * (time - i) <= distance:
        smaller += 1
    else:
        break

print(time - (2 * smaller) + 1)