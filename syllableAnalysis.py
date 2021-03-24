import matplotlib.pyplot as plt
import pandas as pd

summary_file = "-eng-us-all-1gram-20120701.summary.txt"

df = pd.read_csv("wise"+summary_file, sep='\t', header=(0))
# df_hood = pd.read_csv("hood"+summary_file, sep='\t', header=(0))
# df_ness = pd.read_csv("ness"+summary_file, sep='\t', header=(0))
# df_age = pd.read_csv("age"+summary_file, sep='\t', header=(0))
df_ful = pd.read_csv("ful"+summary_file, sep='\t', header=(0))


pd.set_option('display.max_columns', None)

def frequency(df):
    return len(df.index)

# ratio of monosyllabic base words in -wise list
# print(frequency(df))
# print(frequency(df[df['Base Final Stress'] == 'monosyl']))


fig = plt.figure()
ax=plt.subplot(111)

def plot_syllables(df, label):
    monosyl = df[df['Base Final Stress'] == 'monosyl']
    multisyl = df[df['Base Final Stress'] != 'monosyl']

    # print(df[df['First Attested'] > 1900])
    
    monosyl['First Attested'].plot(ax=ax, kind='density', xticks=[1700, 1800, 1900, 2000], label=label+" monosyl")
    multisyl['First Attested'].plot(ax=ax, kind='density', xticks=[1700, 1800, 1900, 2000], label=label+" multisyl")
    ax.set_xlim(1700, 2000)


plot_syllables(df, "wise")
plot_syllables(df_ful, "ful")
ax.legend()
plt.show()