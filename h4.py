import csv
import json


def read_csv(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        decryption_dict = {row['key']: row['value'] for row in reader}
    return decryption_dict


def decrypt_string(s, decryption_dict):
    result = []
    for i in range(0, len(s), 2):
        pair = s[i:i + 2]
        if pair in decryption_dict:
            result.append(decryption_dict[pair])
        else:
            result.append(pair)
    return ' '.join(result)


def main():
    csv_file_name = input().strip()
    decryption_dict = read_csv(csv_file_name)

    decrypted_strings = {}
    index = 0
    while True:
        try:
            line = input().strip()
            if not line:
                break
            decrypted_string = decrypt_string(line, decryption_dict)
            decrypted_strings[str(index)] = decrypted_string
            index += 1
        except EOFError:
            break

    with open('tabula_rasa.json', 'w', encoding='utf-8') as json_file:
        json.dump(decrypted_strings, json_file)


if __name__ == "__main__":
    main()
