def str_to_float(word:str) -> float or None:
    try:
        word = float(word)
        return word
    except ValueError:
        return None

