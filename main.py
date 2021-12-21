from data import nested_list
from data import nested_list2
from iterator import FlatIteratorSimple
from iterator import FlatIteratorExtra
from generator import flat_generator_simple
from generator import flat_generator_extra

if __name__ == '__main__':
    for item in FlatIteratorSimple(nested_list):
        print(item)
    flat_list = [item for item in FlatIteratorSimple(nested_list)]
    print(flat_list)
    for item in FlatIteratorExtra(nested_list2):
        print(item)
    flat_list2 = [item for item in FlatIteratorExtra(nested_list2)]
    print(flat_list2)
    for item in flat_generator_simple(nested_list):
        print(item)
    for item in flat_generator_extra(nested_list2):
        print(item)
