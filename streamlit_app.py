import streamlit
streamlit.title('My Parents New Healthy Diner')
streamlit.title('Breakfast Menue')
streamlit.text('🥣 Omega 3 and Bluenerry Muffines')
streamlit.text('🥗kale, Spinach & Rocket Smoothie')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

Import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
