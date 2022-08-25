from flask import Flask, render_template
from mool.utils.numerical import continuous_data, numerical_distribution_sampler
from mool.utils.categorical import categorical_data, categorical_distribution_sampler
from mool.utils.load import load_config, load_data_from_csv

reference_datapath = "/Users/berangerguedou/projects/mool/data/sample_reference.csv"
current_datapath = "/Users/berangerguedou/projects/mool/data/sample_current.csv"
system_datapath = "/Users/berangerguedou/projects/mool/data/system.csv"
config_path = "/Users/berangerguedou/projects/mool/config.yaml"
config = load_config(config_path)

# system data
system_data, system_columns = load_data_from_csv(system_datapath, config)
# ml data
reference_data, _ = load_data_from_csv(reference_datapath, config)
current_data, columns = load_data_from_csv(current_datapath, config)


app = Flask(__name__)

@app.route('/ml', methods=['GET'])
@app.route('/dashboard', methods=['GET'])
@app.route('/', methods=['GET'])
def ml_dashboard():
    elements = []
    # Numerical elements
    numerical_elements = continuous_data(reference_data, current_data, columns, config)
    numerical_elements = numerical_distribution_sampler(numerical_elements)
    elements.extend(numerical_elements)
    # Categorical elements
    categorical_elements = categorical_data(reference_data, current_data, columns, config)
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