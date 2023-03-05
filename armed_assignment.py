# -*- coding: utf-8 -*-
"""
Created on Sun Mar  5 15:37:29 2023

@author: godwi
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def arm_1():
    #load data
    arm_1=pd.read_csv("C:/Users/godwi/Downloads/arm1.csv")
    #create line plot
    plt.plot(arm_1['Country Name'], arm_1['2013'], label='2013')
    plt.plot(arm_1['Country Name'], arm_1['2014'], label='2014')
    plt.plot(arm_1['Country Name'], arm_1['2015'], label='2015')
    plt.plot(arm_1['Country Name'], arm_1['2016'], label='2016')
    plt.plot(arm_1['Country Name'], arm_1['2017'], label='2017')
    plt.plot(arm_1['Country Name'], arm_1['2018'], label='2018')
    plt.plot(arm_1['Country Name'], arm_1['2019'], label='2019')
    #displaying legend
    plt.legend(loc='upper right', bbox_to_anchor=(1.3,1))
    #add a title
    plt.title("LINE PLOT")
    #displaying x label and y label
    plt.xlabel("Country")
    plt.ylabel("Armed forces (Millions)")
    #To display the grid
    plt.grid(zorder=0)
    plt.show()


def arm2():
    #load data
    arm=pd.read_csv("C:/Users/godwi/Downloads/arm1.csv")
    india=np.array(arm.iloc[0,1:]) 
    china=np.array(arm.iloc[1,1:])
    russia=np.array(arm.iloc[2,1:])
    usa=np.array(arm.iloc[3,1:])
    germany=np.array(arm.iloc[4,1:])
    france=np.array(arm.iloc[5,1:])
    #create scatter plot
    plt.scatter("India", np.average(india), label='India', s=200)
    plt.scatter("China", np.average(china), label='China', s=200)
    plt.scatter("Russia", np.average(russia), label='Russia', s=200)
    plt.scatter("USA", np.average(usa), label='USA', s=200)
    plt.scatter("Germany", np.average(germany), label='Germany', s=200)
    plt.scatter("France", np.average(france), label='France', s=200)
    #add a title
    plt.title("SCATTER PLOT")
    #displaying x and y label
    plt.xlabel("COUNTRY")
    plt.ylabel("Average of armed forces(in millions) ")
    plt.tight_layout()
    #displaying legend
    plt.legend(loc='center right',bbox_to_anchor=(1.25,1))
    # show the plot
    plt.show()

def plot_population_2013():
    # load data
    data = pd.read_csv("C:/Users/godwi/Downloads/arm2.csv")

    # drop missing values
    data.dropna(inplace=True)

    # create pie chart
    fig, ax = plt.subplots()
    ax.set_title("Population in 2013")
    ax.pie(data["2013"], labels=data['Country Name'], autopct='%1.1f%%')

    # show plot
    plt.show()
    


def plot_population_2019():
    # Read the CSV file
    data = pd.read_csv("C:/Users/godwi/Downloads/arm3.csv")

    # Create a figure and axis object
    fig, ax = plt.subplots()

    # Create the pie chart
    ax.pie(data["2019"], labels=data['Country Name'], autopct='%1.1f%%')

    # Add a title
    ax.set_title("Population in 2019")
    
    

    # Show the plot
    plt.show()
arm_1()    
arm2()    
plot_population_2013()
plot_population_2019()    