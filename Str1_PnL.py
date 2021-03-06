import matplotlib.pyplot as plt
import pandas as pd
import os

brickpath = r'D:\HIST Data\Bricks'
pairs = 'XAUUSD'
bp = 4
brickfile = brickpath + os.sep + pairs + '-bricks-{}ip.txt'.format(bp)

df = pd.read_csv(brickfile, header=None)
gn = df[3].values
o = df[0].values

PnL = [10000]
SorP = True
Percent = 10
Pos = 1
expense = 0

dl = len(gn)
backnum = 1
for i in range(dl):
    if i > backnum:
        conP = True
        # conN = True
        nums = list(range(2, backnum + 2))
        for bi in nums:
            conP &= gn[i - bi] < 0

        if conP:
            Pos = 1
            if not SorP:
                Pos = int(PnL[-1] * Percent / o[i - 1])
            pnl = (o[i] - o[i - 1] - expense) * Pos
            PnL.append(PnL[-1] + pnl)
        # elif conN:
        #     Pos = 1
        #     if not SorP:
        #         Pos = int(PnL[-1] * Percent / o[i - 1])
        #     pnl = (o[i - 1] - o[i] - expense) * Pos
        #     PnL.append(PnL[-1] + pnl)

plt.plot(PnL)
plt.tight_layout()
plt.grid()
plt.show()