def sort(input):
	result = list(input)
	_split(input, 0, len(input), result)
	return result

def _split(input, start_index, end_index , result):
	if end_index - start_index < 2 :
		return

	middle = (start_index + end_index) // 2
	_split(input, start_index, middle, result)
	_split(input, middle, end_index, result)
	_merge(result, start_index, middle , end_index)
		

def _merge(output, start_index, middle, end_index):
	input_ref = list(output)
	i = start_index
	j = middle

	for k in range(start_index, end_index):
		if i < middle and (j >= end_index or input_ref[i] < input_ref[j]):
			output[k] = input_ref[i]
			i+=1
		else:
			output[k] = input_ref[j]
			j+=1
	return output

input_arr = [5,2,4,7,8,3,24,1]
print input_arr

result = sort(input_arr)
print result