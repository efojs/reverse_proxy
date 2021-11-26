import pytest

test_words = """\
    Sprite™-ish Sprite-ish sprite Sprite™ sprite/Sprite™/sprite! \
    600000 Straße пришёл spri_e sprite algúns التوهم"""

test_words_result = """\
    Sprite™-ish Sprite™-ish sprite™ Sprite™ sprite™/Sprite™/sprite™! \
    600000 Straße™ пришёл™ spri_e sprite™ algúns™ التوهم™"""


@pytest.fixture
def get_test_source_body():
    return """{0}<p>{0}</p><code>{0}</code>""".format(test_words)


@pytest.fixture
def get_test_result_body():
    return """{0}<p>{0}</p><code>{1}</code>""".format(test_words_result, test_words)
