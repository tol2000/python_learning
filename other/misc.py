def cnt():
    try:
        cnt.qnty += 1
    except AttributeError:
        cnt.qnty = 1
    return cnt.qnty


for i in range(5):
    print(cnt())
