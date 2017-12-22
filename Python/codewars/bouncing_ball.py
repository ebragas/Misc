def bouncingBall(h, bounce, window):
    if h < 0 or bounce < 0 or window < 0:
        return -1

    times = 1
    while True:
        if h > window:
            times += 1
            h *= bounce
            continue
        else:
            return times


print("Times:", bouncingBall(3, 0.66, 1.5))
print("Times:", bouncingBall(30, 0.66, 1.5))
