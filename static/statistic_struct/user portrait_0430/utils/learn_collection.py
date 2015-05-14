__author__ = 'Administrator'

from _collections import deque,defaultdict
from operator import itemgetter as _itemgetter, eq as _eq
class OrderDict(dict):
    """dictionary that rember"""

    def __init__(self, *args, **kwds):
        if len(args) > 1:
            raise TypeError('expected at most 1 arguments, got %d' % len(args))
        try:
            self.__root
        except AttributeError:
            self.__root = root = []   # sentinel node
            root[:] = [root, root, None]
            self.__map = {}

        self.__update(*args, **kwds)
        pass

    def __setitem__(self, key, value, dict_setitem=dict.__setitem__):
        'od.__setitem__(i, y) <==> od[i]=y'
        if key not in self:
            root = self.__root
            last = root[0]
            last[1] = root[0] = self.__map[key] = [last, root, key]
        return dict_setitem(self, key, value)

    def __delitem__(self, key, dict_delitem=dict.__delitem__):
        'od.__delitem__(y) <==> del od[y]'

        dict_delitem(self,key)
        link_prev, link_next, _ = self.__map.pop(key)
        link_prev[1] = link_next
        link_next[0] = link_prev
        pass


class Counter(dict):
    def __init__(self, iterable=None, **kwds):
        super(Counter, self).__init__()
        self.update(iterable, **kwds)

    def __missing__(self,key):
        'The count of elements not in the Counter is zero.'
        return 0

    def most_common(self, n=None):
        """list the n most common elements and their counts from the most common
         to the least. If n is None , then list all element counts"""

        if n is None:
            return sorted(self.iteritems(), key=_itemgetter(1), reverse=True)





