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


def main():
    read_data(file_name="sequential.json", key="unordered_numbers")


if __name__ == '__main__':
    main()