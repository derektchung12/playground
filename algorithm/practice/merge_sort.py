#merge sort practice

def merge_sort(input_list):
	def merge(left_index, mid, right_index):
		temp_array = input_list[left_index:right_index + 1]

		left_iterator = 0
		right_iterator = mid - left_index + 1

		input_iterator = left_index

		while input_iterator <= right_index:
			if left_iterator > mid - left_index: #left iterator used up
				input_list[input_iterator] = temp_array[right_iterator]
				right_iterator += 1
			elif right_iterator >= len(temp_array): #right iterator is used up
				input_list[input_iterator] = temp_array[left_iterator]
				left_iterator += 1
			elif temp_array[left_iterator] < temp_array[right_iterator]:
				input_list[input_iterator] = temp_array[left_iterator]
				left_iterator += 1
			else:
				input_list[input_iterator] = temp_array[right_iterator]
				right_iterator += 1
			input_iterator += 1



	def merge_sort_helper(left_index, right_index):
		if left_index < right_index:
			if left_index == right_index - 1:
				if input_list[right_index] < input_list[left_index]: #swap
					temp = input_list[right_index]
					input_list[right_index] = input_list[left_index]
					input_list[left_index] = temp
				return
			mid = (left_index + right_index)/2
			merge_sort_helper(left_index, mid)
			merge_sort_helper(mid + 1, right_index)
			merge(left_index, mid, right_index)

	merge_sort_helper(0, len(input_list) - 1)

a = [5,4,6,78,2,6,8,2,5,3,1]
merge_sort(a)
print a