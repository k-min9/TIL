switches = [1]*20 + [0]*19

loop = (len(switches) - 1) // 20 + 1
for l in range(loop):
    print(*switches[l*20:(l+1)*20])