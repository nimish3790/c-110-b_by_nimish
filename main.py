from os import stat
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import csv
import pandas as pd

df = pd.read_csv('data.csv')
data = df['temp'].tolist()
#fig = ff.create_distplot([data],["Temp"], show_hist=False)
#fig.show()
population_mean = statistics.mean(data)
std_deviation = statistics.stdev(data)


dataset = []
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
std_deviation_of_sample = statistics.stdev(dataset)
print("Population mean is - ", population_mean)
print("Standard Deviation is - ", std_deviation)
print("Sample mean is - ", mean)
print("Sample standard Deviation is - ", std_deviation_of_sample)

def random_set_of_mean(counter):
    dataset_one = []
    for i in range(0, counter):
        random_index_one = random.randint(0, len(data)-1)
        value = data[random_index_one]
        dataset_one.append(value)
    mean_one = statistics.mean(dataset_one)
    return mean_one

def show_fig(mean_list):
    df1 = mean_list
    mean2 = statistics.mean(df1)
    fig1 = ff.create_distplot([df1], ["Temp"], show_hist=False)
    fig1.add_trace(go.Scatter(x=[mean2, mean2], y=[0, 1], mode = "lines", name = "Mean"))
    fig1.show()

def setup():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-", mean)
setup()

def standard_deviation():
    mean_list = []
    for i in range(0, 1000):
        set_of_means = random_set_of_mean(100)
        mean_list.append(set_of_means)
    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution :-", std_deviation)

standard_deviation()

