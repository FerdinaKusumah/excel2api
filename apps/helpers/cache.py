import hashlib
import orjson
from functools import wraps

import pandas
from starlette import applications


def cache(ttl=None):
    def decorator(func):
        @wraps(func)
        def decorated_function(*args, **kwargs):
            __hash = '{}'.format(func.__name__)
            if args:
                __hash = '{}:{}'.format(func.__name__, ':'.join(str(doc) for doc in args[1:]))

            query_hash = hashlib.sha1(__hash.encode('utf-8')).hexdigest()

            def _is_cache_exists(q_hash):
                return not applications.conf['cache'].get(q_hash) is None

            def _get_cache_values(q_hash):
                return pandas.read_json(orjson.loads(applications.conf['cache'].get(q_hash)))

            def _set_cache_and_return_values(q_hash, data, time_to_live):
                if time_to_live is None:
                    time_to_live = applications.conf['config']['redis'][applications.conf['config']['env']]['min_ttl']

                applications.conf['cache'].set(q_hash, orjson.dumps(data), ex=time_to_live)
                return _get_cache_values(query_hash)

            if _is_cache_exists(query_hash):
                return _get_cache_values(query_hash)

            return _set_cache_and_return_values(query_hash, func(*args, **kwargs), ttl)

        return decorated_function

    return decorator
