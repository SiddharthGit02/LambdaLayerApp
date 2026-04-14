import json
import numpy as np
import pandas as pd

def process_data():
    try:
        # 1. Generate random data using numpy (5 rows, 4 columns)
        random_data = np.random.randint(0, 100, size=(5, 4))
        
        # 2. Load it into a pandas DataFrame
        df = pd.DataFrame(random_data, columns=['A', 'B', 'C', 'D'])
        
        # 3. Perform a quick operation (calculate means of each column)
        column_means = df.mean().to_dict()
        
        # 4. Format the output locally
        result = {
            'message': 'Success! Pandas and Numpy are working locally.',
            'data_preview': df.head().to_dict(orient='records'),
            'averages': column_means
        }
        
        return result

    except Exception as e:
        return {'error': str(e)}

# Local execution block
if __name__ == "__main__":
    # Run the function
    output = process_data()
    
    # Print the result nicely to the console
    print(json.dumps(output, indent=4))