import pytest

pytestmark = [pytest.mark.smoke, pytest.mark.str]

@pytest.mark.sanity
def test_case01():
    assert (1,2,3) == (2,3,4)