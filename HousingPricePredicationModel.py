import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error, r2_score


def USA_HousingPricePredicationModel(avgIncome, avgHouseAge, avgNumOfRooms, areaPopulation):

  """
    Arguments: 
    - Avg. Area Income
    - Avg. Area House Age
    - Avg. Area Number of Rooms
    - Area Population
  """

  df = pd.read_csv('USA_Housing.csv')

  X = df.drop(['Address', 'Price', 'Avg. Area Number of Bedrooms'], axis=1)
  y = df['Price']

  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

  le = LinearRegression()
  le.fit(X_train, y_train)

  # y_train_predict = le.predict(X_train)
  # y_test_predict = le.predict(X_test)

  # print(f">>> Accuracy Score")
  # r2_train = r2_score(y_train, y_train_predict)
  # r2_test = r2_score(y_test, y_test_predict)
  # print(f"Train R2 Score: {r2_train}")
  # print(f"Test R2 Score: {r2_test}")

  # adjecent_r2_train = 1 - (1-r2_train)*(len(y_train)-1)/(len(y_train)-X_train.shape[1]-1)
  # adjecent_r2_test = 1 - (1-r2_test)*(len(y_test)-1)/(len(y_test)-X_test.shape[1]-1)
  # print(f"Train Adjusted R2 Score: {adjecent_r2_train}")
  # print(f"Test Adjusted R2 Score: {adjecent_r2_test}")

  # sns.scatterplot(x=y_test, y=y_test_predict)
  # sns.lineplot(x=y_test, y=y_test, color='red')
  # plt.xlabel('Actual Price')
  # plt.ylabel('Predicted Price')
  # plt.title('Actual vs. Predicted Prices')
  # plt.show()

  data = pd.DataFrame({"Avg. Area Income": [avgIncome], 'Avg. Area House Age': [avgHouseAge], 'Avg. Area Number of Rooms': [avgNumOfRooms], 'Area Population': [areaPopulation]})
  return le.predict(data)[0]


# >> Test
# print(USA_HousingPricePredicationModel(66500, 5, 5, 27000))