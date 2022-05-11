import json
 
with  open('sources.json') as f: 
	data = json.load(f)

for animal in data:
	del data[animal]["Animal"]
	for key,value in data[animal].items():
		if value == "":
			value = None
		data[animal][key] = {"value": value,"source":None}


with open('sources_newformat.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


with  open('foods.json') as f: 
	data = json.load(f)

for food in data:
	del data[food]["Food"]
	for key,value in list(data[food].items()):
		if value:
			data[food][key] = {"value": value,"source":None}
		else:
			del data[food][key]			


with open('foods_newformat.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
