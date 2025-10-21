import os
import pandas as pd

folder_path = '/home/hexu1/Quant/data/test'
folder_path = '/home/hexu1/Quant/data/training'

for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(folder_path, filename)
        
        # if empty, delete the file
        if os.path.getsize(file_path) == 0:
            print(f'Deleting empty file: {filename}')
            os.remove(file_path)
            continue
        
        try:
            df = pd.read_csv(file_path)
            
            # if empty, delete the file
            if df.empty:
                print(f'Deleting file with no data: {filename}')
                os.remove(file_path)
                continue
            
            df['amount'] = 0
            
            df.to_csv(file_path, index=False)
            
            print(f'Updated {filename}')
        except pd.errors.EmptyDataError:
            # if no columns:, delete the file
            print(f'Deleting file with no columns: {filename}')
            os.remove(file_path)