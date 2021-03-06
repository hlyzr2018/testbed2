import matplotlib.pyplot as plt
import pandas as pd
import os


path = 'E:\\newdata\IV Data\Copper\cleaneddata'
f1 = '铜期货历史数据'
f2 = '铜期货历史数据US'
fx = 'USD_CNY历史数据'

reverse = False

data1 = pd.read_csv(path + os.sep + f1 + '.csv')
data2 = pd.read_csv(path + os.sep + f2 + '.csv')
fxdata = pd.read_csv(path + os.sep + fx + '.csv')

datalen = 220 * 1

c1 = list(data1['收盘'])
c2 = list(data2['收盘'])
fxc = list(fxdata['收盘'])

adjc1 = list(reversed(c1))[-1 * datalen: -1]
adjc2 = list(reversed(c2))[-1 * datalen: -1]
adjfxc = list(reversed(fxc))[-1 * datalen: -1]

adjc1b = [adjc1[i] / adjfxc[i] for i in range(len(adjc1))]
adjc1 = adjc1b

rio1 = 100 / adjc1[0]
rio2 = 100 / adjc2[0]
#
aadjc1 = [rio1 * i for i in adjc1]
aadjc2 = [rio2 * i for i in adjc2]

diff = [aadjc1[i] - aadjc2[i] for i in range(len(aadjc1))]

I1, = plt.plot(aadjc1, label='CN Copper')
I2, = plt.plot(aadjc2, label='US Copper')
Id, = plt.plot(diff, label='DIFF')

plt.tight_layout()
plt.grid()
plt.legend()
plt.show()

