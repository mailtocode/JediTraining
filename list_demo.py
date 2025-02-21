import random
def reverse(input_list):
    last_index = len(input_list) - 1
    first_index = 0
    measure_count = 0
    while first_index < last_index:
        measure_count += 1
        a_element = input_list[last_index] * input_list[first_index]
        input_list[first_index] = int(a_element / input_list[first_index])
        input_list[last_index] = int(a_element / input_list[first_index])
        first_index = first_index + 1
        last_index = last_index - 1
    print(measure_count)


alist = random.sample(range(1000),10)
print(alist)
reverse(alist)
print(alist)
