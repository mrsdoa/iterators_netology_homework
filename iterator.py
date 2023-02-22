# 1.
class HW():

    def __init__(self, nested_list):    
        self.nested_list = nested_list
        pass

    def __iter__(self):
        self.cursor = 0
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.nested_list):
            for item in self.nested_list:
                for inner_item in item:
                    print(inner_item)
            raise StopIteration

    def series_generator(self):
        new_list = []
        while self.cursor != len(self.nested_list):
            yield item
            self.cursor += 1
        for num in self.nested_list:
            new_list.append(num)
        return new_list

if __name__ == "__main__":
    new_hw = HW([['a', 'b', 'c'],['d', 'e', 'f', 'h', False],[1, 2, None],])
    for item in new_hw:
        print(item)

# flat_list = [item for item in FlatIterator(nested_list)]
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

