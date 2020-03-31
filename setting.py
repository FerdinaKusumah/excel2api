import os

import yaml


class Setting:

    def __init__(self, current_pah: str = os.getcwd()):
        self.__file_path = "{}/conf/env.yml".format(current_pah)

    @property
    def load_config(self) -> dict:
        """Load config from file yml to json
        :return: dict
        """
        with open(self.__file_path, 'r') as stream:
            return yaml.safe_load(stream)
