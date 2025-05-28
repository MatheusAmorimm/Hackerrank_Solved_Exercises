def breakingRecords(scores):
    arrMaxMin = list()
    contMin = 0
    contMax = 0
    maxScore = minScore = 0
    cont = 0
    for score in range(len(scores)):
        if cont == 0:
            maxScore = minScore = scores[score]
            cont += 1
        else:
            if scores[score] > maxScore:
                maxScore = scores[score]
                contMax += 1
            elif scores[score] < minScore:
                minScore = scores[score]
                contMin += 1
    arrMaxMin.append(contMax)
    arrMaxMin.append(contMin)
    return arrMaxMin