import pytest

from core.RT_Margin_clipboard import get_multiplier

@pytest.mark.parametrize(
    "value,expected",
    [
        (0.5, 1.75),
        (1, 1.75),
        (2_000_000, 1.70),
        (4_000_000, 1.65),
        (8_000_000, 1.60),
        (16_000_000, 1.55),
        (32_000_000, 1.50),
    ],
)
def test_get_multiplier(value, expected):
    assert get_multiplier(value) == expected
