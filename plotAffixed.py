import matplotlib.pyplot as plt
import pandas as pd

summary_file = "-eng-us-all-1gram-20120701.summary.txt"

df = pd.read_csv("ity"+summary_file, sep='\t', header=(0))
df_ness = pd.read_csv("ness"+summary_file, sep='\t')
df_ment = pd.read_csv("ment"+summary_file, sep='\t', header=(0))

def endswith(x):
    if not isinstance(x, str):
        return False
    return str.endswith(x, 'k')

pd.set_option('display.max_columns', None)

def plot(df, ax, label):
    endings = df.loc[df['Base Phon'].apply(endswith)]
    print(endings)

    value_counts = df['First Attested'].value_counts()
    flipped = pd.Series(data=value_counts.index, index=value_counts.values)
    flipped.plot(ax=ax, kind='density', xticks=[1700, 1800, 1900, 2000], label=label)
    ax.set_xlim(1700, 2050)
    
    endings['First Attested'].plot(ax=ax, kind='density', xticks=[1700, 1800, 1900, 2000], label="k-"+label)
    

fig = plt.figure()
ax=plt.subplot(111)
plot(df_ness, ax, "ness")
plot(df, ax, "ity")
plot(df_ment, ax, "ment")
ax.legend()
plt.show()