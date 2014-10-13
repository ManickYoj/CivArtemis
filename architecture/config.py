import ConfigParser
import os


def strToTup(item):
    """
    Utility function to parse a string item to a tuple if the
    string is in tuple form. If the item is not in tuple form,
    this function returns the original string.
    """

    if item[0] == "(" and item[-1] == ")":
        return tuple(int(x) for x in item[1:-1].split(','))
    else: return item


def loadConfig(sections=[], filename='!config.cfg'):
    c = ConfigParser.ConfigParser()
    c.readfp(open(os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)))

    if not sections:
        sections = c.sections()

    config_dict = {}
    for section in sections:
        config_dict[section.upper()] = dict(c.items(section))
        section = section.upper()

        # Parsing types
        for key in config_dict[section]:
            item = config_dict[section][key]
            item = item.upper()
            item = strToTup(item)
            config_dict[section][key] = item

    return config_dict


class Config:
    _raw_config = loadConfig()

    @staticmethod
    def get(section, item):
        section = section.upper()
        item = item.lower()
        if section in Config._raw_config and item in Config._raw_config[section]:
            return Config._raw_config[section][item]
        else:
            raise ValueError(''.join([section, ", ", item, " not found in config file."]))

print("hi")
# Testing
if __name__ == "__main__":
    print(Config._raw_config)
    print(Config.get('Graphics', 'display_size'))
