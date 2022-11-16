import pytest as pytest

from exceptions import InvalidCircleRadius
from models import Circle, Ball

tests_circle_create = [1.0, 2.0, 3.0]


@pytest.mark.parametrize('radius', tests_circle_create)
def test_circle(radius: float) -> None:
    """Test for circle's radius.
    Args:
        radius: float - circle's radius.
    """
    circle = Circle(radius)
    assert circle.radius == radius


@pytest.mark.xfail(raises=InvalidCircleRadius)
def test_err_invalid_circle():
    """Tests for circles' InvalidCircleRadius."""
    with pytest.raises(InvalidCircleRadius):
        Circle(-5)


@pytest.mark.xfail(raises=ValueError)
def test_err_value_circle():
    """Tests for circles' InvalidCircleRadius."""
    with pytest.raises(InvalidCircleRadius):
        Circle("ja radius pusti")


tests_circle_len = [(Circle(4), 25.13), (Circle(2), 12.57), (Circle(3), 18.85)]


@pytest.mark.parametrize('circle, expect', tests_circle_len)
def test_circle_len(circle: Circle, expect: float) -> None:
    """Test for circle's len.
    Args:
        circle: circle - the circle.
        expect: float - circle's len.
    """
    assert circle.get_len_circle() == expect


tests_ball_move_evenly = [(Ball(1), 6.28, 1, 0), (Ball(1), 3.14, 1, 180), (Ball(3), 9.42, 1, 179.9)]


@pytest.mark.parametrize('ball, speed, time,  expect', tests_ball_move_evenly)
def test_bool_move_evenly(ball: Ball, speed: float, time: float, expect: float) -> None:
    assert ball.move(speed, time) == expect


tests_ball_move_uniformly_accelerated_motiony = [(Ball(1), 3, 1, 10, 98.6), (Ball(10), 1, 1, 1, 8.59), (Ball(7), 5, 2, 20, 49.28)]


@pytest.mark.parametrize('ball, speed, time, acceleration, expect', tests_ball_move_uniformly_accelerated_motiony)
def test_bool_move_evenly(ball: Ball, speed: float, time: float, acceleration: float, expect: float) -> None:
    assert ball.move(speed, time, acceleration) == expect
