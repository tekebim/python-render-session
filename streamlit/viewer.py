import streamlit as st
import pandas as pd
import numpy as np
import os

st.title('Exploring Data with Streamlit')



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
st.subheader('Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur')
if st.button("Show dataset sample"):
    st.write(df.head(10))

# Show Columns
st.subheader('Afficher le nom des colonnes du dataset')
if st.button("Show dataset columns"):
    st.write(df.columns)

st.subheader('Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées')

# Show Shape
st.subheader('La shape du dataset, par lignes et par colonnes')
if st.button("Show shape"):
    st.write(df.describe())

if st.checkbox("Show sample of the current Dataset"):
    number = st.number_input("Number of Rows to View")
    st.dataframe(df.head(number))

# Show Dataset
if st.checkbox('Show Dataset'):
    number = st.number_input('Number of Rows to View')
    st.dataframe(df.head(number))

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

