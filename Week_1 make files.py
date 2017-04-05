import yaml
import json

def make_yaml_file(file):
	with open('my_list.yml','w') as f:
		f.write(yaml.dump(my_list, default_flow_style = False))

def make_json_file(file):
	with open ("my_list.json", "w") as f:
		json.dump(my_list, f)



my_list = [
	'bob',
	'ted',
	{'hostname': 'router_thingy',
	'ip_address':['192.168.0.1','172.16.42.1','10.0.0.1']
	}]

make_yaml_file(my_list)
make_json_file(my_list)

	
