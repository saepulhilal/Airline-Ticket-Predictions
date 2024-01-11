import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image




#membuat function untuk nantinya dipanggil di app.py
def run():
    st.title('Welcome to Explaration Data Analysis')
#Memanggil data csv 
    df= pd.read_csv(r"data_10_pertama.csv")
#menampilakn 5 data teratas
    st.header('Data Flight Price Prediction')
    st.dataframe(df)

    st.header('Harga Tiket Berdasarkan Maskapai')
    image = Image.open('EDA1.png')
    st.image(image, caption='figure 1')
    st.markdown('_Berdasarkan visual diatas, diketahui bahwa maskapai vistara merupakan maskapai dengan harga tiket termahal disusul oleh maskapai Air India dan maskapai AirAsia adalah yang termurah_')

    st.header('Perubahan Harga Tiket Berdasarkan Waktu Keberangkatan dan Kedatangan')
    image = Image.open('EDA2.png')
    st.image(image, caption='figure 2')
    st.markdown('_Dapat diketahui bahwa harga tiket berdasarkan waktu keberangkatan dan waktu kedatangan sangat berfariasi_')



    st.header('Pengaruh Harga Tiket dengan Jumlah Hari Sebelum Keberangkatan')
    image = Image.open('EDA3.png')
    st.image(image, caption='figure 3')
    st.markdown('_Secara keselurhan rata-rata dari harga tiket ketika mendekati hari keberangkatan memiliki visual yang cenderung ke arah up trend. Untuk lebih jelas dapat dilihat langsung berdasarkan kota asal dan kota tujuan yang ingin dipilih_')

    st.header('Perubahan Harga Tiket Berdasarkan Kota Keberengkatan dan Tujuan')
    image = Image.open('EDA4.png')
    st.image(image, caption='figure 4')
    st.markdown('_Bisa dilihat dari visual diatas bahwa harganya begitu variatif. Contoh penerbangan dari kota Kolkata ke Delhi memiliki harga di sekitar 19.000 namun penerbangan dari kota Delhi ke Kolkata berkisar pada 21.000 sehingga memiliki selisih sekitar 1.100_')
    
    st.header('Perbedaan Harga Tiket antara Kelas Ekonomi dan Bisnis')
    image = Image.open('EDA5.png')
    st.image(image, caption='figure 5')
    st.markdown('_Dapat dilihat perbedaan dari harga tiket pesawat berdasarkan kelasnya untuk ekonomi memilki range harga dari 1.105 hingga 42.349 sedangkan untuk kelas bisnis dari 12.000 hingga 123.071_')


    st.header('Pengaruh Fitur Paling Besar')
    image = Image.open('EDA6.png')
    st.image(image, caption='figure 6')
    st.markdown('_Kolom type memiliki pengaruh paling besar di antara semua fitur, menjadi fitur yang paling dominan dalam membuat prediksi._')





