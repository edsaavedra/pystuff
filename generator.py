import itertools

chrs, min_length, max_length = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', 13, 13

f = open('./dir.txt', 'w')

for n in range(min_length, max_length+1):
	for xs in itertools.product(chrs, repeat=n):
		f.write('\n'.join(xs))
