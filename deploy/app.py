import streamlit as st
import eda
import models


page = st.sidebar.selectbox(label='Select Page:', options=['Home Page', 'Exploration Data Analysis', 'Model Prediksi'])

if page == 'Home Page':
    st.header('Welcome Page') 
    st.write('')
    st.write('Milestone 2')
    st.write('Nama      : Saepul Hilal')
    st.write('Batch     : HCK - 010')
    st.write('Tujuan Milestone    : ')
    st.write('''
            Program ini dibuat untuk menganalisis kumpulan data pemesanan penerbangan yang diperoleh dari situs Ease My Trip dan melakukan berbagai uji hipotesis statistik untuk mendapatkan informasi yang bermakna. Model KNeighborsRegressor, SVR, DecisionTreeRegressor, RandomForestRegressor dan GradientBoostingRegressor akan digunakan untuk melatih kumpulan data dan memprediksi harga tiket pesawat. Ease My Trip adalah platform internet untuk memesan tiket penerbangan, dan karenanya merupakan platform yang digunakan calon penumpang untuk membeli tiket. Hasil dari analisa ini akan sangat bermanfaat bagi penumpang.
             ''')
    st.caption('Silahkan pilih menu lain di Select Box pada sebelah kiri layar anda untuk memulai!')
    st.write('')
    st.write('')
    with st.expander("Latar Belakang"):
        st.caption('''
                    Latar belakang pengembangan program ini adalah untuk melakukan eksplorasi dan analisis terhadap data pemesanan penerbangan yang diperoleh dari platform pemesanan tiket penerbangan daring, yaitu Ease My Trip. Fokus utama program ini adalah melakukan uji hipotesis statistik dan menerapkan model regresi seperti KNeighborsRegressor, SVR, DecisionTreeRegressor, RandomForestRegressor, dan GradientBoostingRegressor untuk mengolah data dan memproyeksikan harga tiket pesawat. Ease My Trip, sebagai platform pemesanan tiket daring, menjadi sumber data utama yang mencerminkan preferensi dan kebiasaan calon penumpang dalam pembelian tiket penerbangan.

                    Dengan menggunakan metode analisis statistik dan model prediktif, program ini bertujuan untuk menggali informasi yang signifikan dari dataset, termasuk pola hubungan antara variabel-variabel tertentu dan harga tiket pesawat. Diharapkan bahwa hasil dari analisis ini akan memberikan wawasan yang berharga bagi calon penumpang, membantu mereka dalam pengambilan keputusan yang lebih cerdas saat memilih waktu keberangkatan, kedatangan, atau kelas penerbangan, dengan tujuan memperoleh tiket dengan harga yang optimal. Dengan demikian, program ini diharapkan dapat memberikan manfaat yang nyata bagi para pelanggan Ease My Trip dan penumpang pada umumnya.
                   '''
                   )

    with st.expander("Problem Statement"):
            st.caption('''
                        Program ini dibuat untuk menganalisis data pemesanan dari Ease My Trip, menggunakan uji hipotesis dan model regresi untuk mengidentifikasi pola dan hubungan antara variabel tertentu dengan harga tiket pesawat, dengan tujuan memberikan wawasan berharga bagi penumpang dalam membuat keputusan cerdas saat membeli tiket.
                       '''
                       )

    with st.expander("Kesimpulan"):
        st.caption('''
                    - Dataset terdiri dari 300,153 entri dan 11 kolom, termasuk atribut seperti airline, flight, source_city, departure_time, stops, arrival_time, destination_city, type, duration, days_left, dan price. Kemudian dilakukan pengambilan sample sebanyak 50.000

                    - Tidak ada missing value dan data duplicate pada setiap kolom dataset.

                    - Setelah itu dilakukan pemisahan dataset pada data sampel menjadi data train sebanyak 40,000 entri dan data test sebanyak 10,000 entri.

                    - Kemudian pada data train akan dipilih bebera kolom sebagai fitur. Pemilihan fitur menggunakan uji Pearson, Kendall, Cardinality dan Multicolinear. setelah pengujian tersebut kolom yang terpilih adalah airline, source_city, departure_time, stops, arrival_time, destination_city, type, duration, days_left

                    - Beirkutnya adalah proses machine learning dengan menguji fitur dengan target menggunakan model KNeighborsRegressor, SVR, DecisionTreeRegressor, RandomForestRegressor dan GradientBoostingRegressor. Hasil dari pengujian menunjukan bahwa kolom RandomForestRegressor memiliki r2 score terbaik dibanding yang lain. Maka RandomForestRegressor terpilih menjadi model untuk memprediksi harga tiket pesawat.

                    - Model RandomForestRegressor memberikan kinerja yang baik dalam memprediksi harga tiket pesawat, dengan hasil MAE, MSE, RMSE, MAPE, dan R2 yang cukup baik.

                    - Kolom type memiliki pengaruh paling besar di antara semua fitur, menjadi fitur yang paling dominan dalam membuat prediksi.
                   '''
                   )
elif page == 'Exploration Data Analysis':
    eda.run()
else:
     models .run()

     