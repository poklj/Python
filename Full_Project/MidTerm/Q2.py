__author__ = "Zachary Higgs"
def vert_string(String):
    """
    Make a given String vertical (Without spaces for words that are shorter)
    :param String: String you wish to vertical
    :return: Newlined List of Words derived from string given
    """

    oldList = String.split()
    newList = []
    longestString = len(max(oldList, key=len))
    for i in range(len(oldList)):
        newList.append("")

    for x in oldList:
        letter = 0
        for i in x:
            letter += 1
            if newList[letter] == None:
                newList.append("")
            newList[letter] = newList[letter] + i

    nWord = ""
    for i in newList:
        if i != '':
            nWord = nWord + i + "\n"

    return nWord

stringlist = "This test is easy but very long adadada opdppa dooodic aAADD"
print(vert_string(stringlist))