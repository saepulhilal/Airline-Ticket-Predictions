# Airline Ticket Predictions

## Objective

This program was created to analyze flight booking data obtained from the Ease My Trip website and perform various statistical hypothesis tests to obtain meaningful information. The KNeighborsRegressor, SVR, DecisionTreeRegressor, RandomForestRegressor, and GradientBoostingRegressor models will be used to train the dataset and predict flight ticket prices. Ease My Trip is an online platform for booking flight tickets and is therefore the platform used by prospective passengers to purchase tickets. The results of this analysis will be highly beneficial for passengers.

---

## Conclusion


- The dataset consists of 300,153 entries and 11 columns, including attributes such as airline, flight, source_city, departure_time, stops, arrival_time, destination_city, type, duration, days_left, and price. A sample of 50,000 entries was then taken.

- There are no missing values or duplicate data in any column of the dataset.

- The dataset was then split into a training dataset of 40,000 entries and a testing dataset of 10,000 entries.

- Then, several columns were selected as features in the training data. Feature selection was performed using Pearson, Kendall, Cardinality, and Multicolinear tests. After testing, the selected columns were airline, source_city, departure_time, stops, arrival_time, destination_city, type, duration, and days_left.

- Next is the machine learning process by testing the features with the target using the KNeighborsRegressor, SVR, DecisionTreeRegressor, RandomForestRegressor, and GradientBoostingRegressor models. The results of the testing show that the RandomForestRegressor column has the best r2 score compared to the others. Therefore, RandomForestRegressor is selected as the model for predicting airplane ticket prices.

- The RandomForestRegressor model performs well in predicting airplane ticket prices, with satisfactory results for MAE, MSE, RMSE, MAPE, and R2.

- The days_left column has the greatest influence among all features, making it the most dominant feature in making predictions.

---

To see the deployment results, visit [HuggingFace](https://huggingface.co/spaces/saepulhilal/milestone2)
