from medsummary.core import extract_sections
def test_sections(): assert extract_sections("Plan: follow up")["plan"] == ["follow up"]
