#Defining Jaccard Correlation Function
def Jac(usersInCommon, totalUsers1, totalUsers2):
    union = (totalUsers1) + float(totalUsers2) - float(usersInCommon)
    return float(usersInCommon / union)
