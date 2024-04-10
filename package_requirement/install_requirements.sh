"""
This Bash script is used to install the required packages for the project.

The script will install the following packages:

1. Azure CLI
2. Azure ML SDK
3. The packages listed in the requirements.txt file

"""
python --version
pip install --upgrade azure-cli
pip install --upgrade azureml-sdk
pip install -r requirements.txt