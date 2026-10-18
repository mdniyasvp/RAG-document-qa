import pytest

from src.chunker import chunk_text


def test_chunk_text_returns_expected_chunks():
    text = "abcdefghij"

    chunks = chunk_text(
        text,
        chunk_size=6,
        chunk_overlap=2,
    )

    assert chunks == ["abcdef", "efghij"]


def test_chunk_text_returns_empty_list_for_empty_input():
    assert chunk_text("") == []


def test_chunk_text_rejects_non_string_input():
    with pytest.raises(TypeError):
        chunk_text(None)


def test_chunk_text_rejects_non_positive_chunk_size():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=0)


def test_chunk_text_rejects_negative_overlap():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=5, chunk_overlap=-1)


def test_chunk_text_rejects_overlap_equal_to_chunk_size():
    with pytest.raises(ValueError):
        chunk_text("hello", chunk_size=5, chunk_overlap=5)
