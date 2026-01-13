def ordenando_palavras(words):
    return " ".join(sorted(words.split(), key=str.casefold))
