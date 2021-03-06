import pandas as pd
import numpy as np
from japanmap import picture
import japanmap
import matplotlib.pyplot as plt
from pylab import rcParams

word = '離婚率'

df = pd.read_csv("都道府県別出生率.csv")
df_i = df.set_index('都道府県')
print(df_i)

cmap = plt.get_cmap('YlOrBr')#coolwarm
norm = plt.Normalize(vmin=df_i[f'{word}'].min(), vmax=df_i[f'{word}'].max())
fcol = lambda x: '#' + bytes(cmap(norm(x), bytes=True)[:3]).hex()
plt.rcParams["font.family"] = "Meiryo"
plt.colorbar(plt.cm.ScalarMappable(norm, cmap))
plt.imshow(picture(df_i[f'{word}'].apply(fcol)));
plt.tick_params(bottom=False, top=False, left=False, right=False,
                labelbottom=False, labeltop=False, labelleft=False, labelright=False)
plt.text(0, 670, '総務省統計局 2-16　都道府県別出生率（令和元年）：https://www.stat.go.jp/data/nihon/02.html', fontname="Meiryo", style = 'italic', size =7)
plt.title('都道府県別離婚率（令和元年）', fontname="Meiryo")
plt.show()

from japanmap import get_data, pref_points
qpqo = get_data()
pnts = pref_points(qpqo)
from japanmap import pref_map
x=df_i['婚姻率']
cols = x.apply(fcol)
# 県ごとに色分け + 境界なし (SVG to PNG)
svg_code = pref_map(range(1,48), cols=cols.values, tostr=True)

# SVG 調整: サイズ、枠線
svg_code = svg_code.replace('<svg ', '<svg  width="500px" height="500px" ')
svg_code = svg_code.replace('<path ', '<path style="stroke: black; stroke-width: 0.001" ')
with open('japan.svg', 'w') as fp:
    fp.write(svg_code)
