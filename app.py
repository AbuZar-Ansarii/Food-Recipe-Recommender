import streamlit as st
import pandas as pd
import pickle
import joblib

# Load data
df = pickle.load(open('df_recipe.pkl', 'rb'))
lst_name = pickle.load(open('rec_name.pkl', 'rb'))

# Load cosine similarity matrix
# matching = joblib.load('matching_compressed.pkl')

st.title("RECIPE WEB/APP")

# Select food from dropdown
recipe_name = st.selectbox("Select Food", lst_name)

# Function to find similar recipes
def recipe_matcher(rec):
    try:
        index_of_recipe = df[df["name"] == rec].index[0]
        close_distance = matching[index_of_recipe]
        lst_of_recipe = sorted(list(enumerate(close_distance)), reverse=True, key=lambda x: x[1])[1:10]
        return [df.name.iloc[i[0]] for i in lst_of_recipe]
    except IndexError:
        return []

# Function to get ingredients
def recipe_food(food):
    try:
        index_of_recipe = df[df["name"] == food].index[0]
        return df["ingredients_name"][index_of_recipe]
    except IndexError:
        return "No ingredients found."

# Function to get cuisine type
def cus_type(cus):
    try:
        index_of_recipe = df[df["name"] == cus].index[0]
        return df["cuisine"][index_of_recipe]
    except IndexError:
        return "N/A"

# Function to get diet type
def diet_t(die):
    try:
        index_of_recipe = df[df["name"] == die].index[0]
        return df["diet"][index_of_recipe]
    except IndexError:
        return "N/A"

# Function to get course type
def curs_ty(cur):
    try:
        index_of_recipe = df[df["name"] == cur].index[0]
        return df["course"][index_of_recipe]
    except IndexError:
        return "N/A"

# Function to get cooking instructions
def instruction(instru):
    try:
        index_of_recipe = df[df["name"] == instru].index[0]
        return df["instructions"][index_of_recipe]
    except IndexError:
        return "Instructions not found."

# Function to get image URL
def img_url(img):
    try:
        index_of_recipe = df[df["name"] == img].index[0]
        return df["image_url"][index_of_recipe]
    except IndexError:
        return ""

# Get image URL for the selected recipe
image_url = img_url(recipe_name)

# Action after button click
if st.button('Click to Get Recipe'):
    if image_url:
        st.image(image_url, use_column_width=True)
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header(f"CUISINE\n{cus_type(recipe_name)}")
    with col2:
        st.header(f"COURSE\n{curs_ty(recipe_name)}")
    with col3:
        st.header(f"DIET\n{diet_t(recipe_name)}")

    st.header(f"INGREDIENTS\n{recipe_food(recipe_name)}")
    st.header(f"LET'S COOK IT\n{instruction(recipe_name)}")
    
    # st.header(f"RECOMMENDATION FOR\n{recipe_name}")

    # Get recommendations and display
    # recommendations = recipe_matcher(recipe_name)
    # if recommendations:
        # for rec_recipe in recommendations:
            # st.subheader(rec_recipe)
            # i_url = img_url(rec_recipe)
            # if i_url:
                # st.image(i_url, width=400)
    # else:
        # st.write("No recommendations available.")
