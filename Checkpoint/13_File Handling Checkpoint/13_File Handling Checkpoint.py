import numpy as np

# import the data from the csv file using np.genfromtxt
data = np.genfromtxt('Lending-Company-Saving.csv', delimiter = ',', skip_header = 1, missing_values = '', filling_values = np.nan, dtype=[('LoanID', 'i'), ('StringID', 'U20'), ('Product', 'U20'), ('CustomerGender', 'U20'), ('Location', 'U20'), ('Region', 'U20'), ('TotalPrice', 'f')])
print(data)

# Apply some statistical analysis
loan_amounts = data['TotalPrice'] # Extract the total_price column of the data
loan_amounts = loan_amounts[~np.isnan(loan_amounts)] # Remove any NaN values

min_loan = np.min(loan_amounts)
max_loan = np.max(loan_amounts)
range_loan = np.ptp(loan_amounts)
mean = np.mean(loan_amounts)
median = np.median(loan_amounts)
std_dev = np.std(loan_amounts)

# Print the results
print("Range of loan amount:", range_loan)
print("Minimum loan amount:", min_loan)
print("Maximum loan amount:", max_loan)
print("Mean loan amount:", mean)
print("Median loan amount:", median)
print("Standard deviation of loan amount:", std_dev)