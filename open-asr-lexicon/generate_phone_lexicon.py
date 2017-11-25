import os, sys, codecs

ilex_fn    = sys.argv[1]
mapping_fn = sys.argv[2] # pinyin_to_phone mapping


mapping = {}
for l in open(mapping_fn, 'r'):
	if l.strip() == '':
		continue
	cols = l.strip().split('\t')
	old = cols[0]
	new = cols[1]
	mapping[old] = new
	
for l in open(ilex_fn, 'r'):
	if l.strip() == '':
		continue
	cols = l.strip().split('\t')
	if len(cols) == 1:
		continue
	word  = cols[0]
	prons = cols[1].split(';')

	for pron in prons:
		sys.stdout.write('{}\t'.format(word))
		symbols = pron.split(' ')
		for i in range(len(symbols)):
			if mapping.get(symbols[i]) != None:
				sys.stdout.write('{}'.format(mapping[symbols[i]]))
			else:
				sys.stdout.write('{}'.format(symbols[i]))
			if i != len(symbols)-1:
				sys.stdout.write(' ')
		sys.stdout.write('\n')
