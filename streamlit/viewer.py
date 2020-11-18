import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
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

# define filename as current file selected
filename = file_selector()
# display filename selected
st.info('Dataset selected {}'.format(filename))

# Read Dataset
df = pd.read_csv(filename)

# Show sample head
st.write(df.head(5))

# Show Dataset
st.subheader('1. Chargement du Dataset - Aperçu')
if st.button('Show dataset sample'):
    st.write(df.head(10))

# Select custom rows index
st.subheader('2. Afficher le dataset chargé suivant un nombre de ligne entrées par l’utilisateur')
selected_indices = st.multiselect('Sélectionner des lignes :', df.index)
if  selected_indices:
    selected_rows = df.loc[selected_indices]
    st.write('### Lignes à afficher', selected_rows)

# Show Columns
st.subheader('3. Afficher le nom des colonnes du dataset')
if st.button("Show dataset columns"):
    st.write(df.columns)

st.subheader('4. Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées')

# Show Datatypes
if st.button('Data Info'):
    st.write(df.info)

# Show Datatypes
if st.button('Data Types'):
    st.write(df.dtypes)

st.subheader('5. Afficher les statistiques descriptives du dataset')

# Show Summary
if st.checkbox('Statistiques : summary'):
    st.write(df.describe().T)



# Show Shape
st.subheader('6. La shape du dataset, par lignes et par colonnes')
if st.button("Show shape"):
    st.write(df.shape())
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
st.title("Data Visualization")

st.subheader('7. Afficher plusieurs type de graphique dans une partie visualisation avec notamment :')

st.subheader('7.1. Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)')

st.subheader('7.2. Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)')

