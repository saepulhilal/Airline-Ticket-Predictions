# Airline Ticket Predictions

## Tujuan

Program ini dibuat untuk menganalisis kumpulan data pemesanan penerbangan yang diperoleh dari situs Ease My Trip dan melakukan berbagai uji hipotesis statistik untuk mendapatkan informasi yang bermakna. Model KNeighborsRegressor, SVR, DecisionTreeRegressor, RandomForestRegressor dan GradientBoostingRegressor akan digunakan untuk melatih kumpulan data dan memprediksi harga tiket pesawat. Ease My Trip adalah platform internet untuk memesan tiket penerbangan, dan karenanya merupakan platform yang digunakan calon penumpang untuk membeli tiket. Hasil dari analisa ini akan sangat bermanfaat bagi penumpang.

---

## Kesimpulan


- Dataset terdiri dari 300,153 entri dan 11 kolom, termasuk atribut seperti airline, flight, source_city, departure_time, stops, arrival_time, destination_city, type, duration, days_left, dan price. Kemudian dilakukan pengambilan sample sebanyak 50.000

- Tidak ada missing value dan data duplicate pada setiap kolom dataset.

- Setelah itu dilakukan pemisahan dataset pada data sampel menjadi data train sebanyak 40,000 entri dan data test sebanyak 10,000 entri.

- Kemudian pada data train akan dipilih bebera kolom sebagai fitur. Pemilihan fitur menggunakan uji Pearson, Kendall, Cardinality dan Multicolinear. setelah pengujian tersebut kolom yang terpilih adalah airline, source_city, departure_time, stops, arrival_time, destination_city, type, duration, days_left

- Beirkutnya adalah proses machine learning dengan menguji fitur dengan target menggunakan model KNeighborsRegressor, SVR, DecisionTreeRegressor, RandomForestRegressor dan GradientBoostingRegressor. Hasil dari pengujian menunjukan bahwa kolom RandomForestRegressor memiliki r2 score terbaik dibanding yang lain. Maka RandomForestRegressor terpilih menjadi model untuk memprediksi harga tiket pesawat.

- Model RandomForestRegressor memberikan kinerja yang baik dalam memprediksi harga tiket pesawat, dengan hasil MAE, MSE, RMSE, MAPE, dan R2 yang cukup baik.

- Kolom days_left memiliki pengaruh paling besar di antara semua fitur, menjadi fitur yang paling dominan dalam membuat prediksi.


---

Untuk melihat hasil deployment bisa dilihat pada [HuggingFace](https://huggingface.co/spaces/saepulhilal/milestone2)
