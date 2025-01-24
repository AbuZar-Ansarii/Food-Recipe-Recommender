import streamlit as st
import pandas as pd
import pickle
import joblib

df = pickle.load(open('df_recipe.pkl','rb'))
st.title("RECIPE WEB/APP")


lst_name = pickle.load(open('rec_name.pkl','rb'))
matching = joblib.load('matching_compressed.pkl')

recipe_name = st.selectbox("Select Food",lst_name)

def recipe_matcher(rec):
    index_of_recipe = df[df["name"] == rec].index[0]
    close_distance = matching[index_of_recipe]
    lst_of_recipe = sorted(list(enumerate(close_distance)), reverse=True, key=lambda x: x[1])[1:8]

    return [df.name.iloc[i[0]] for i in lst_of_recipe]

def recipe_food(food):
    index_of_recipe = df[df["name"]==food].index[0]
    ingredients_names = df["ingredients_name"][index_of_recipe]
    return ingredients_names

def cus_type(cus):
    index_of_recipe = df[df["name"] == cus].index[0]
    cuisine_type = df["cuisine"][index_of_recipe]
    return cuisine_type
def diet_t(die):
    index_of_recipe = df[df["name"] == die].index[0]
    diet_type = df["diet"][index_of_recipe]
    return diet_type

def curs_ty(cur):
    index_of_recipe = df[df["name"] == cur].index[0]
    course = df["course"][index_of_recipe]
    return course
def instruction(instru):
    index_of_recipe = df[df["name"] == instru].index[0]
    guide = df["instructions"][index_of_recipe]
    return guide

def img_url(img):
    index_of_recipe = df[df["name"] == img].index[0]
    url = df["image_url"][index_of_recipe]
    return url

image_url = img_url(recipe_name)


# action after button clicked

if st.button('click'):
    st.image(image_url,use_container_width=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.header(f"CUISINE \n{cus_type(recipe_name)}")
    with col2:
        st.header(f"COURSE \n{curs_ty(recipe_name)}")
    with col3:
        st.header(f"DIET \n{diet_t(recipe_name)}")

    st.header(f"INGREDIENTS \n{recipe_food(recipe_name)}")
    st.header(f"lET'S COOK IT \n{instruction(recipe_name)}")
    st.header(f"RECOMMENDATION FOR  \n{recipe_name}")
    recommendations = recipe_matcher(recipe_name)
    for rec_recipe in recommendations:
        st.subheader(rec_recipe)

        i_url = img_url(rec_recipe)
        st.image(i_url, width=400)

