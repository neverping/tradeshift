from triangle import check_triangle_type
import pytest

class TestClass(object):

    def test_if_inputs_are_ok(self):
        with pytest.raises(ValueError, match=r'All values must be integer type!'):
            check_triangle_type('a', None, 1)

    def test_for_numbers_above_zero(self):
        with pytest.raises(ValueError, match=r'You must pass values greater than 0!'):
            check_triangle_type(0, 2, -1)

    def test_it_must_be_a_equilateral_triangle(self):
        t = check_triangle_type(2, 2, 2)
        assert t == 'This triangle is an equilateral type.'

    def test_it_must_be_a_isosceles_triangle(self):
        t = check_triangle_type(2, 1, 2)
        assert t == 'This triangle is an isosceles type.'

    def test_it_must_be_a_scalene_triangle(self):
        t = check_triangle_type(2, 1, 3)
        assert t == 'This triangle is a scalene type.'