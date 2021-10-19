import pandas as pd

def object_dtype(df):
    """
    printing the real data type of the object

    """
    
    if list(df.select_dtypes(include=['object']).columns) != [] :
    
        for column in df.select_dtypes(include=['object']).columns:

            print(column,type(df[column][0]))
    else:
        print('No complex data types :)')
        

def fix_price(df, column='price'):
    """
    fix price format from %d,%d$ --> %f

    args: 
         - dataframe contains the columns
         - column name
    """
    df[column] = df[column].str.replace(',', '').str.replace('$', '').astype(float)
    
    
def fix_date(df, column='date', format='%Y-%m-%d'):
    """
    fix date

    args: 
         - dataframe 
         - column name
         - format
    """
    
    df[column] = pd.to_datetime(df[column], format='%Y-%m-%d')
    
    
def df_shape(df):
    """
    printing the shape of the dataframe
    """
    print('the df has {} rows and {} columns'.format(df.shape[0],df.shape[1]))
    
def get_reviewer_name(id, df ,id_col='reviewer_id', name_col='reviewer_name' ):
    """
    get reviewer name by his id
    
    args: id, original_df, id_columns, name_column
    
    return: reviwer name
    """
    name = df[df[id_col] == id][:1].reset_index()
    return name[name_col][0]


def coloring(val, values_colors):
    if val not in values_colors.keys():
        return 'background-color: white'
    else:
        return 'background-color: %s' % values_colors[val]
