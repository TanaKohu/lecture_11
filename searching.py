# balik funkcii
import os, json

# get current working directory path, vrati cestu do pracovneho adresara
cwd_path = os.getcwd()


def read_data(file_name, key):
    """
    Reads json file and returns sequential data.
    :param file_name: (str), name of json file
    :param key: (str), field of a dict to return
    :return: (list, string),
    """

    if key not in {"unordered_numbers", "ordered_numbers", "dna_sequence"}:
        return None

    # join -  metoda, ktora bezpezcne spaja retazce z vylsednej cesty, spoji cestu do aktualneho pracovneho adresara a nazov suboru
    file_path = os.path.join(cwd_path, file_name)

    # nacitanie suboru
    with open(file_path, "r") as json_file:
        sequences = json.load(json_file)

    return sequences[key]


def linear_search(file_name, number):
    positions = []
    count = 0
    i=0

    while i < len(file_name):
        if file_name[i] == number:
            positions.append(i)
            count = count + 1
        i = i + 1

    return {"positions" : positions, "count" : count}


def pattern_search(sequence, pattern):
    position = set()
    p_size = len(pattern)
    start = 0
    end = p_size

    while end < len(sequence):
        if pattern == sequence[start:end]:
            position.add(start + p_size // 2)

        start = start + 1
        end = end + 1

    return position


def main():
    file1 = read_data(file_name="sequential.json", key="unordered_numbers")
    file2 = read_data(file_name="sequential.json", key="dna_sequence")
    print(file1)
    print(linear_search(file1, number=9))
    print(pattern_search(file2, pattern="ATA"))


if __name__ == '__main__':
    main()
