import json
from pprint import pprint

def get_data(file='data/BLESS_coord.json'):
    data = json.load(open(file))
    return data
    #pprint(data)
    #print(type(data))

