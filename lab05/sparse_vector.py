"""
COMP 1510 202010 Lab 05
Young Kim (A01087377)
"""


def sparse_add(sparse_vector1, sparse_vector2):
    """
    """
    if sparse_vector1['length'] != sparse_vector2['length']:
        return None

    vector1 = convert_vector_dict_to_list(sparse_vector1)
    vector2 = convert_vector_dict_to_list(sparse_vector2)
    added_vector = [v1 + v2 for v1, v2 in zip(vector1, vector2)]
    convert_vector_list_to_dict(added_vector)

    return new_sparse_vector


def sparse_dot_product(sparse_vector1, sparse_vector2):
    """
    """
    if sparse_vector1['length'] != sparse_vector2['length']:
        return None

    vector1 = convert_vector_dict_to_list(sparse_vector1)
    vector2 = convert_vector_dict_to_list(sparse_vector2)

    dot_product = sum([v1 * v2 for v1, v2 in zip(vector1, vector2)])
    return dot_product


def convert_vector_dict_to_list(vector_in_dict):
    """
    """
    list_converted = [vector_in_dict[key] if key in vector_in_dict else 0
                      for key in range(vector_in_dict['length'])]
    return list_converted


def convert_vector_list_to_dict(vector_in_list):
    """
    """
    dict_converted = {'length': len(vector_in_list)}
    counter = 0
    while counter < len(vector_in_list):
        if vector_in_list[counter] != 0:
            dict_converted[counter] = vector_in_list[counter]
        counter += 1
    return dict_converted


def main():
    """
    """
    test_vec1 = {2: 5, 5: 1, 9: 1, 'length': 10}
    test_vec2 = {'length': 10, 3: 2, 7: 5, 9: 2}
    print(sparse_dot_product(test_vec1, test_vec2))
    # print(sparse_add(test_vec1, test_vec2))


if __name__ == "__main__":
    main()
