def flat_generator_simple(my_list):
    for lists in my_list:
        for item in lists:
            yield item


def flat_generator_extra(my_list):
    for item in my_list:
        if isinstance(item, list):
            for element in flat_generator_extra(item):
                yield element
        else:
            yield item
