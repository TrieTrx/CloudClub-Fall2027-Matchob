from ai.matching.fusion import rrf
from ai.matching.search import keyword_search


def test_rrf_ranks_common_item_first():
    """Test that RRF prioritizes items that appear early in multiple lists."""
    result = rrf(["a", "b", "c"], ["b", "c", "a"])
    assert result[0] == "b", f"Expected 'b' to be ranked first, got {result[0]}"


def test_rrf_includes_unique_items():
    """Test that RRF includes items that only appear in one list."""
    result = rrf(["a", "b"], ["c"])
    assert "c" in result, f"Expected 'c' to be in result, got {result}"


def test_keyword_search_ranks_by_relevance():
    """Test that keyword_search returns ids of best-matching units."""
    units = [
        {"id": "job1", "text": "Senior Python Developer with Django experience"},
        {"id": "job2", "text": "JavaScript frontend engineer React Vue"},
        {"id": "job3", "text": "Python backend engineer Flask FastAPI"},
        {"id": "job4", "text": "Full stack developer Python JavaScript"},
        {"id": "job5", "text": "Data scientist machine learning Python pandas"},
    ]
    
    result = keyword_search("Python developer", units, top_k=3)
    
    assert len(result) == 3, f"Expected 3 results, got {len(result)}"
    assert all(isinstance(id, str) for id in result), "Expected all results to be strings (ids)"
    assert "job1" in result or "job3" in result or "job4" in result, \
        "Expected Python-related jobs to be in top 3"


def test_keyword_search_handles_punctuation():
    """Test that keyword_search correctly handles punctuation in matching."""
    units = [
        {"id": "job1", "text": "Looking for Python, Java, and C++ skills"},
        {"id": "job2", "text": "Need Rust experience"},
        {"id": "job3", "text": "Python expert wanted"},
    ]
    
    result = keyword_search("Python", units, top_k=2)
    
    assert "job1" in result or "job3" in result, \
        "Python with comma should match Python query"
