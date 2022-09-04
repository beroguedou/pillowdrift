import os
import signal
from flask import render_template
from pillowdrift.utils.numerical import (
    continuous_data,
    numerical_distribution_sampler,
)
from pillowdrift.utils.categorical import (
    categorical_data,
    categorical_distribution_sampler,
)


def initialize(
    config, system_data, system_columns, reference_data, current_data, columns
):
    elements = []
    # Numerical elements
    numerical_elements = continuous_data(reference_data, current_data, columns, config)
    numerical_elements = numerical_distribution_sampler(numerical_elements)
    elements.extend(numerical_elements)
    # Categorical elements
    categorical_elements = categorical_data(
        reference_data, current_data, columns, config
    )
    categorical_elements = categorical_distribution_sampler(categorical_elements)
    elements.extend(categorical_elements)
    # Service elements
    system_data_map = {}
    for col, element in zip(system_columns, system_data):
        system_data_map[col] = element

    qps_col = config["service"]["requests per second"]
    latency_col = config["service"]["latency"]
    date_col = config["model"]["inference date"]
    qps = system_data_map[qps_col]
    latency = system_data_map[latency_col]
    dates = system_data_map[date_col]
    return elements, dates, qps, latency


def create_app(
    app,
    config,
    system_data,
    system_columns,
    reference_data,
    current_data,
    columns,
):

    # Initialization
    elements, dates, qps, latency = initialize(
        config,
        system_data,
        system_columns,
        reference_data,
        current_data,
        columns,
    )

    @app.route("/ml", methods=["GET"])
    @app.route("/dashboard", methods=["GET"])
    @app.route("/", methods=["GET"])
    def ml_dashboard():
        return render_template("ml_dashboard.html", elements=elements)

    @app.route("/about", methods=["GET"])
    def about():
        return render_template("about.html")

    @app.route("/system", methods=["GET"])
    def service_monitoring():
        return render_template(
            "service_monitoring.html", labels=dates, qps=qps, latency=latency
        )

    @app.route("/shutdown", methods=["GET"])
    def shutdown():
        os.kill(os.getpid(), signal.SIGINT)
        return "Server shutting down..."
