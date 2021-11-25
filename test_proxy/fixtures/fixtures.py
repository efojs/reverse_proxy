import pytest


@pytest.fixture
def get_test_source_body():
    return """<a href="news">Hacker News</a><td>Im developing ... random
    flow fields... <p>600000 ways always looking Friday/Cybermonday social
    skills?</p></td><pre><code>[string in list(soup.strings)]</code></pre>"""


@pytest.fixture
def get_test_result_body():
    return """<a href="news">Hacker™ News</a><td>Im developing ... random™
    flow fields™... <p>600000 ways always™ looking Friday™/Cybermonday social™
    skills™?</p></td><pre><code>[string in list(soup.strings)]</code></pre>"""
