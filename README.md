# BangaloreHousePricePrediction
In this project i have built an end to end application which predicts the house price based on various locations in bangalore.

Libraries Used:

Matplotlib,Seaborn,Pandas,Sklearn

Based on the features the "area_type	availability	location	size	society	total_sqft	bath	balcony	 house_price" the price of the house for particular location is predicted.

Firstly various data preprocessing methods have been applied to dataset for better understanding of the features and feature importance techniques is also applied to retain the Importance features alone.

For model building i have applied trial and error methods where ensemble methods like GradientBoosting and RandomForest have given better accuracy than other models.

For furthermore Optimization of models i have used Hyperparameter Tuning which reduced overfitting of models as well.

Below are the results of R2 score for various models:
Ridge :84%
Lasso:84%
GradientBoosting:78%
RandomForest:76%

App buidling : Basic HTML and CSS is applied for the Front end.

For the backend i have used Flask and Postman for testing end to end application.

![image](https://user-images.githubusercontent.com/26068822/187892567-91bf45c1-d5d4-47f2-988e-61317ef44f45.png)

