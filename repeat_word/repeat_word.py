from hash_tables.hash_tables import Hashtable


def repeat_word(text: str) -> str:
    valid_chars = "abcdefghijklmnopqrstuvwxyz "
    words = "".join([i for i in text.lower() if i in valid_chars])
    hashs = Hashtable()
    for i in words.split():
        if hashs.contains(i):
            return i
        hashs.set(i, "i")

    return "no words found"
