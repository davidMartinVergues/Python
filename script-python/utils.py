
import pandas as pd
import json,sys,itertools
import validator,routes
from os import listdir
from os.path import isfile, join
import csv
from datetime import datetime

def parse_file_to_json(path:str) -> list:

    xl_file = pd.ExcelFile(path)

    if 'Total' in xl_file.sheet_names:
        df = pd.read_excel(path,sheet_name="Total", header=7)
    elif 'Cargabal entity description' in xl_file.sheet_names:
        df = pd.read_excel(path,sheet_name="Cargabal entity description", header=6)


    json_str_list = df.to_json(orient = 'records')
    json_list = json.loads(json_str_list)

    for item in json_list:

        if item.get('UNIT'):
            item['Entity'] = item.pop('UNIT')
            item['Name'] = item.pop('ID Securitization')
            item['Period'] = item.pop('PERIOD')
        else:
            s = item['Period']
            item['Period'] = (datetime.fromtimestamp(s/1e3)).strftime('%d/%m/%Y')
        
    return json_list


def read_all_files_to_json(path:str)-> list:

    only_xlsx_files = [join(path, f) for f in listdir(path) if isfile(join(path, f)) and f.lower().endswith('.xlsx') and not f.lower().startswith('~')]

    if len(only_xlsx_files) > 0:

        all_files_to_json= []
        data = []

        for file in only_xlsx_files :

            try:
               all_files_to_json.append(parse_file_to_json(file))
            except BaseException as err:
                print('\nsomething went wrong!\n')
                print(f'{err} \n')


        data = list(itertools.chain(*all_files_to_json))

        return data
    else:
       raise Exception('excel file not found')

def get_keys_from_JSON_LIST(data) -> set:

    '''
    
    
    '''

    my_set = set()

    for element in data:

        my_keys = element.keys()
        my_set_aux = set(my_keys)

        my_set = my_set.union(my_set_aux)

    return my_set

