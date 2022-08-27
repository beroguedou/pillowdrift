import os, signal
import argparse
from flask import Flask
from pillowdrift.utils.load import load_config, load_data_from_csv
from pillowdrift.utils.app_utils import create_app



ml_reference_datapath = "/Users/berangerguedou/projects/pillowdrift/data/sample_reference.csv"
ml_current_datapath = "/Users/berangerguedou/projects/pillowdrift/data/sample_current.csv"
system_datapath = "/Users/berangerguedou/projects/pillowdrift/data/system.csv"
config_path = "/Users/berangerguedou/projects/pillowdrift/config.yaml"
host = "127.0.0.1"
port = 5000

# Load config
config = load_config(config_path)
# Load system data
system_data, system_columns = load_data_from_csv(system_datapath, config)
# Load ml data
ml_reference_data, _ = load_data_from_csv(ml_reference_datapath, config)
ml_current_data, columns = load_data_from_csv(ml_current_datapath, config)

app = Flask(__name__)
# Create the app with the arguments
create_app(app, ml_reference_datapath, ml_current_datapath, 
           system_datapath, config_path, config, system_data, 
           system_columns, ml_reference_data, ml_current_data,
           columns)




if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)