import streamlit as st
import pandas as pd

st.title("Palmer's Penguins")
st.subheader("Made by James Edge")


st.write("This is an interactive app where you can manipulate data in Palmer's Penguins data set")

df = pd.read_csv("basic-streamlit-app/data/penguins.csv")

species = st.selectbox('Select a Species', df["species"].unique())
st.write(f'Penguins in {species}')
st.dataframe(df[df['species'] == species])

bodymass = st.slider("Choose a maximum body mass",
          min_value = df['body_mass_g'].min(),
          max_value = df['body_mass_g'].max())

st.write(f'Penguins with body mass under {bodymass}')
st.dataframe(df[df['body_mass_g'] <= bodymass])