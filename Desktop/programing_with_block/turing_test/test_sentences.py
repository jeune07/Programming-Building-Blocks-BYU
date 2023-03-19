import random
import pytest
from sentences import get_determiner, get_noun, get_verb

def test_sentence_structure():
    # Generate a random sentence
    quantity = random.randint(1, 3)
    tense = random.choice(['past', 'present', 'future'])
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    sentence = f"{determiner.capitalize()} {noun} {verb}."

    # Check that the sentence has the correct structure
    assert isinstance(sentence, str)
    assert sentence[0].isupper() == True
    assert sentence[-1] == "."
    #assert len(sentence.split()) == 3

    # Check that the sentence uses the correct determiner and verb tense
    if quantity == 1 and tense == "present":
        assert sentence.split()[0] in ["A", "One", "The"]
        assert sentence.split()[2].endswith("s") == False
    else:
        assert sentence.split()[0] in ["Some", "Many", "The"]
        
    if tense == "past":
        assert sentence.split()[2].endswith("ed") == True
    elif tense == "future":
        assert sentence.split()[2].startswith("will") == True
    else:
        assert sentence.split()[2].endswith("s") == False

pytest.main(["-v", "--tb=line", "-rN", __file__])
