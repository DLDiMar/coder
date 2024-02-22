import pandas as pd
from pandas.api.types import is_string_dtype, is_integer_dtype

def create_employee_df(employee_data, columns):
    # Create an empty dataframe with the specified columns
    df = pd.DataFrame(columns=columns)
    
    # Iterate over the input data and populate the dataframe
    for row in employee_data:
        for col, value in zip(columns, row):
            if is_string_dtype(df[col].dtype):
                if not isinstance(value, str):
                    raise ValueError(f"Invalid data type for column '{col}': expected string, got {type(value)}")
            elif is_integer_dtype(df[col].dtype):
                if not isinstance(value, int):
                    raise ValueError(f"Invalid data type for column '{col}': expected integer, got {type(value)}")
            else:
                # Add more type checks as needed
                pass
        
        df = df.append(pd.Series(row, index=columns), ignore_index=True)
    
    # Convert datetime columns to datetime format
    for col in df.columns:
        if col.startswith('dob'):
            df[col] = pd.to_datetime(df[col])
    
    return df
    
# Define the columns
columns = ['name', 'dob', 'employee_id', 'department', 'salary']

# Define the input data as an array of arrays
employee_data = [
    ["John Smith", "2018-01-05", "E1029", "Sales", 50000],
    ["Idah Johnson", "2011-05-06", "E1090", "Marketing", 60000],
    ["Peter John-Smith", "2016-09-12", "E1049", "IT", 70000],
    ["Jane Doe", "2019-02-20", "E1102", "HR"]
]

# Create the dataframe
df = create_employee_df(employee_data, columns)
print(df)