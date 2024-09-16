import glob
import os
from nltk.sentiment import SentimentIntensityAnalyzer
import streamlit as st
import plotly.express as px

st.title('Diary Tone')

st.subheader('Positivity')

# get the folder
folder_path = 'diary'

txt_files = glob.glob(os.path.join(folder_path,'*.txt'))

# store lists for the graphs
dates = []
positivitys = []
negativitys = []

# read the files in the folder
for file in txt_files:
    with open(file, 'r') as f:
        book = f.read()
# analyze and extract the setiment data
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(book)
# get the data that we want in a list and store it in a variable
    positivity = score['pos']
    negativity = score['neg']
# get dates base on the file name and use it later for the plot
    filename = os.path.basename(file)
    date = filename[:-4]
# append the for loop values in the list for global use as otherwise it will do the graph more than once
    dates.append(date)
    positivitys.append(positivity)
    negativitys.append(negativity)
# plotly graph for positivity and data correlation
figure = px.line(x=dates, y=positivitys, labels = {'x':'Dates', 'y' :'Positivity level'})
st.plotly_chart(figure)
# plotly graph for negativity and data correlation
st.subheader('Negativity')
figure = px.line(x=dates, y=negativitys, labels = {'x':'Dates', 'y' :'Negativity level'})
st.plotly_chart(figure)








