import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pylab as plt

def visualize(path2):

    work = year2[year2['workingday'] == 1]
    rest = year2[year2['workingday'] == 0]
    plt.figure(figsize=(10, 10))
    plt.bar(work['dteday'], work['cnt'], width=0.4, label='Work day')
    plt.bar(rest['dteday'], rest['cnt'], width=0.4, label='Rest day')
    plt.xlabel('Date')
    plt.ylabel('Number of Bike-Sharing Users in total')
    plt.title('Bike-Sharing Users by Rest days and Work days in 2011')
    plt.legend()

    pal = sns.cubehelix_palette(10, rot=-.25, light=.7)
    g = sns.FacetGrid(year2, row='mnth',hue='mnth',aspect=10,height=.5,palette=pal)
    g.map(sns.kdeplot, 'cnt',bw_adjust=.5,clip_on=False,fill=True,alpha=1,linewidth=1.5)
    g.map(sns.kdeplot, 'cnt',clip_on=False,color='w',lw=2,bw_adjust=.5)
    g.refline(y=0,linewidth=2,linestyle='-',color=None,clip_on=False)
    def label(x,color,label):
        ax = plt.gca()
        ax.text(0, .2,label,fontweight='bold',color=color,
                ha='left',va='center',transform=ax.transAxes)
    g.map(label,'cnt')
    g.figure.subplots_adjust(hspace=-.05)
    g.set_titles('')
    g.set(yticks=[],ylabel='')
    g.despine(bottom=True,left=True)
    g.fig.suptitle('Monthly Distribution in 2012', fontsize=16, fontweight='bold', y=1.05)

    season_dict = {1: 'spring', 2: 'summer', 3: 'fall', 4: 'winter'}
    color_dict = {1: 'green', 2: 'red', 3: 'yellow', 4: 'blue'}
    palette = [color_dict[season] for season in season_dict.keys()]
    plot = sns.catplot(x="season", y="cnt", hue="season", kind="bar", data=year2, palette=palette)
    plot.fig.suptitle('Number of Users by Season in 2012')
    plot.set(xlabel='Season', ylabel='Number of Users')
    legend = plot.ax.legend(title='Season')
    for season, label in season_dict.items():
        legend.get_texts()[season-1].set_text(label)

    plt.show()
    