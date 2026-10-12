def rrf(*ranked_lists, k: int = 60) -> list:
    """Reciprocal Rank Fusion across multiple ranked lists.

    Combines several ranked lists into a single consensus ranking using
    the RRF formula: score(item) = sum(1 / (k + rank)) for each list
    that contains the item, where rank is 1-indexed.

    Args:
        *ranked_lists: One or more iterables of hashable items, each
            ordered from most to least relevant.
        k: Smoothing constant that reduces the impact of high-ranked
            items. Defaults to 60 (the value from the original paper).

    Returns:
        A deduplicated list of items sorted by descending RRF score.

    Raises:
        ValueError: If no ranked lists are provided.
    """
    if len(ranked_lists) == 0:
        raise ValueError("At least one ranked list is required.")

    item_scores: dict = {}
    for ranked_list in ranked_lists:
        for rank, item in enumerate(ranked_list, start=1):
            item_scores[item] = item_scores.get(item, 0.0) + 1.0 / (k + rank)

    return [item for item, score in sorted(item_scores.items(), key=lambda x: x[1], reverse=True)]