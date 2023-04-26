# Energy Efficiency Enhancement 
Enhancing electrical device efficiency
author: Taha Imtiaz


<h1>Reading Data</h1>

The first cell reads a dataset from a CSV file named dataset.csv using Pandas. It also includes an error handling mechanism in case the file is not found.<h1>Data Preprocessing</h1>

The second cell generates random input power consumption and working hours for each data point in the dataset. Then, it calculates the output power and efficiency, and creates two new columns in the dataset for these values.

The third cell drops any row that contains NaN or infinite values, and replaces them with np.nan.

The fourth cell computes the enhanced efficiency for each data point and creates a new column in the dataset for this value.

The fifth cell applies a correction to the efficiency values based on the enhanced efficiency values. If the enhanced efficiency is greater than the efficiency, it subtracts the absolute value of the difference from the efficiency; if the enhanced efficiency is less than the efficiency, it adds the absolute value of the difference to the efficiency; otherwise, it keeps the efficiency unchanged.
<h1>Machine Learning<h1/>

The sixth cell splits the data into training and test sets, and fits a Gradient Boosting Regressor model to predict the efficiency.

The seventh cell uses hierarchical clustering to group the data points based on their minimum and maximum consumption values. It then visualizes the resulting dendrogram.

The eighth cell repeats the machine learning process, but this time predicts the enhanced efficiency using the same features as before.
<h1>Conclusion<h1/>

This notebook demonstrates how to preprocess data, correct errors, and apply machine learning to predict energy efficiency using Gradient Boosting Regressor. It also shows how to use hierarchical clustering to analyze the data's structure.
