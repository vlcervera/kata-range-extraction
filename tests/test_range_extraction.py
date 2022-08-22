import pytest

from app.range_extraction import RangeExtraction, IncorrectMinRangeSize


class TestRangeExtractionShould:

    def test_extract_with_no_ordered_numbers(self):
        numbers = [1, 2, 3, -2, -10, -20, -11, 100]
        range_extraction = RangeExtraction(numbers)
        assert range_extraction.execute() == "-20,-11,-10,-2,1-3,100"

    @pytest.mark.parametrize(
        "numbers,expected_range",
        [
            (
                    [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15],
                    "-10--8,-6,-3-1,3-5,7-11,14,15",
            ),
            (
                    [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20],
                    "-10--8,-6,-3-1,3-5,7-11,14,15,17-20",
            )
        ],
    )
    def test_extract_with_default_min_range_size(self, numbers, expected_range):
        range_extraction = RangeExtraction(numbers)
        assert range_extraction.execute() == expected_range

    def test_extract_with_custom_min_range_size(self):
        numbers = [-10, -9, -8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20, 21]
        range_extraction = RangeExtraction(numbers)
        assert range_extraction.execute(min_range_size=5) == "-10--6,-3-1,3,4,5,7-11,14,15,17-21"

    def test_extract_with_incorrect_min_range_size(self):
        with pytest.raises(IncorrectMinRangeSize) as ex:
            numbers = [-10, -9, -8, -7, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20, 21]
            range_extraction = RangeExtraction(numbers)
            range_extraction.execute(min_range_size=0)
