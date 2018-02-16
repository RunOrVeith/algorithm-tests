import numpy as np
import sys

def nw(a, b):
	# Answers "what do I have to do with a to get to b in the minimal amount of moves?"
	grid = np.zeros((len(a) + 1, len(b) + 1))
	grid[0,:] = -np.arange(len(b) + 1)
	grid[:, 0] = -np.arange(len(a) + 1)
	ops = {"replace": (lambda x, y: (max(x-1, 0),max(y-1, 0))), "delete": (lambda x, y: (max(x-1, 0), y)), "insert": (lambda x, y: (x, max(y-1, 0)))}
	req_ops = []

	# Fill grid
	for r in range(1, len(a) + 1):
		for c in range(1, len(b) + 1):
			subs = grid[r-1, c-1] - (a[r-1] != b[c-1])
			dels = grid[r-1, c] - 1
			reps = grid[r, c-1] - 1
			grid[r, c] = np.max([subs, dels, reps])
			
	print(grid)
	# Backtrack
	r, c = len(a), len(b)
	while r > 0 or c > 0:
		current = grid[r, c]
		new_coords = [ops[op](r, c) for op in ops.keys()]
		values = np.array([grid[coords] for coords in new_coords])
		if r == 0:
			values[0] = -float("inf")
			values[1] = -float("inf")
		if c == 0:
			values[0] = -float("inf")
			values[2] = -float("inf")
		max_value_idx = np.argmax(values, axis=0)
		max_value = np.max(values, axis=0) 
		assert current <= max_value
		r, c = new_coords[max_value_idx]
		if current != max_value:
			req_ops.append((list(ops.keys())[int(max_value_idx)], c))
	req_ops = req_ops[::-1]	
	print(a)
	a = list(a)
	for op, idx in req_ops:
		print(op, idx)
		if op == "insert":
			
			a.insert(idx, b[idx])
		elif op == "replace":
			a[idx] = b[idx]
		elif op == "delete":
			del a[idx]

		print("".join(a))


if __name__ == "__main__":
	nw(sys.argv[1], sys.argv[2])	
