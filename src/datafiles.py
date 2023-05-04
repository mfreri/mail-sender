import csv
import json
import os


def check_file(filename):
	if not os.path.exists(filename):
		raise FileNotFoundError(f"File <{filename}> not found.")


# CSV

# Read
def read_csv(filename):
	# Read an CSV file and return a list of dictionaries with name_column: value
	check_file(filename)
	output = []
	with open(filename) as f:
		data = csv.DictReader(f)
		for row in data:
			output.append(row)
	return output


# JSON

# Read
def read_json(filename):
	# Read a JSON file and return a dictionary with the content
	check_file(filename)
	with open(filename, 'r') as f:
		data = json.load(f)
	return data


def read_json_key(filename, key):
	# Read a JSON file ando return the value of a given key
	return read_json(filename)[key]


# TXT

# Read
def read_txt(filename):
	# Read the content of a text file
	check_file(filename)
	with open(filename) as f:
		output = f.read()
	return output


if __name__ == '__main__':
	print("This is a package. Use it inside your program.")

