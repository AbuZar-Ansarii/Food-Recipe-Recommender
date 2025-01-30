import streamlit as st
import pandas as pd
import pickle
import joblib

# Load data
df = pickle.load(open('df_recipe.pkl', 'rb'))
lst_name = pickle.load(open('rec_name.pkl', 'rb'))

# Load cosine similarity matrix
matching = joblib.load('matching_compressed.pkl')

st.title("RECIPE WEB/APP")

# Select food from dropdown
recipe_name = st.selectbox("Select Food", lst_name)

# Function to find similar recipes
def recipe_matcher(rec):
    try:
        index_of_recipe = df[df["name"] == rec].index[0]
        close_distance = matching[index_of_recipe]
        lst_of_recipe = sorted(list(enumerate(close_distance)), reverse=True, key=lambda x: x[1])[1:10]
        return [df.iloc[i[0]]["name"] for i in lst_of_recipe if i[0] < len(df)]
    except (IndexError, KeyError):
        return []

# Function to get details safely
def get_detail(column_name, recipe):
    try:
        index_of_recipe = df[df["name"] == recipe].index[0]
        return df.at[index_of_recipe, column_name]
    except (IndexError, KeyError):
        return "N/A"

# Action after button click
if st.button('Click to Get Recipe'):
    image_url = get_detail("image_url", recipe_name)
    if image_url:
        st.image(image_url, use_column_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header(f"CUISINE\n{get_detail('cuisine', recipe_name)}")
    with col2:
        st.header(f"COURSE\n{get_detail('course', recipe_name)}")
    with col3:
        st.header(f"DIET\n{get_detail('diet', recipe_name)}")

    st.header(f"INGREDIENTS\n{get_detail('ingredients_name', recipe_name)}")
    st.header(f"LET'S COOK IT\n{get_detail('instructions', recipe_name)}")
    st.header(f"RECOMMENDATION FOR\n{recipe_name}")

    # Get recommendations and display
    recommendations = recipe_matcher(recipe_name)
    if recommendations:
        for rec_recipe in recommendations:
            st.subheader(rec_recipe)
            i_url = get_detail("image_url", rec_recipe)
            if i_url:
                st.image(i_url, width=400)
    else:
        st.write("No recommendations available.")