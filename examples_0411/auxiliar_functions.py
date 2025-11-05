import pandas as pd

def get_range_outlier(
        q1:float, 
        q3:float, 
        IQR:float, 
        factor_value:float=1.5):

    min_value = q1 - IQR*factor_value
    max_value = q3 + IQR*factor_value

    return min_value, max_value

def check_is_outlier(value, min_value, max_value):
    
    if value > max_value or value < min_value:
        return True
    else:
        return False

def generate_df_counts(df_values, columns_name, verbose:bool=False):
    data_rows = []

    for column in df_values.columns:
        counts = df_values[column].value_counts()

        row = [column, 0, 0] # generamos una fila

        if 1 in counts.index: # preguntamos si se identificaron nulos
            row[1] = counts[1] # lo asignamos al espacio del nulos en la fila
        if 0 in counts.index: # preguntamos si se identificaron no nulos
            row[2] = counts[0] # lo asignamos al espacio de no nulos
        
        if verbose:
            print(row)
        data_rows.append(row) # la fila la agregamos a la matriz

    # usamos la matriz para generar un data frame.
    df_counts = pd.DataFrame(data=data_rows, columns=columns_name)
    return df_counts

def categorize_iqr(value):
    if value >0:
        return 1
    else:
        return 0
        