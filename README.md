# End-to-End-MLOps-Training-for-Insurance-Claims

- `data/`:
   - `insurance.csv/`: This CSV file contains the data for the MLOps project. This data was taken from the Kaggle and due to the cost efficiency, the study uses a subset of insurance data. 

- `environment_setup/`:
    - `cloud-environment.json`: This JSON file is the Infrastructure as a Code for all the necessary resources for the MLOps Lifecycle. 
    - `iac-create-environment-pipeline-arm.yml`: The YAML file contains all the resources and environment names as variable groups and values which will be used to connect and authenticate the resources using Azure Agents in the Continuous Integration Pipeline. 

- `package_requirement/`:
    - `install_requirements.sh`: This bash script will read the requirements.txt and install all the packages. 
    - `requirements.txt`: This text file contains all the versions of the packages. 


- `training/`:
    - `conda_dependencies.yml`: The YAML file specifying the Conda environment dependencies required for the project.
    - `parameters.json`: The JSON file containing parameters for the model.
    - `train.py`: Python script for train_test_split, train the model and evaluation setup for the machine learning model.
    - `train_aml.py`: Python script for training the machine learning model using Azure Machine Learning.
    - `train_insurance.runconfig`: This file is a configuration script for Azure Machine Learning experiments, defining compute resources, environment settings, and data references.
    - `train_test.py`: Python scripts for running unit tests in the DevOps Continuous Integration Pipeline.
