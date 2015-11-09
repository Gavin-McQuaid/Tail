import sys
n = sys.argv[1]
n = int(n)

lines = []
line = raw_input()
while line != 'end':
	lines.append(line)
	line = raw_input()


if len(lines) < n:
	for l in lines:
		print l
else:
	i = len(lines) - n
	while i < len(lines):
		print lines[i]
		i += 1
