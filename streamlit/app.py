import streamlit as st 
import pandas as pd
import numbers as np

st.title("AStreamlit app   ")



st.write("hhiii ")



# create a dataframe 
df =pd.DataFrame({
    'name':[1,2,3,4],
    'age':[20,30,40,50],
    'gender':['M','F','M','F'],
    'income':[50000,60000,70000,80000]

})




st.write(df)


# create a line chart 
c