import json
import numpy as np
import pandas as pd

def lambda_handler(event, context):
    try:
        # 1. Generate random data using numpy (5 rows, 4 columns)
        random_data = np.random.randint(0, 100, size=(5, 4))
        
        # 2. Load it into a pandas DataFrame
        df = pd.DataFrame(random_data, columns=['A', 'B', 'C', 'D'])
        
        # 3. Perform a quick operation (calculate means of each column)
        column_means = df.mean().to_dict()
        
        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Success! Pandas and Numpy are working.',
                'data_preview': df.head().to_dict(orient='records'),
                'averages': column_means
            })
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                'error': str(e)
            })
        }