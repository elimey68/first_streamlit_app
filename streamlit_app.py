import streamlit

streamlit.title('My Parents New Healthy Diner')
streamlit.title('Breakfast Menue')
streamlit.text('Omega 3 and Bluenerry Muffines')
streamlit.text('kale, Spinach & Rocket Smoothie')


import snowflake.connector


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_row = my_cur.fetchone()
streamlit.text("the fruit list contains:")
streamlit.text(my_data_row)
