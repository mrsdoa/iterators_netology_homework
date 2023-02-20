
class HW():

    def __init__(self):     # экземпляр класса
        pass

    def __iter__(self):
        self.nested_list = [
            ['a', 'b', 'c'],
            ['d', 'e', 'f', 'h', False],
            [1, 2, None],
        ]
        self.cursor = 0
        return self

    def __next__(self):
        self.cursor += 1
        if len(self.nested_list):
            for item in self.nested_list:
                for inner_item in item:
                    print(inner_item)
            raise StopIteration

if __name__ == "__main__":
    new_hw = HW()
    for item in new_hw:
        print(item)
