STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "


def writeTextToFile(param):
    FILE_NAME = "file.txt"
    content = STATICKY_TEXT + str(param)

    file = open(FILE_NAME, "w")

    file.write(content)
    file.close()

    return FILE_NAME
