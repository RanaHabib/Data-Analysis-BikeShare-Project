# Bike Share data analysis project 

## Overview

In this project, you will make use of Python to explore data related  to bike share systems for three major cities in the United  States—Chicago, New York City, and Washington. You will write code to  import the data and answer interesting questions about it by computing  descriptive statistics. You will also write a script that takes in raw  input to create an interactive experience in the terminal to present  these statistics.

![img](https://video.udacity-data.com/topher/2018/March/5aa7718d_divvy/divvy.jpg)

*Divvy is a bicycle sharing system in the City of Chicago and two adjacent suburbs (image: [Wikipedia](https://en.wikipedia.org/wiki/Divvy))*

## What Software Do I Need?

To complete this project, the following software requirements apply:

- You should have Python 3, NumPy, and pandas installed using Anaconda
- A text editor, like [Sublime](https://www.sublimetext.com/) or [Atom](https://atom.io/).
- A terminal application (Terminal on Mac and Linux or Cygwin on Windows).

## Bike Share Data

Over the past decade, bicycle-sharing systems have been growing in  number and popularity in cities across the world. Bicycle-sharing  systems allow users to rent bicycles on a very short-term basis for a  price. This allows people to borrow a bike from point A and return it at point B, though they can also return it to the same location if they'd  like to just go for a ride. Regardless, each bike can serve several  users per day.

Thanks to the rise in information technologies, it is easy for a user of the system to access a dock within the system to unlock or return  bicycles. These technologies also provide a wealth of data that can be  used to explore how these bike-sharing systems are used.

In this project, you will use data provided by [Motivate](https://www.motivateco.com/), a bike share system provider for many major cities in the United  States, to uncover bike share usage patterns. You will compare the  system usage between three large cities: Chicago, New York City, and  Washington, DC.

## The Datasets

Randomly selected data for the first six months of 2017 are provided  for all three cities. All three of the data files contain the same core **six (6)** columns:

- Start Time (e.g., 2017-01-01 00:07:57)
- End Time (e.g., 2017-01-01 00:20:53)
- Trip Duration (in seconds - e.g., 776)
- Start Station (e.g., Broadway & Barry Ave)
- End Station (e.g., Sedgwick St & North Ave)
- User Type (Subscriber or Customer)

The Chicago and New York City files also have the following two columns:

- Gender
- Birth Year



![img](https://video.udacity-data.com/topher/2018/March/5aa771dc_nyc-data/nyc-data.png)

*Data for the first 10 rides in the **new_york_city.csv** file*



The original files are much larger and messier, and you don't need to  download them, but they can be accessed here if you'd like to see them ([Chicago](https://www.divvybikes.com/system-data), [New York City](https://www.citibikenyc.com/system-data), [Washington](https://www.capitalbikeshare.com/system-data)). These files had more columns and they differed in format in many cases. Some [data wrangling](https://en.wikipedia.org/wiki/Data_wrangling) has been performed to condense these files to the above core six  columns to make your analysis and the evaluation of your Python skills  more straightforward. In the Data Wrangling course that comes later in  the Data Analyst Nanodegree program, students learn how to wrangle the  dirtiest, messiest datasets, so don't worry, you won't miss out on  learning this important skill!

## Statistics Computed

You will learn about bike share use in Chicago, New York City, and  Washington by computing a variety of descriptive statistics. In this  project, you'll write code to provide the following information:

**#1 Popular times of travel** (i.e., occurs most often in the start time) 

- most common month
- most common day of week
- most common hour of day

**#2 Popular stations and trip**

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

**#3 Trip duration**

- total travel time
- average travel time

**#4 User info**

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)

## The Files

To answer these questions using Python, you will need to write a  Python script. To help guide your work in this project, a template with  helper code and comments is provided in a **bikeshare.py** file, and you will do your scripting in there also. You will need the three city dataset files too: 

- **chicago.csv**
- **new_york_city.csv**
- **washington.csv**

All four of these files are zipped up in the **Bikeshare** file in the resource tab in the sidebar on the left side of this page.  You may download and open up that zip file to do your project work on  your local machine. 

Some versions of this project also include a Project Workspace page  in the classroom where the bikeshare.py file and the city dataset files  are all included, and you can do all your work with them there.

## Introduction

Though there are a number of ways you can go about tackling this project, we recommend using **NumPy** and **pandas**.  Using these libraries is the industry standard for working with data  in Python. In the quizzes in this and the following sections, you will  get some practice using NumPy and pandas to complete different parts of  the project. Then for the project, you will need to piece your code  together with some additional code to complete a final project! These  sections will likely be helpful if you use NumPy and pandas to complete  the project.



## Understanding the Data

Let's use pandas to better understand the bike share data! Use this code editor to explore **chicago.csv** and answer the questions below. The file included here is a mini  version of one of the actual data files you will work with for the  project. It only includes 400 rows, but the structure and columns are  the same.

- What columns are in this dataset?
- Are there any missing values?
- What are the different types of values in each column?

Some useful pandas methods: 

- `df.head()`
- `df.columns`
- `df.describe()`
- `df.info()`
- `df['column_name'].value_counts()`
- `df['column_name'].unique()`