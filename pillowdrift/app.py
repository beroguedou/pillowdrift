import os
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


app = Flask(__name__)

@app.route('/ml', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
@app.route('/', methods=['GET'])
def ml_dashboard():
    elements = []
    # Numerical elements
    numerical_elements = continuous_data(ml_reference_data, ml_current_data, columns, config)
    numerical_elements = numerical_distribution_sampler(numerical_elements)
    elements.extend(numerical_elements)
    # Categorical elements
    categorical_elements = categorical_data(ml_reference_data, ml_current_data, columns, config)
    categorical_elements = categorical_distribution_sampler(categorical_elements)
    elements.extend(categorical_elements)

    return render_template('ml_dashboard.html', elements=elements)

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/system', methods=['GET'])
def system_monitoring():
    
    system_data_map = {}
    for col, element in zip(system_columns, system_data):
        system_data_map[col] = element
    
    qps_col = config['service']['requests per second']
    date_col = config['model']['inference date']
    qps = system_data_map[qps_col]
    dates = system_data_map[date_col]
    
    return render_template('system_monitoring.html', labels=dates, values=qps)

if __name__ == '__main__':
    app.run(debug=True)