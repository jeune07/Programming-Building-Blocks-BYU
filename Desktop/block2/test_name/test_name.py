from names import make_full_name, \
    extract_family_name, extract_given_name
import pytest

# def test_make_full_name():

#    #test that the return srting values.
#    assert make_full_name("jeune", "Winsley")=="Winsley;jeune"


# def test_extract_given_name():   
#    assert extract_given_name("Brown; Sally")== "Sally"
def test_extract_family_name():
    # Test cases where the input string is in the expected format.
    assert extract_family_name("Brown; Sally") == "Brown"
    assert extract_family_name("Smith; John") == "Smith"
    assert extract_family_name("Lee; Mary Jane") == "Lee"
    assert extract_family_name("Baker; Richard Edward") == "Baker"
    assert extract_family_name("Zhang; Wei") == "Zhang"
    
    # Test cases where the input string is not in the expected format.
    with pytest.raises(ValueError):
        extract_family_name("Brown, Sally")



# def extract_given_name():
#    print("jfjf")


pytest.main(["-v", "--tb=line", "-rN", __file__])