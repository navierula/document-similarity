'''
jaccard_similarity.py

This programs implements the Jaccard Similarity for a 
given set of documents.
'''

# to keep comparing docs,
# while "doc_list" != []:
# assign a max_score and return
# which two docs in the set are the
# most similar

import json
import nltk
import string

def read_file(filename):
	with open(filename) as fp:
		data = json.load(fp)
		data = data["text"].encode("ascii", "ignore")
		data = data.decode('utf-8','ignore').encode("utf-8")
		print(data)

def clean_file(data):
	data = data.split("")
	print(data)


def main():

	#read_file("test_docs/val-26492666287-1.json")
	#read_file("test_docs/val-26492666287-2.json")
	#read_file("test_docs/val-26492666287-3.json")
	#read_file("test_docs/val-26492666287-4.json")

	#read_file("test_docs/val-28063956216-1.json")
	#read_file("test_docs/val-28063956216-2.json")
	#read_file("test_docs/val-28063956216-3.json")
	d = read_file("test_docs/val-28063956216-4.json")
	clean_file(d)

if __name__ == "__main__":
	main()