#assuming seaborn, pandas, and matplotlib are imported and necessary dataframe has been created

lav = '#9292dd'
mycolors = ["#115f9a", "#1984c5", "#22a7f0", "#48b5c4", "#76c68f", "#a6d75b", "#c9d52f", "#d0ee11", lav]
majors = ['General Agriculture','Genetics','General Business','General Education','General Engineering','Geological Engineering','General Medical and Health Services', 'Geology', 'Geosciences', 'General Social Sciences', 'Geography', 'Average(All majors)']
mycolors2 =["#115f9a", "#1984c5", "#22a7f0", "#48b5c4", "#76c68f", "#a6d75b", "#c9d52f", "#d0ee11"]
sns.set_palette(sns.color_palette(mycolors2))
y_indexes = np.arange(len(g_df['Major']))

fig, axes = plt.subplots(1, 2, figsize=(17, 5), sharex = True)

sns.barplot(y = 'Major_category', x = 'Unemployment_rate', data = cat_df, orient = 'h', dodge = False, ax = axes[0])
sns.set_palette(sns.color_palette(mycolors))
sns.barplot(y = y_indexes, x = 'Unemployment_rate', hue = 'Major_category', data = g_df, orient = 'h', dodge = False, ax = axes[1])

axes[0].set_title('Category Unemployment Rates')
axes[0].set_xlabel('')
axes[0].set_ylabel('')
axes[0].legend([], frameon = False)
axes[0].invert_yaxis()
axes[0].grid(linewidth=0.25)

axes[1].legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
axes[1].set_title('Major Unemployment Rates')
axes[1].set_xlabel('')
axes[1].set_ylabel('')
axes[1].grid(linewidth=0.25)
axes[1].set_yticklabels(labels = (majors))
fig.tight_layout()
plt.savefig('cat_and_majors_barchart',dpi=300, bbox_inches = "tight")
