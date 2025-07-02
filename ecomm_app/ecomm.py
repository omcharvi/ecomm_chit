import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib. pyplot as plt
import pandas as pd
import streamlit as st


def main ():
    st.title("this is app for ecomm am creating")
    st.sidebar.title("please upload file")

upload_file = st.sidebar.file_uploader ('upload your file', type= ['csv', 'xlsx'])

if upload_file is not None:
    try:
        if upload_file.name.endswith('csv'):
           data= pd.read_csv(upload_file)
        else:
            data= pd.read_excel(upload_file, engine='openpyxl') 
        st.sidebar.success("file is uploaded successfully")
        st.subheader("i am going to show you a data details")
        st.dataframe(data.head())

        st.subheader("let see some more detail in data")
        st.write("shape of the data", data.shape)
        st.write("the colum name inside data is",data.columns)
        st.write("missing value into colum", data.isnull().sum())

        st.subheader("i will show the bit of stats")
        st.write(data.describe())

    except Exception as e :
        print (e)
if __name__== "__main__":
    main()