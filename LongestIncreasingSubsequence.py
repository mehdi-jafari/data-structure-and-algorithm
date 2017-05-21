def find_the_longest_sequence(input):
	T = [0]
	R = [-1] * len(input)
	best_length = 1;
	
	for i in range(1, len (input)) :
		if input[i] > input[T[len(T)-1]] :			
			R[i] = T[len(T) - 1]
			T.append(i)			
		elif input[i] < input[T[0]] :
			T[0] = i
		else:
			new_index = find_the_best_index(input, T , input[i])
			T[new_index] = i
			R[T[new_index]] = T[new_index-1]
		

	current_index = T[len(T)-1]
	output = []
	
	while current_index != -1 :
		output.append(input[current_index])
		current_index = R[current_index]

	for i in reversed(output):
		print i
	
	print 'length is ' + str(len(T))
	


def find_the_best_index(input , T , value) :
	start = 0
	end = len(T) -1
	while start <= end :
		middel = (end + start) // 2
		if(middel < len(T) and value > input[T[middel]] and value <= input[T[middel+1]]):
			return middel+1
		if value > input[middel] :
			start = middel + 1
		else:
			end = middel -1;


