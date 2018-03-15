def load_words(file_path: str) -> List[Word]:
    """Load and cleanup the data."""
    
    words = load_words_raw(file_path)
    print(f"Loaded {len(words)} words.")
    
    words = remove_stop_words(words)
    print(f"Removed stop words, {len(words)} remain.")
    
    words = remove_duplicates(words)
    print(f"Removed duplicates, {len(words)} remain.")
    
    return words