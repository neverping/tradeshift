from triangle import check_triangle_type

class TestClass(object):

    def test_if_inputs_are_ok(self):
        assert check_triangle_type('a', 'b', None) == 0

    def test_only_numbers_are_accepted(self):
        assert check_triangle_type('a', 2, None) == 0

    def test_for_numbers_above_zero(self):
        assert check_triangle_type(-1, 2, 0) == 2
