
import yaml 
import pandas as pd


def load_config(configpath):
    with open(configpath, 'r') as file:
        content = yaml.safe_load(file)
    return content


def load_data_from_csv(datapath):
    dataframe = pd.read_csv(datapath)
    #ordinal = config['model']['variables']['numerical']['ordinal']
    data = []
    columns = dataframe.columns.tolist()
    for col in columns:
        data.append(dataframe[col].values.tolist())
    return data, columns
    

def load_data_from_mysql():
    pass

def load_data_from_postgresql():
    pass