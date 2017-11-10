import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style("whitegrid")
df = pd.read_csv("investition.csv")
g=sns.barplot(x='Jahr', y='Umsatz in Milliarden Euro', data=df, palette=sns.cubehelix_palette(8, start=0.5, rot=-.5, light=.50, dark=.20))
#g=sns.barplot(x='Jahr', y='Umsatz in Millionen Euro', data=df, palette=sns.color_palette('YlOrBr', 4))
for index, row in df.iterrows():
    plt.text(row.name, row[1]/2, row[1], color='white', ha='center', fontsize='14')
plt.savefig('investition.png', transparent=True, dpi=1000)
plt.show()
