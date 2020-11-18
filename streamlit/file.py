import streamlit as st
import pandas as pd
import numpy as np
import os

st.title('Exploring Data with Streamlit')

# method load specific dataset
DATA_URL = 'data/Pokemon.csv'
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# method for dataset files selector
def file_selector(folder_path='./data'):
    # list files name on folder_path
    filenames = os.listdir(folder_path)
    # select specific dataset from list
    selected_filename = st.selectbox('Select a dataset',filenames)
    # return the path / file
    return os.path.join(folder_path,selected_filename)

filename = file_selector()
# display filename selected
st.info('Dataset selected {}'.format(filename))

# Read Data
df = pd.read_csv(filename)

# Show Dataset
if st.button("Show dataset sample"):
    st.write(df.head(10))

# Show Columns
if st.button("Show columns name"):
    st.write(df.columns)

if st.checkbox("Show sample of the current Dataset"):
    number = st.number_input("Number of Rows to View")
    st.dataframe(df.head(number))

# Show Dataset
if st.checkbox('Show Dataset'):
    number = st.number_input('Number of Rows to View')
    st.dataframe(df.head(number))

# loading the dataset
data_load_state = st.text('Loading data...')
data = load_data(10000)

# success
data_load_state.text('Done! (using st.cache)')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.subheader('Data\'s columns')
st.write(data.columns.tolist())

# st.write(data.columns.tolist())
