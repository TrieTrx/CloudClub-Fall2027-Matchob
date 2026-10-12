from ai.matching.fusion import rrf


def test_rrf_ranks_common_item_first():
    """Test that RRF prioritizes items that appear early in multiple lists."""
    result = rrf(["a", "b", "c"], ["b", "c", "a"])
    assert result[0] == "b", f"Expected 'b' to be ranked first, got {result[0]}"


def test_rrf_includes_unique_items():
    """Test that RRF includes items that only appear in one list."""
    result = rrf(["a", "b"], ["c"])
    assert "c" in result, f"Expected 'c' to be in result, got {result}"
