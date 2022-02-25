import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df=pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True)
df['date']=pd.to_datetime(df['date'])
df.set_index('date',inplace=True)
df =df

# Clean data
df=df.sort_values(by='value')
df=df.loc[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]
df =df


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize = (9, 9))
    grap1=sns.lineplot(x='date',y='value',color='red',data=df).set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')




    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar=df.copy()
    m=df.index.month.values
    count=0
    name=[]
    for month in m:
      count+=1
      if month==1:
          name.append('June')
      elif month==2:
          name.append('February')
      elif month==3:
          name.append('March')
      elif month==4:
          name.append('April')
      elif month==5:
          name.append('May')
      elif month==6:
          name.append('June')
      elif month==7:
          name.append('July')
      elif month==8:
          name.append('August')
      elif month==9:
          name.append('September')
      elif month==10:
          name.append('October')
      elif month==11:
          name.append('November')
      elif month==12:
          name.append('December')     
    df_bar['month']=name

    # Draw bar plot
    df_bar['year']=df.index.year.values        
    df_bar=df_bar.groupby(['year', 'month']).mean().reset_index()

    fig, ax = plt.subplots(figsize = (9, 9))
    grap2=sns.barplot(x='year',y='value',hue='month',hue_order=["January", "February", "March","April", "May","June", "July" ,"August","September" ,"October","November","December"] ,data=df_bar).set(xlabel='Years',ylabel='Average Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2,figsize = (9, 9))
    grap3=sns.boxplot(x='year', y='value', data=df_box, ax=axes[0]).set(title='Year-wise Box Plot (Trend)',xlabel='Year',ylabel='Page Views')
    grap4=sns.boxplot(x='month', y='value',palette="Set2", data=df_box, order=["Jan", "Feb", "Mar","Apr", "May","Jun","Jul" ,"Aug","Sep","Oct","Nov","Dec"], ax=axes[1]).set(title='Month-wise Box Plot (Seasonality)',xlabel='Month',ylabel='Page Views')   


    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
