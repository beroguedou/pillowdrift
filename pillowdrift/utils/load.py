import yaml
import pandas as pd


def load_config(configpath):
    with open(configpath, "r") as file:
        content = yaml.safe_load(file)
    return content


def load_data_from_csv(datapath, config):

    dataframe = pd.read_csv(datapath)
    columns = dataframe.columns.tolist()
    date_col = config["model"]["inference date"]
    # Sort by date if there is a column date in the data.
    dataframe[date_col] = pd.to_datetime(dataframe[date_col])
    dataframe = dataframe.sort_values(by=date_col, ascending=True)
    dataframe[date_col] = dataframe[date_col].apply(lambda x: str(x))
    data = []
    for col in columns:
        data.append(dataframe[col].values.tolist())

    return data, columns


def load_data_from_mysql():
    pass


def load_data_from_postgresql():
    pass
