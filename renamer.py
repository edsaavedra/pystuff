import os
import re

def main():
	i = 0
	path = "vids/mastering react/5 - Pagination, Filtering, and Sorting"
	for filename in os.listdir(path):
		print(re.sub(r'^\d+ - ', '', filename))
		src = path + '/' + filename
		dst = path + '/' + re.sub(r'^\d+ - ', '', filename)
		os.rename(src, dst)
		i += 1

if __name__ == '__main__':
	main()