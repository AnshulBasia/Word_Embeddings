def sorted_by_similarity(words: List[Word], base_vector: Vector) -> List[Tuple[float, Word]]:
    """Returns words sorted by cosine distance to a given vector, most similar first"""
    words_with_distance = [(cosine_similarity(base_vector, w.vector), w) for w in words]
    # We want cosine similarity to be as large as possible (close to 1)
    return sorted(words_with_distance, key=lambda t: t[0], reverse=True)