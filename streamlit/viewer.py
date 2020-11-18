import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns
import os
st.set_option('deprecation.showPyplotGlobalUse', False)

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

# Show raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)

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

# Show Datatypes columns
st.subheader('4. Afficher le type des colonnes du dataset ainsi que les colonnes sélectionnées')
if st.button('Data Types'):
    st.write(df.dtypes)

# selected columns
selected_columns = st.multiselect('Sélectionner des colonnes :', df.columns)
if selected_columns:
    # selected_cols = df.loc[selected_columns]
    # selected_cols = df.loc[selected_cols].dtypes()
    st.write('You selected',len(selected_columns),'column(s)')
    # st.write('### Colonnes à afficher', selected_cols)

# Show summary
st.subheader('5. Afficher les statistiques descriptives du dataset')
if st.button('Show summary'):
    st.write(df.describe().T)
if st.button('Show describe'):
    st.write(df.describe())

# Show Shape
st.subheader('6. La shape du dataset, par lignes et par colonnes')
shape_type = st.radio('Shapes dataset :',('Lignes','Colonnes','Tous'))
if shape_type == 'Lignes':
    st.text('Nombre de lignes')
    st.write(df.shape[0])
elif shape_type == 'Colonnes':
    st.text('Nombre de colonnes')
    st.write(df.shape[1])
elif shape_type == 'Tous':
    st.text('Tous')
    st.write(df.shape)
else:
    st.write(df.shape())

st.title('Data Visualization')

st.subheader('7. Afficher plusieurs type de graphique dans une partie visualisation avec notamment :')

st.subheader('7.1. Une heatmap des corrélations avec Matplotlib et Seaborn (avec les valeurs annotés)')

# Seaborn Heatmap
if st.button('Show heatmap'):
    dfHeatmap = sns.heatmap(df.corr(), annot=True)
    dfHeatmap.set_title('Heatmap')
    st.write(dfHeatmap)
    st.pyplot()

# Graph plot
st.subheader('7.2. Un graphique en barres afin de visualiser la taille du dataset par caractéristiques (on pourra notamment grouper les données afin d’avoir des graphiques plus précis)')
if st.button('Show '):
    st.write('graph plot')

if st.button('Merci :)'):
    st.balloons()
