import pytest
import sys

# pytestmark = pytest.mark.skipif(sys.version_info > (3, 6), reason="do not work on version >= 3.6")

const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah

# print(cent_to_fah())
@pytest.mark.skip(reason="skip test for no reason")
def test_case01():
    assert type(const) == float

# @pytest.mark.skipif(sys.version_info > (3, 6), reason="do not work on version >= 3.6")
@pytest.mark.skipif(cent_to_fah() == 32, reason="skip test cuz default value tested")
def test_case02():
    assert cent_to_fah() == 32

def test_case03():
    assert cent_to_fah(38) == 100.4