import argparse
import configparser


def get_config():
    """
    This method read the default configuration file configuration.ini in the same path of the pipeline execution
    :return:
    """
    config = configparser.ConfigParser()
    config.read("configuration.ini")
    return config


def get_parameters():
    """
    This method provide a possibility to read arguments for the pipeline and combine then with the default
    configuration
    :return:
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--import_conda", help="Import Conda Recipes", action='store_true')
    parser.add_argument("-d", "--import_docker", help="Import Docker Recipes", action='store_true')

    return parser


def import_conda(config):
    """
    Import conda containers into the registry database
    :param config: Parameters for conda
    :return:  
    """
    print("Starting importing Conda packages")


def main(parameters):
    config = get_config()

    if config['DEFAULT']['VERBOSE'] == "True":
        for key in config['DEFAULT']:
            print(key + "=" + config['DEFAULT'][key])
        print(parameters)
    if parameters.import_conda is not None:
        import_conda(config)

if __name__ == "__main__":
    parameters = get_parameters().parse_args()
    main(parameters)