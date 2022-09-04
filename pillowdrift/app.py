import argparse
from flask import Flask
from pillowdrift.utils.load import load_config, load_data_from_csv
from pillowdrift.utils.app_utils import create_app
from logging import config, getLogger
from pillowdrift.utils.logging_config import logging_config

config.dictConfig(logging_config)
logger = getLogger("root")


parser = argparse.ArgumentParser(
    description=" Helps to turn on the monitoring dashboards ."
)
parser.add_argument(
    "--reference-datapath", type=str, help="Path of the reference dataset"
)
parser.add_argument("--current-datapath", type=str, help="Path of the current dataset")
parser.add_argument(
    "--service-datapath", type=str, help="Path of the service metrics dataset"
)
parser.add_argument("--configpath", type=str, help="Path of the yaml config.")
parser.add_argument(
    "--host",
    type=str,
    default="127.0.0.1",
    help="IP address of the host to deploy the dashboard",
)
parser.add_argument("--port", type=str, default="5000", help="Port for the dashboard")

args = parser.parse_args()
reference_datapath = args.reference_datapath
current_datapath = args.current_datapath
service_datapath = args.service_datapath
configpath = args.configpath
host = args.host
port = args.port

# Load config
logger.info("Loading the configuration file ...")
config = load_config(configpath)
# Load system data
logger.info("Loading the service dataset ...")
system_data, system_columns = load_data_from_csv(service_datapath, config)
# Load ml data
logger.info("Loading the reference dataset ...")
reference_data, _ = load_data_from_csv(reference_datapath, config)
logger.info("Loading the current dataset ...")
current_data, columns = load_data_from_csv(current_datapath, config)

logger.info("Creating the Flask app ...")
app = Flask(__name__)
# Create the app with the arguments
create_app(
    app,
    config,
    system_data,
    system_columns,
    reference_data,
    current_data,
    columns,
)

if __name__ == "__main__":
    app.run(debug=True, host=host, port=port)
