import streamlit as st
import langchain_helper

st.title('Restaurant Name Generator')

cuisine = st.sidebar.selectbox("Pick a cuisine", ("Indian", "Portuguese", "American", "Ghanaian", "Mexican", "South Africa"))

if cuisine:
    # Ensure that cuisine is passed as a string
    response = langchain_helper.chain_function(cuisine)
    
    st.header(response['restaurant_name'])
    menu_items = response['menu'].split(",")
    st.write("**Menu Items**")
    for item in menu_items:
        st.write("-", item.strip())
