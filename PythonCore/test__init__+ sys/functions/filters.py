def filtered_items(*args):
    sequence1 = args[0]
    sequence2 = args[1]

    not_matched = list()
    common_elements_in_all = list(set.intersection(*map(
        set, [sequence1, sequence2]
        )
    ))
    return common_elements_in_all 