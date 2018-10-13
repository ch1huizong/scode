# -*- coding:UTF-8 -*-
# 把数据转化为特定字节形式(JSON/pickle)保存在后端中

import pickle

from django.core.signing import JSONSerializer as BaseJSONSerializer


class PickleSerializer:
    """
    自定义时自己需要实现dumps和loads方法
    Simple wrapper around pickle to be used in signing.dumps and
    signing.loads.
    """
    def dumps(self, obj):
        return pickle.dumps(obj, pickle.HIGHEST_PROTOCOL)

    def loads(self, data):
        return pickle.loads(data)


JSONSerializer = BaseJSONSerializer
