#!/usr/bin/env python
# coding: utf-8

# # Task 1 

# ## Q1]

# In[ ]:


#Q1] def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here

 #   return df


# In[2]:


import pandas as pd


# In[6]:


def generate_car_matrix(df)->pd.DataFrame:
        
    # Get unique 'id_1' and 'id_2' values
    id_1_values = df['id_1'].unique()
    id_2_values = df['id_2'].unique()

    # Create an empty DataFrame with 'id_1' as index and 'id_2' as columns
    car_matrix = df.pivot(index='id_1', columns='id_2', values='car')
  
    car_matrix = car_matrix.fillna(0).astype(int)
   
    return car_matrix
df = pd.read_csv('dataset-1.csv')
car_matrix = generate_car_matrix(df)

print(car_matrix.head())


# ## Q2]

# In[ ]:


# def get_type_count(df)->dict:
#     """
#     Categorizes 'car' values into types and returns a dictionary of counts.

#     Args:
#         df (pandas.DataFrame)

#     Returns:
#         dict: A dictionary with car types as keys and their counts as values.
#     """
#     # Write your logic here

#     return dict()


# In[6]:


def get_type_count(df)->dict:
    
    df['car_type'] = pd.cut(df['car'], bins=[float('-inf'), 15, 25, float('inf')],  labels=['low', 'medium', 'high'], right=False)

    # Count occurrences of each 'car_type'
    car_type_counts = df['car_type'].value_counts().to_dict()

     # Sort the dictionary alphabetically based on keys
    sorted_car_type_counts = dict(sorted(car_type_counts.items()))

    return sorted_car_type_counts

df = pd.read_csv('dataset-1.csv')
car_type = get_type_count(df)

print(car_type)


# ## Q3]

# In[ ]:


# Q3]def get_bus_indexes(df)->list:
#     """
#     Returns the indexes where the 'bus' values are greater than twice the mean.

#     Args:
#         df (pandas.DataFrame)

#     Returns:
#         list: List of indexes where 'bus' values exceed twice the mean.
#     """
#     # Write your logic here

#     return list()


# In[8]:


def get_bus_indexes(df)->list:
     # Calculate the mean of 'bus' values
    bus_mean = df['bus'].mean()

    # Find indexes where 'bus' values are greater than twice the mean
    high_bus_indexes = df[df['bus'] > 2 * bus_mean].index.tolist()

    return high_bus_indexes

df = pd.read_csv('dataset-1.csv')
bus_indices = get_bus_indexes(df)

print(bus_indices)


# ## Q4]

# In[ ]:


# Q4]def filter_routes(df)->list:
#     """
#     Filters and returns routes with average 'truck' values greater than 7.

#     Args:
#         df (pandas.DataFrame)

#     Returns:
#         list: List of route names with average 'truck' values greater than 7.
#     """
#     # Write your logic here

#     return list()


# In[9]:


def filter_routes(df)->list:
    route_truck_means = df.groupby('route')['truck'].mean()
    
    # Filter routes where the average 'truck' value is greater than 7
    selected_routes = route_truck_means[route_truck_means > 7].index.tolist()
  
    return selected_routes
    
df = pd.read_csv('dataset-1.csv')
routes= filter_routes(df)
print(routes)


# ## Q5]

# In[ ]:


# def multiply_matrix(matrix)->pd.DataFrame:
#     """
#     Multiplies matrix values with custom conditions.

#     Args:
#         matrix (pandas.DataFrame)

#     Returns:
#         pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
#     """
#     # Write your logic here

#     return matrix


# In[31]:


import pandas as pd

def multiply_matrix(input_matrix):
   
    # Create a deep copy of the input matrix to avoid modifying the original matrix
    modified_matrix = input_matrix.copy()

    # Apply the specified logic to modify values
    modified_matrix[modified_matrix > 20] *= 0.75
    modified_matrix[modified_matrix <= 20] *= 1.25

    # Round values to 1 decimal place
    modified_matrix = modified_matrix.round(1)

    return modified_matrix


df = pd.read_csv('dataset-1.csv')
car_matrix = generate_car_matrix(df)

# Modify the matrix using the function
modified_result = multiply_matrix(car_matrix)

print("Original Matrix:")
# print(car_matrix.head() )

print("\nModified Matrix:")
print(modified_result.head())


# ## Q6]

# In[ ]:


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()


# In[ ]:





# In[ ]:




