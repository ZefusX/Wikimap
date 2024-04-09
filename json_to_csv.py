import json

def json_to_csv(json_file,csv_file):
    result=""
    with open(json_file, 'r') as f:
        data = json.load(f)
    for title,content in data.items():
        result+=str(title)
        for element in content:
            result+=","+str(element)
        result+="\n"
    with open(csv_file,'w',encoding="utf-8") as f:
        f.write(result)
    print("Fini")

json_to_csv("dico_unique.json", "dico_unique.csv")