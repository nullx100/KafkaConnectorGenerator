# OracleCDC Kafka Connect Config Generator

This script generates a JSON configuration file for an OracleCDC Kafka Connect connector. This file is used to set up a connection to a database and continuously stream data changes from a specified table to Kafka topics.

## Usage

    Clone this repository.
    Navigate to the project directory and run python generator.py
    Follow the prompts to input the necessary parameters for your database connection and table configuration.
    Review the outputted JSON configuration file before using it to create a Kafka Connect connector in a production environment.

⚠️⚠️⚠️ WARNING: If not used properly, this script may result in overlapping topics. Review the generated configuration file thoroughly before using it in a production environment. ⚠️⚠️⚠️

## Author

Name: Santiago Aguado
GitHub: https://github.com/nullx100

## Disclaimer

This script is provided as-is and without warranty. Use at your own risk.
