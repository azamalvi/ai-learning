import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


df = pd.DataFrame({
    "age": [25, 30, None, 40],
    "salary": [50000, 60000, 70000, None],
    "city": ["Lahore", "Karachi", "Lahore", "Islamabad"]
})


# print(df)


# print("Head:", df.head())
# print("Info", df.info())
# print("describe", df.describe())
# print(df.describe())

# This will fill NaN values in numeric columns with the mean of that column

# df["age"].fillna(df["age"].mean(), inplace=True)
# df["salary"].fillna(df["salary"].mean(), inplace=True)
#
# print(df)

# print(df.fillna(df.mean(numeric_only=True)))

df_encoded = pd.get_dummies(df, columns=["city"])
scaler = StandardScaler()

df_encoded[["age", "salary"]] = scaler.fit_transform(
    df_encoded[["age", "salary"]]
)
# print(df_encoded)



# list1 = [1, 4, 7, 6, 9]
# features = np.array([
#     [25, 50000],
#     [30, 60000],
#     [35, 70000]
# ])
#
# data = np.array([10, 20, np.nan, 40])
#
# print(data)
# print(np.nanmean(data))
# print(np.isnan(data))


# print(features)
# array1 = np.array(list1)
# print("Numpy Array:", array1)
# print("Array Shape:", array1.shape)
# print("Array Data Type:", array1.dtype)
# print("Array Mean:", np.mean(array1))
# print("Array Standard Deviation:", np.std(array1))
# print("Array Sum:", np.sum(array1))
# print("Array Max:", np.max(array1))
# print("Array Min:", np.min(array1))
# reshaped_array = array1.reshape((5, 1))
# print("Reshaped Array:\n", reshaped_array)
# transposed_array = reshaped_array.T
# print("Transposed Array:\n", transposed_array)
# squared_array = array1 ** 2
# print("Squared Array:", squared_array)
# sliced_array = array1[1:4]
# print("Sliced Array (indices 1 to 3):", sliced_array)
# print("list1", list1)
# print("list1", np.sort(array1))

matrix = np.array([[1, 2, 3], [4, 5, 6]])




print(matrix[0]) # first row
print(matrix[:, 1]) # all rows `:`, column 1

def convert_to_normalized_data():
    features = np.array([50, 60, 70, 80, 90])
    mean = np.mean(features)
    std = np.std(features)
    normalized_features = (features - mean) / std
#     print(normalized_features)

convert_to_normalized_data()