import os
import sys
from Configurations import ConfigReader

# The following function get the Input file location along with the configuration section name and keys
def read_config_get_file_location(_config_section_name, _config_key_value):
    _file_location = os.path.dirname((os.path.dirname(sys.modules[__name__].__file__))) + \
                      '\\' + (ConfigReader.readconfig(_config_section_name, _config_key_value))
    print("File Locator read config file location " + _file_location)
    return _file_location

# The following function get the Input file location
def get_file_location(_file_subdir):
    _file_location = os.path.dirname((os.path.dirname(sys.modules[__name__].__file__))) + '\\' + _file_subdir
    print("File Locator get file location " + _file_location)
    return _file_location
