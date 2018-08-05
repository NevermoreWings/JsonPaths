import json
import sys


def json2obj(data): 
	return json.loads(data)

def simplifier(my_dictionary):
	my_new_dict = {}
	for key, value in my_dictionary.items():
		if type(value) is dict: #simplify the inside
			simplified=simplifier(value)
			for new_key, new_value in simplified.items():
				my_new_dict_key = key + "." + new_key
				my_new_dict[my_new_dict_key] = new_value
		else:
			my_new_dict[key] = value
	return my_new_dict

def main():
	lines = sys.stdin.read()
	my_dictionary = json2obj(lines)
	result = simplifier(my_dictionary)
	print(result)
	return result

main()