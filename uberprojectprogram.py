import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os
from folium.plugins import HeatMap
import folium
import webbrowser
import plotly.graph_objects as go
import plotly.offline as ply


def plot(df,day):
    basemap=folium.Map()
    df_out=df[df['weekday']==day]
    df_out.groupby(['Lat','Lon'])['weekday'].count().reset_index()
    HeatMap(df_out.groupby(['Lat','Lon'])['weekday'].count().reset_index(),zoom=20,radius=15).add_to(basemap)
    basemap.save("basemap.html")
    webbrowser.open("basemap.html")


def fun(i):
    if i == 4:
        x = "APRIL"
        return x
    elif i == 5:
        x = "MAY"
        return x
    elif i == 6:
        x = "JUNE"
        return x
    elif i == 7:
        x = "JULY"
        return x
    elif i == 8:
        x = "AUGUST"
        return x
    elif i == 9:
        x = "SEPTEMBER"
        return x

def heatmap(col1,col2):
    by_cross = df.groupby([col1,col2]).apply(lambda x:len(x))
    pivot=by_cross.unstack()
    plt.figure(figsize=(10,6))
    plt.title("{} vs {}".format(col1,col2))
    sns.heatmap(pivot,annot=False)
    plt.show()

def fun1(df):
    x = df.groupby('month')['hour'].count().index
    y = df.groupby('month')['hour'].count()
    t=go.Bar(x=x, y=y,text=y,textposition='outside')
    layout = go.Layout(title="MONTH WISE TOTAL RIDES",xaxis={'title':"months"},yaxis={'title':"in million"})
    data = [t]
    fig = dict(data=data, layout=layout)
    ply.plot(fig, filename="sample.html")








def fun2(df):
    x = df["weekday"].value_counts().index
    y = df["weekday"].value_counts()
    plt.bar(x, y)
    plt.xlabel("WEEKDAYS")
    plt.ylabel("NO.OF RIDES")
    plt.title("JOURNEY IN WEEKDAYS IN TOTAL 6 MONTHS")
    plt.show()

def fun3(df):
    for i in df['month'].unique():
        plt.figure(figsize=(5, 3))
        m=fun(i)
        plt.title("JOURNEY IN WEEKDAYS {}".format(m))
        plt.xlabel("WEEKDAYS")
        plt.ylabel("NO.OF RIDES")
        df[df['month'] == i]['weekday'].hist(rwidth=0.8)
        plt.show()


def fun4(df):
    plt.title("JOURNEY BY HOURS IN TOTAL 6 MONTHS ")
    plt.xlabel("24 HOURS")
    plt.ylabel("COUNT")
    plt.hist(df['hour'], rwidth=0.85, bins=24)
    plt.xticks([int(x) for x in range(int(input(),difference))])
    plt.show()

def fun5(df):
    for i in df['month'].unique():
        plt.figure(figsize=(5, 3))
        m=fun(i)
        plt.title("JOURNEY BY HOURS IN {}".format(m))
        df[df['month'] == i]['hour'].hist(rwidth=0.9,bins=24)
        plt.xticks([0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
        plt.xlabel("24 HOURS")
        plt.ylabel("COUNT")
        plt.show()


def fun6(df):
    plt.title("analysis by day in total 6 months")
    plt.hist(df['day'], rwidth=0.9, bins=31)
    plt.xticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
         31])
    plt.xlabel('days in month')
    plt.ylabel('total rides')
    plt.show()

def fun7(df):
    for i, month in enumerate(df['month'].unique(), 1):
        df_out = df[df['month'] == month]
        plt.hist(df_out['day'], rwidth=0.7, bins=31)
        m=fun(month)
        plt.title("analysis by day {}".format(m))
        plt.xlabel('days in month {}'.format(fun(month)))
        plt.ylabel('total rides')
        plt.show()

def fun8(df):
    x = sns.pointplot(x="hour", y="Lat", data=df)
    x.set_title("hours vs latitude of passengers in total data")
    plt.show()

def fun9(df):
    x = sns.pointplot(x="hour", y="Lat", hue="weekday", data=df)
    x.set_title("hours vs latitude of passengers based on weekday ")
    plt.show()

def fun10(df):
    x = sns.pointplot(x="hour", y="Lat", hue="month", data=df)
    x.set_title("hours vs latitude of passengers based on monthly")
    plt.show()

def fun11(df):
    base = df.groupby(['Base', 'month'])['Date/Time'].count().reset_index()
    plt.figure(figsize=(10, 6))
    sns.lineplot(x='month', y='Date/Time', hue='Base', data=base)
    plt.show()

def fun12(df):
    heatmap('weekday', 'hour')

def fun13(df):
    heatmap('day', 'hour')

def fun14(df):
    heatmap('weekday', 'month')

def fun15(df):
    heatmap('day', 'month')

def fun16(df):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Lon'], df['Lat'], 'r+', ms=0.5)
    plt.xlabel("longitude")
    plt.ylabel("latitude")
    plt.title("LOCATIONS")
    plt.xlim(-74.2, -73.7)
    plt.ylim(40.6, 41)
    plt.show()

def fun17(df):
    x=input("enter a weekday and first letter should be capital:")
    plot(df,x)

if __name__ == '__main__':
    files = os.listdir(r"C:\projects\uber\files")

    path = r"C:\projects\uber\files"
    final = pd.DataFrame()

    for file in files:
        df = pd.read_csv(path + "/" + file, encoding='utf-8')
        final = pd.concat([df, final])
    df = final.copy()
    df['Date/Time'] = pd.to_datetime(df['Date/Time'], format="%m/%d/%Y %H:%M:%S")
    df['weekday'] = df['Date/Time'].dt.day_name()
    df['day'] = df['Date/Time'].dt.day
    df['month'] = df['Date/Time'].dt.month
    df['hour'] = df['Date/Time'].dt.hour
    df['minute'] = df['Date/Time'].dt.minute
    print("1.which month has maximum ride\n2.analysis of weekday for total\n3.analysis of weekday for monthly")
    print("4.analysis of hour for total\n5.analysis of hour monthly")
    print("6.analysis of day for total\n7.analysis of day monthly")
    print("8.rush in hour for total\n9.rush in hour based on weekday\n10.rush in hour based on monthly")
    print("11.which base number gets popular by month name")
    print("12.cross analysis based on heatmap hour vs weekday\n13.cross analysis based on heatmap hour vs day")
    print("14.cross analysis based on heatmap month vs weekday\n15.cross analysis based on heatmap month vs weekday")
    print("16.locations\n17.perform Spatial Analysis using heatmap to get a clear cut of Rush on particular day")
    print("18.exit")
    while(1):
        n=int(input("select a value between 1-18:"))
        if n==1:
            fun1(df)
        elif n==2:
            fun2(df)
        elif n==3:
            fun3(df)
        elif n==4:
            fun4(df)
        elif n==5:
            fun5(df)
        elif n==6:
            fun6(df)
        elif n==7:
            fun7(df)
        elif n==8:
            fun8(df)
        elif n==9:
            fun9(df)
        elif n==10:
            fun10(df)
        elif n==11:
            fun11(df)
        elif n==12:
            fun12(df)
        elif n==13:
            fun13(df)
        elif n==14:
            fun14(df)
        elif n==15:
            fun15(df)
        elif n==16:
            fun16(df)
        elif n==17:
            fun17(df)
        elif n==18:
            exit()
        else:
            print("enter value between 1-18")







