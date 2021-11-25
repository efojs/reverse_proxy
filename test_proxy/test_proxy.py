from proxy import format_text


def test_text_formatter(get_test_source_body, get_test_result_body):
    res = format_text(get_test_source_body)
    assert res == get_test_result_body.encode()
