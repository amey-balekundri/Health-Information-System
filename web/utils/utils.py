import json

def json_parser(json_file):
    with open(json_file) as f:
        obj=json.load(f)
        temp=[]
        for x in obj:
            temp.append((x,x))
    return temp