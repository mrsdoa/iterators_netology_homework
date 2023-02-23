# 1.
class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        if self.cursor is len(self.list_of_list):
            raise StopIteration
        else:
            self.cursor += 1
            return iter(self.list_of_list[self.cursor])

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
def hello_world(n):
    for i in n:
        for b in i:
            yield b

for item in hello_world(n=[
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None],
        ]):
    print(item)

n = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None],
        ]
hello_world_generator = hello_world(n)

