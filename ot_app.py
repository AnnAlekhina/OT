from filters import even_numb, alfa, not_none
import glob
import os
import json


def filter_app():
    filter_dict = {"even_numb": even_numb, "not_none" : not_none, "alfa": alfa}

    for config_file in glob.glob('config.json'):
        with open(config_file) as f:
            try:
                config = json.load(f)
            except json.decoder.JSONDecodeError as err:
                print(f'Ошибка файла конфигурации: {err}')
                return f'Ошибка файла конфигурации: {err}'

    for filename in glob.glob(os.path.join(config["input_path"], '*.json')):
        with open(filename) as f_read:
            try:
                work_dict = json.load(f_read)
                for el in config["filters"]:
                    work_dict = filter_dict[el](work_dict)
            except json.decoder.JSONDecodeError as err:
                print(f'некорректный данные в файле {os.path.basename(filename)} : {err}')
                continue

        with open(f'{config["output_path"]}\\{os.path.basename(filename)}', 'w') as f:
            json.dump(work_dict, f)


filter_app()
