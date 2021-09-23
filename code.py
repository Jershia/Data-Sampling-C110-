import csv
import statistics
import plotly.express as px
import pandas as pd
import math
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

def random_mean(counter):
    dataset = []
    for i in range (0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    sampling_mean = statistics.mean(dataset)
    return sampling_mean

def show_fig(mean_list):
    df = mean_list
    fig = ff.create_distplot([df], ["temp"], show_hist=False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        set_of_means= random_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )
    population_mean = statistics.mean(data)
    print("population mean:- ", population_mean)

setup()
