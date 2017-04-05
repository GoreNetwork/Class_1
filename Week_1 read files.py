import yaml
import json
from pprint import pprint as pp


def read_and_print_yaml_file(file):
	with open(file) as f:
		new_list = yaml.load(f)
        print("YAML Print: \n")
	print(yaml.dump(new_list, default_flow_style = False))
        print("\n\n")
	

def read_and_print_json_file(file):
	with open (file) as f:
		new_list = json.load(f)
	print("JSON print: \n")
        pp(new_list)
        print("\n\n")


read_and_print_yaml_file('my_list.yml')
read_and_print_json_file('my_list.json')


	
