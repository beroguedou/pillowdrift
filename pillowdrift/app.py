import os
<<<<<<< HEAD
import pathlib

from flask import Flask, render_template
from pillowdrift.utils.numerical import continuous_data, numerical_distribution_sampler
from pillowdrift.utils.categorical import categorical_data, categorical_distribution_sampler
from pillowdrift.utils.load import load_config, load_data_from_csv


package_root_path = pathlib.Path(__file__).resolve().parent.parent
ml_reference_datapath = os.path.join(package_root_path, "data/sample_reference.csv")
ml_current_datapath = os.path.join(package_root_path, "data/sample_current.csv")
system_datapath = os.path.join(package_root_path, "data/system.csv")
config_path = os.path.join(package_root_path, "config.yaml")
config = load_config(config_path)

# system data
system_data, system_columns = load_data_from_csv(system_datapath, config)
# ml data
ml_reference_data, _ = load_data_from_csv(ml_reference_datapath, config)
ml_current_data, columns = load_data_from_csv(ml_current_datapath, config)

=======
import signal
import argparse
from flask import Flask
from pillowdrift.utils.load import load_config, load_data_from_csv
from pillowdrift.utils.app_utils import create_app
from logging import config, getLogger
from pillowdrift.utils.logging_config import logging_config

config.dictConfig(logging_config)
logger = getLogger('root')

#logger.info("Informative messages from your code.")
#logger.warning("Everything works but there is something to be aware of.")
#logger.error("There's been a mistake with the process.")
#logger.critical("There is something terribly wrong and process may terminate.")

parser = argparse.ArgumentParser(
    description=' Helps to turn on the monitoring dashboards .')
parser.add_argument('--reference-datapath', type=str,
                    help='Path of the reference dataset')
parser.add_argument('--current-datapath', type=str,
                    help='Path of the current dataset')
parser.add_argument('--service-datapath', type=str,
                    help='Path of the service metrics dataset')
parser.add_argument('--configpath', type=str, help='Path of the yaml config.')
parser.add_argument('--host', type=str, default='127.0.0.1',
                    help='IP address of the host to deploy the dashboard')
parser.add_argument('--port', type=str, default='5000',
                    help='Port for the dashboard')

args = parser.parse_args()
reference_datapath = args.reference_datapath
current_datapath = args.current_datapath
service_datapath = args.service_datapath
configpath = args.configpath
host = args.host
port = args.port

# Load config
logger.info('Loading the configuration file ...')
config = load_config(configpath)
# Load system data
logger.info('Loading the service dataset ...')
system_data, system_columns = load_data_from_csv(service_datapath, config)
# Load ml data
logger.info('Loading the reference dataset ...')
reference_data, _ = load_data_from_csv(reference_datapath, config)
logger.info('Loading the current dataset ...')
current_data, columns = load_data_from_csv(current_datapath, config)
>>>>>>> 95d86f4df782d6cf036a1c2a55c3ad6e9f327c6a

logger.info('Creating the Flask app ...')
app = Flask(__name__)
# Create the app with the arguments
create_app(app, config, system_data,
           system_columns, reference_data, current_data,
           columns)

if __name__ == '__main__':
    app.run(debug=True, host=host, port=port)
