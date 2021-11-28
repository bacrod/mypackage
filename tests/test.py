from my_package import myModule

def test_top_n():
    """Make sure top_n works"""

    assert myModule.top_n([8,9,3,2,5],3)==[9,8,5], 'incorrect'
    assert myModule.top_n([1,9,13,2,50],3)==[50,13,9], 'incorrect'
    assert myModule.top_n([3,1,6,4,5],3)==[6,5,4], 'incorrect'