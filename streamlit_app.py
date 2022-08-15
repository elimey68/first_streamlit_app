import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.title('Breakfast Menue')
streamlit.text('🥣 Omega 3 and Bluenerry Muffines')
streamlit.text('🥗kale, Spinach & Rocket Smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
# Let's put a pick list here so they can pick the fruit they want to include 

streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])

fruit_selected=streamlit.multiselect("Pick some fruits", list(my_fruit_list_index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruit_selected]

streamlit.dataframe(fruits_to_show)
