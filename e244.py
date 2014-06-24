import re

start = (0, sum([1 << x for x in [1, 4, 5, 8, 9, 12, 13]]))
stop = (0, sum([1 << x for x in [2, 5, 7, 8, 10, 13, 15]]))
def get_next((white, reds)):
	all_nexts = []
	is_red = lambda x: (reds & (1 << x)) > 0
	new_whites = []
	if white > 3: new_whites.append((white - 4, 'U'))
	if white < 12: new_whites.append((white + 4, 'D'))
	if white % 4 != 0: new_whites.append((white - 1, 'L'))
	if white % 4 != 3: new_whites.append((white + 1, 'R'))
	for new_white, code in new_whites:
		if is_red(white) and not is_red(new_white):
			new_reds = reds - (1 << white)
		elif is_red(new_white) and not is_red(white):
			new_reds = reds + (1 << white)
		else:
			new_reds = reds
		all_nexts.append(((new_white, new_reds), code))
	return all_nexts

reachable = set([start])        # All the reachable states for BFS
current_seq = {start: []}	    # The move sequences to reach current state

while stop not in current_seq:
	print len(reachable)
	tmp_seq = {}
	to_add = set()
	for config, codes in current_seq.iteritems():
		for next, codes in get_next(config):
			if not next in reachable:
				to_add.add(next)
				if not next in tmp_seq:
					tmp_seq[next] = []
				for code in codes:
					tmp_seq[next].append(current_seq[config])
					tmp_seq[next].append(code)
	reachable |= to_add
	current_seq = tmp_seq

final_seq = ""
for s in re.findall('[a-zA-Z]', str(current_seq[stop])):
	final_seq += s
	final_seq += ' '
print final_seq
