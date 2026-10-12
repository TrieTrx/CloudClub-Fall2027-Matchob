import re
from rank_bm25 import BM25Okapi

def words(text: str) -> list[str]:
    return re.findall(r"\w+", text.lower())
def keyword_search(requirement: str, units: list[dict], top_k: int = 5) -> list[str]:
    bm25 = BM25Okapi([words(u["text"]) for u in units])
    scores = bm25.get_scores(words(requirement))
    ids = list(range(len(units)))
    ids.sort(key=lambda x: scores[x], reverse=True)
    return [units[idx]["id"] for idx in ids[:top_k]]