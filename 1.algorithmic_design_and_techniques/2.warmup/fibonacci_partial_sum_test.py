# run with pytest <- requires pip3
import fibonacci_partial_sum

def test_fibonacci_partial_sum():
	assert fibonacci_partial_sum.fibonacci_partial_sum(3, 7) == 1
	assert fibonacci_partial_sum.fibonacci_partial_sum(10, 10) == 5
	assert fibonacci_partial_sum.fibonacci_partial_sum(10, 200) == 2
	assert fibonacci_partial_sum.fibonacci_partial_sum(0, 0) == 0
	assert fibonacci_partial_sum.fibonacci_partial_sum(1, 2) == 2
	assert fibonacci_partial_sum.fibonacci_partial_sum(0, 7) == 3

def test_get_fibonacci_huge_with_pisano_sequence():
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(0, 10) == 0
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(1, 10) == 1
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(2, 10) == 1
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(3, 10) == 2
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(4, 10) == 3
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(5, 10) == 5
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(6, 10) == 8
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(7, 10) == 3
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(8, 10) == 1
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(9, 10) == 4

	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(2015, 3) == 1
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(239, 1000) == 161
	assert fibonacci_partial_sum.get_fibonacci_huge_with_pisano_sequence(2816213588, 30524) == 10249