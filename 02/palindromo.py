def eh_palindromo_dois_ponteiros(text):
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = "".join(char for char in text if char.isalnum()).lower()

    inicio = 0
    fim = len(text) - 1
    while fim >= inicio:
        if text[inicio] != text[fim]:
            return False
        fim -= 1
        inicio += 1

    return True


def eh_palindromo(text):
    text = text.encode("ascii", "ignore").decode("utf-8")
    text = "".join(char for char in text if char.isalnum()).lower()
    return text == text[::-1]
