import streamlit as st
import pandas as pd
import numpy as np

# method load specific dataset
DATA_URL = 'data/Pokemon.csv'
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    # data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# loading the dataset
data_load_state = st.text('Loading data...')
data = load_data(10000)

# success
data_load_state.text('Done! (using st.cache)')

st.subheader('Data\'s columns')
st.write(data.columns.tolist())

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)
