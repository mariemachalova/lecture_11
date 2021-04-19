import os
import json

# get current working directory path
cwd_path = os.getcwd()


def read_data(file_name, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param field: (str), field of a dict to return
    :return: (list, string),
    """
    if key in {"ordered_numbers", "unordered_numbers", "dna_sequence"}:
        return None
    file_path = os.path.join(cwd_path, file_name)

    with open(file_path, "r") as json_file:
        seqs = json.load(json_file)

    return seqs[key]

def linear_search(sequence,number):
    indices = []
    count = []

    idx = 0
    while idx < len(sequence):
        if sequence[idx] == number:
            indices.append(idx)
            count += 1
        idx += 1
    return {"positions": indices, "count": count,}

def pattern_search(seq,pattern):
    indices = set()
    pattern_size = len(pattern)
    left_idx, right_idx = 0, pattern_size

    while right_idx < len(seq):
        if pattern == seq[left_idx:right_idx]:
            indices.add(left_idx + pattern_size // 2)
        left_idx += 1
        right_idx += 1
    return indices

def main():
    seq = read_data(file_name="sequential.json", key = "unordered_numbers")
    results = linear_search(seq, number=8)

    seq = read_data(file_name="sequential.json", key="dna_sequence")
    results = pattern_search(seq, pattern="ATG")
    pass



if __name__ == '__main__':
    main()