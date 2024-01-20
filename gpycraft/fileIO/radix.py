import pandas as pd
import warnings


class radix:
    """
        # Sample DataFrame
    data = {
        'Price': [12.345, 45.678, 67.890],
        'Quantity': [100, 200, 150],
        'Amount': [1234.56, 5678.90, 7890.12]
    }

    df = pd.DataFrame(data)

    # List of numerical columns to convert from decimal to comma
    columns_to_convert = ['Price', 'Amount']
    # Create an instance of the Radix class
    radix_converter = Radix()

    # Convert specified columns to use commas for decimal values
    radix_converter.to_comma(df, column=columns_to_convert)

    # Display the modified DataFrame
    print(df)
    """
    def __init__(self):
        pass

    def to_comma(self, df, column=None):
        if column is not None:
            for col in column:
                if col in df.columns and pd.api.types.is_numeric_dtype(df[col]):
                    df[col] = df[col].apply(lambda x: f"{x:.2f}".replace('.', ','))
        else:
            warning={
                'message' : 'Attempting to convert .xlsx to a dotfile without specifiying numeric columns will result to error when converting dotfile to xlsx',
                'do':'create a list of numeric columns cols=[] '
            }
            print(f'WARNING: {warning} \n')
            
        return df
