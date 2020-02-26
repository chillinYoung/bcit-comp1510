"""
COMP 1510 202010 Lab 05
Young Kim (A01087377)
"""


def sparse_add(sparse_vector1: dict, sparse_vector2: dict) -> dict:
    """Add two vectors.

    A function that adds two vectors which are in dictionary form.

    :param sparse_vector1: a sparse vector as a dictionary
    :param sparse_vector2: a sparse vector as a dictionary
    :precondition: the sparse vectors must be given as a dictionary including
                    vector's length in key and value pair
    :postcondition: calculate addition of two sparse vectors correctly
    :return: a dictionary

    >>> test_vec1 = {2: 5, 5: 1, 9: 1, 'length': 10}
    >>> test_vec2 = {'length': 10, 3: 2, 7: 5, 9: 3}
    >>> sparse_add(test_vec1, test_vec2)
    {'length': 10, 2: 5, 3: 2, 5: 1, 7: 5, 9: 4}
    >>> test_vec1 = {'length': 2, 1: 1}
    >>> test_vec2 = {'length': 2, 1: -1}
    >>> sparse_add(test_vec1, test_vec2)
    {'length': 2}
    >>> test_vec1 = {'length': 2}
    >>> test_vec2 = {'length': 2}
    >>> sparse_add(test_vec1, test_vec2)
    {'length': 2}
    """
    if (sparse_vector1['length'] != sparse_vector2['length']):
        return None

    vector1 = convert_vector_dict_to_list(sparse_vector1)
    vector2 = convert_vector_dict_to_list(sparse_vector2)
    added_vector_in_list = [v1 + v2 for v1, v2 in zip(vector1, vector2)]

    return convert_vector_list_to_dict(added_vector_in_list)


def sparse_dot_product(sparse_vector1: dict, sparse_vector2: dict):
    """Calculate dot product of two vectors.

    A function that calculates dot product of two vectors.

    :param sparse_vector1: a sparse vector as a dictionary
    :param sparse_vector2: a sparse vector as a dictionary
    :precondition: the sparse vectors must be given as a dictionary including
                    vector's length in key and value pair
    :postcondition: calculate dot product of two sparse vectors correctly
    :return: a number (integer or float)
    """
    if sparse_vector1['length'] != sparse_vector2['length']:
        return None

    vector1 = convert_vector_dict_to_list(sparse_vector1)
    vector2 = convert_vector_dict_to_list(sparse_vector2)

    return sum([v1 * v2 for v1, v2 in zip(vector1, vector2)])


def convert_vector_dict_to_list(vector_in_dict: dict) -> list:
    """Convert a dictionary vector to a list vector.

    :param vector_in_dict: a sparse vector as a dictionary
    :precondition: the sparse vectors must be given as a dictionary including
                    vector's length in key and value pair
    :postcondition: correctly convert the given dictionary vector to a list
                    vector with tagged vector length
    :return: a list
    """
    return [vector_in_dict[key] if key in vector_in_dict else 0
            for key in range(vector_in_dict['length'])]


def convert_vector_list_to_dict(vector_in_list: list) -> dict:
    """Convert a list vector to a dictionary vector.

    :param vector_in_list: a sparse vector as a dictionary
    :precondition: the sparse vectors must be given as a list
    :postcondition: correctly convert the given list vector to a dictionary
                    vector including tag for the vector length
    :return: a dictionary
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
    Drive the Program.
    """
    test_vec1 = {2: 5, 5: 1, 9: 1, 'length': 10}
    test_vec2 = {'length': 10, 3: 2, 7: 5, 9: 3}
    print(sparse_dot_product(test_vec1, test_vec2))
    print(sparse_add(test_vec1, test_vec2))


if __name__ == "__main__":
    main()
