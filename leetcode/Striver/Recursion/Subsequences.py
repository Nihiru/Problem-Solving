array = [3, 1, 2]
length = len(array)


def subseq(index, subList):
    if index >= length:
        print(subList)
        return
    subList.append(array[index])
    subseq(index+1, subList)
    subList.remove(array[index])
    subseq(index+1, subList)
    return


subseq(0, [])
