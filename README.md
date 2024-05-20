
# Salary Data Analysis

This repository contains a simple Python script for analyzing salary data using pandas. The script reads data from two CSV files, performs basic data exploration, and calculates the mean salary for each city.

## Files

- `salaries.csv`: This file contains salary data downloaded from [Kaggle](https://www.kaggle.com/).
- `dz.csv`: This file contains additional salary data provided as part of an assignment.

## Script Overview

The script performs the following tasks:

1. Reads the `salaries.csv` file and displays the first 5 rows, basic information, and descriptive statistics.
2. Reads the `dz.csv` file and calculates the mean salary for each city.

## Usage

1. Make sure you have Python installed on your system.
2. Install the required library by running:
    ```bash
    pip install pandas
    ```
3. Place the `salaries.csv` and `dz.csv` files in the same directory as the script.
4. Run the script:
    ```bash
    python script.py
    ```

## Code

```python
import pandas as pd

# Read and explore the Kaggle salary data
kaggle_df = pd.read_csv('salaries.csv')
print(kaggle_df.head(5))
print(kaggle_df.info())
print(kaggle_df.describe())

# Read and analyze the assignment data
df = pd.read_csv('dz.csv')
print(df.groupby('City')['Salary'].mean())
```

## Requirements

- pandas

You can install the required package using:
```bash
pip install pandas
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
