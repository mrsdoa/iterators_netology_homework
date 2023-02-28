# 1.
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
#         self.cursor = -1
        self.outer_list_cursor = 0 #внешний основной
        self.inner_list_cursor = 1 #вложенный
        return self

    def __next__(self):
        while self.outer_list_cursor <= len(self.list_of_list):
            for item in self.list_of_list:
                self.outer_list_cursor += 1
                self.inner_list_cursor = 0
                for inner_item in item:
                    self.inner_list_cursor += 1
                #self.list_of_list.pop(0)
        StopIteration
        return self.list_of_list[self.outer_list_cursor][self.inner_list_cursor]
    
#         if self.cursor is len(self.list_of_list):
#             raise StopIteration
#         else:
#             self.cursor += 1
#             return iter(self.list_of_list[self.cursor])

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    new_hw = FlatIterator([['a', 'b', 'c'], ['d', 'e', 'f', 'h', False], [1, 2, None], ])
    for row in new_hw:
        for x in row:
            print(x)
    test_1()

# 2.
import types
from collections.abc import Iterable


def flat_generator(list_of_lists, ignore_types=(str, bytes)):
    for x in list_of_lists:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from x
        else:
            yield

    # for row in iterables:
    #     for i in row:
    #         yield i



def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    list_of_lists = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]
    for x in flat_generator(list_of_lists):
        print(x)
