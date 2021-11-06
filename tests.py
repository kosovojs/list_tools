import pytest

from list_tools import *

@pytest.mark.parametrize("test_name, list_to_chunk, chunk_size, expected_result", [
	("empty string", "", 2, []),
	("empty list", [], 2, []),
	("list", [0, 1, 2], 1, [[0], [1], [2]]),
	("not full list", [0, 1, 2], 2, [[0, 1], [2]]),
	("not full list", [0, 1, 2], 5, [[0, 1, 2]]),
	# ("dictionary", {'lorem': 'ipsum', 'foo': 'bar', 'star': 'wars'}, 2, [{'lorem': 'ipsum', 'foo': 'bar'}, {'star': 'wars'}]),
])
def test_chunk_success(test_name, list_to_chunk, chunk_size, expected_result):
	result = chunk(list_to_chunk, chunk_size)
	assert list(result) == expected_result, test_name
