import streamlit
import pandas


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")3
streamlit.dataframe(my_fruit_list)


streamlit.title('My Parents new Healthy Diner')
streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 and Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and ROcket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocada Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
