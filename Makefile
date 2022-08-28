.ONESHELL:
# Variables
PROJECT_ROOT_PATH := "/home/alka/Documents"
PATH_TO_CONFIG := "${PROJECT_ROOT_PATH}/pillowdrift/config.yaml"
PATH_TO_REFERENCE_DATASET := "${PROJECT_ROOT_PATH}/pillowdrift/data/sample_reference.csv"
PATH_TO_CURRENT_DATASET := "${PROJECT_ROOT_PATH}/pillowdrift/data/sample_current.csv"
PATH_TO_SERVICE_DATASET := "${PROJECT_ROOT_PATH}/pillowdrift/data/system.csv"
HOST_IP := "127.0.0.1"
PORT := "5000"



# Make a pre-commit
pre-commit:
	pre-commit run --all-files
# Create a conda environment named devenv
devenv:
	conda create --name devenv python=3.8.13
	conda activate devenv
	pre-commit install && \
	pre-commit autoupdate

# Start the dashboards server
pillowstart:
	pillowdrift start --configpath=${PATH_TO_CONFIG} \
					--datapath-ref=${PATH_TO_REFERENCE_DATASET} \
					--datapath-cur=${PATH_TO_CURRENT_DATASET} \
					--datapath-service=${PATH_TO_SERVICE_DATASET} \
					--host=${HOST_IP} --port=${PORT}

# Stop the dashboards server
pillowstop:
	pillowdrift stop --host=${HOST_IP} --port=${PORT}

# Unitary tests
# Integration tests
# Build docker image
# Push the docker image to a repository
