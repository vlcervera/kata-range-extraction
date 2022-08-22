from typing import List


class IncorrectMinRangeSize(Exception):
    def __init__(self, min_range_size: int):
        super().__init__(
            f"Range size must be a positive number, incorrect value for {min_range_size}"
        )


class RangeExtraction:
    def __init__(self, numbers: List[int]):
        self.numbers = sorted(numbers)

    def extract(self, min_range_size: int = 3) -> str:
        if min_range_size < 1:
            raise IncorrectMinRangeSize(min_range_size)

        consecutive_numbers_grouped = self._group_consecutive_numbers()
        ranges = [
            self._format_groups_in_ranges(group, min_range_size)
            for group in consecutive_numbers_grouped
        ]
        return ",".join(ranges)

    def _group_consecutive_numbers(self) -> List[List[int]]:
        groups = []
        consecutive_numbers = [self.numbers[0]]
        for number in self.numbers[1::]:  # iterate from second position
            if consecutive_numbers[-1] == number - 1:  # numbers are consecutive
                consecutive_numbers.append(number)
                continue
            groups.append(consecutive_numbers)
            consecutive_numbers = [number]
        else:
            groups.append(consecutive_numbers)

        return groups

    def _format_groups_in_ranges(self, group: List[int], min_group_size: int) -> str:
        if len(group) >= min_group_size:
            return f"{group[0]}-{group[-1]}"

        return ",".join([str(number) for number in group])
