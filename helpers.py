
def print_related(words: List[Word], text: str) -> None:
    base_word = find_word(text, words)
    sorted_words = [
        word.text for (dist, word) in
            sorted_by_similarity(words, base_word.vector)
            if word.text.lower() != base_word.text.lower()
        ]
    print(', '.join(sorted_words[:7]))
    
def find_word(words: List[Word], text: str) -> Word:
    return next(w for w in words if text == w.text)
view rawhelpers.py hosted with ❤ by GitHub