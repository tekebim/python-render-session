import streamlit as st
import pandas as pd
import numpy as np
import os

st.title('Exploring Data with Streamlit')

DATA_URL = 'data/Pokemon.csv'

# set cache request
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# function for file_selector
def file_selector(folder_path='./data'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox("Select a dataset",filenames)
    return os.path.join(folder_path,selected_filename)

filename = file_selector()
st.info("Dataset selected {}".format(filename))

# Read Data
df = pd.read_csv(filename)

# loading the dataset
data_load_state = st.text('Loading data...')
data = load_data(10000)
# success
data_load_state.text("Done! (using st.cache)")

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)


st.subheader('Data\'s columns')
st.write(data.columns.tolist())

# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)
# st.write(data.columns.tolist())
