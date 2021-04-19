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

def main():
    read_data(file_name="sequential.json", key = "unordered_numbers")
    linear_search(sequence="unordered_numbers", number=8)
    pass



if __name__ == '__main__':
    main()