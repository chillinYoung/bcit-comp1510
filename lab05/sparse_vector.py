"""
COMP 1510 202010 Lab 05
Young Kim (A01087377)
"""


def sparse_add(sparse_vector1, sparse_vector2):
    """
    """
    if sparse_vector1['length'] != sparse_vector2['length']:
        return None

    vector1 = [sparse_vector1[key] if key in sparse_vector1 else 0
               for key in range(sparse_vector1['length'])]
    vector2 = [sparse_vector2[key] if key in sparse_vector2 else 0
               for key in range(sparse_vector2['length'])]
    added_vector = [v1 + v2 for v1, v2 in zip(vector1, vector2)]

    new_sparse_vector = {'length': len(added_vector)}
    counter = 0
    while counter < len(added_vector):
        if added_vector[counter] != 0:
            new_sparse_vector[counter] = added_vector[counter]
        counter += 1

    return new_sparse_vector


def sparse_dot_product(sparse_vector1, sparse_vector2):
    """
    """
    if sparse_vector1['length'] != sparse_vector2['length']:
        return None

    vector1 = [sparse_vector1[key] if key in sparse_vector1 else 0
               for key in range(sparse_vector1['length'])]
    vector2 = [sparse_vector2[key] if key in sparse_vector2 else 0
               for key in range(sparse_vector2['length'])]

    dot_product = sum([v1 * v2 for v1, v2 in zip(vector1, vector2)])
    return dot_product


def main():
    test_vec1 = {2: 5, 5: 1, 9: 1, 'length': 10}
    test_vec2 = {'length': 10, 3: 2, 7: 5, 9: 2}
    print(sparse_dot_product(test_vec1, test_vec2))
    # print(sparse_add(test_vec1, test_vec2))


if __name__ == "__main__":
    main()
