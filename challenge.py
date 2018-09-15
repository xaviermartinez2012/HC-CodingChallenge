import math


class TwoSum:

    @staticmethod
    def find_two_sum(list_of_integers, target_value):
        """
        :param list_of_integers: A list of integers.
        :param target_value: We are looking for the indexes of two numbers that sum to this target value
        :returns: An ordered tuple of (index0, index1), indexes in the list_of_integers for numbers which sum to this target value, where index0 < index1.
        """

        indexed_loi = list(enumerate(list_of_integers))
        sorted_indexed_loi = sorted(indexed_loi, key=lambda pair: pair[1])
        for left_index, left_value in sorted_indexed_loi:
            for right_index, right_value in reversed(sorted_indexed_loi):
                if left_index == right_index:
                    break
                if (left_value + right_value) == target_value:
                    return (right_index, left_index) if (left_index >
                                                         right_index) else (left_index, right_index)
        return None


long_sequence = [int((i * math.sin(i) * 10) ** 2) for i in range(1000000)]
print(TwoSum.find_two_sum(long_sequence, 64718))

assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 13) == (0, 2)
assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 14) is None
assert TwoSum.find_two_sum([3, 6, 10, 2, 2], 4) == (3, 4)
assert TwoSum.find_two_sum(
    [-82, 84, 85, -68, -18, -83, 2, -24, 52, 74], 86) == (1, 6)
