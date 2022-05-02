import random, time


stock_value = 100
bal = 5
loss = 0

playing = True

while playing:
    w_l = random.randint(1, 10)
    b_s = random.randint(1, 50)
    if w_l >= 6:
        stock_value += b_s
        print(f"Stock Value Increased, new price : ${stock_value} per share")
    else:
        stock_value -= b_s
        b_s = loss
        if stock_value - loss < 0:
            stock_value = 0
        print(f"Stock Value Decreased, new price : ${stock_value} per share")
    time.sleep(5)
