def get_min(values):
	min = values[0]
	for val in values:
		if val < min:
			min=val
	return min