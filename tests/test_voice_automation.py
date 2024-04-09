
import pytest
from voice_automation.voice_automation import voice_automation 


# Demo Tests

@pytest.mark.skip
def test_start():
    actual = voice_automation()
    expected = "Starter test"
    assert actual == expected

@pytest.mark.skip
def test_fixture_01(fixture_01):
    actual = voice_automation(fixture_01)
    expected = "Starter fixture"
    assert actual == expected


# Demo Fixture
        
@pytest.fixture 
def fixture_01():
    yield "Starter fixture"

