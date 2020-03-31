# thread connection
import logging
import logging.config
from os.path import dirname, join

# core database
# redis connection
import redis

# import setting
from setting import Setting


class Connection:

    def __init__(self):
        self.__setting = Setting()
        logs_path = join(dirname(__file__), self.__setting.load_config['log']['path'])
        logging.config.fileConfig(fname=logs_path, disable_existing_loggers=False)
        # Get the logger specified in the file
        self.logger = logging.getLogger(__name__)

    def cache_conn(self) -> object:
        """Define cache database configuration
        :return: object
        """
        _config = self.get_config
        # cache database
        return redis.StrictRedis(
            connection_pool=redis.ConnectionPool(
                host=_config['redis'][_config['env']]['host'],
                port=_config['redis'][_config['env']]['port'],
                db=_config['redis'][_config['env']]['db_cache'],
                password=_config['redis'][_config['env']]['password'])
        )

    @property
    def get_config(self):
        """Load configuration from file
        :return:
        """
        return self.__setting.load_config
