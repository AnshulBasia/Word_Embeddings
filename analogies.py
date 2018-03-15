
def closest_analogies(
    left2: str, left1: str, right2: str, words: List[Word]
) -> List[Tuple[float, Word]]:
    word_left1 = find_word(left1, words)
    word_left2 = find_word(left2, words)
    word_right2 = find_word(right2, words)
    vector = add_vectors(
        sub_vectors(word_left1.vector, word_left2.vector),
        word_right2.vector)
    closest = sorted_by_similarity(words, vector)[:10]
    def is_redundant(word: str) -> bool:
        """
        Sometimes the two left vectors are so close the answer is e.g.
        "shirt-clothing is like phone-phones". Skip 'phones' and get the next
        suggestion, which might be more interesting.
        """
        return (
            left1.lower() in word.lower() or
            left2.lower() in word.lower() or
            right2.lower() in word.lower())
    return [(dist, w) for (dist, w) in closest if not is_redundant(w.text)]

def print_analogy(left2: str, left1: str, right2: str, words: List[Word]) -> None:
    analogies = closest_analogies(left2, left1, right2, words)
    if (len(analogies) == 0):
        print(f"{left2}-{left1} is like {right2}-?")
    else:
        (dist, w) = analogies[0]
        print(f"{left2}-{left1} is like {right2}-{w.text}")
