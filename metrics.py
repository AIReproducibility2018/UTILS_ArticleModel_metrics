import os
import pandas as pd
import matplotlib
import seaborn as sns
from matplotlib import pyplot as plt


def normalize_title(category):
    split = category.split(' ')
    return ' '.join([split[0].title()] + split[1:])


def create_barh_plot(data, output_path, **kwargs):
    fig = data.plot.barh(**kwargs)
    fig.invert_yaxis()
    fig.xaxis.tick_top()
    fig.xaxis.set_label_position('top')
    fig.set_xlabel("Score")
    fig.get_figure().savefig(output_path, bbox_inches='tight')
    plt.clf()
    return fig


def main(output_directory):
    plt.style.use('seaborn-white')
    colors = ['#0485d1bf', '#75bbfdbf', '#00ffffbf', '#04d8b2bf']
    custom_cmap = matplotlib.colors.ListedColormap(colors)
    data = pd.read_csv('metrics.csv', sep=',',
                       quotechar='"',
                       doublequote=True,
                       header=0,
                       encoding='utf-8')
    data.drop(data.columns[[1, 2]], axis=1, inplace=True)
    data.set_index('Result', inplace=True)
    data = data.transpose()
    data.index = data.index.map(normalize_title)

    path = os.path.join(output_directory, 'metrics_barh.svg')
    create_barh_plot(data, path, figsize=(8, 8), cmap=custom_cmap)


if __name__ == '__main__':
    main(output_directory='figures')
