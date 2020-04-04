def split(text, char1, char2):
    for i in range(0, len(text)):
        if text.find(char1):
            result = text.replace(char1, char2)
            return result


