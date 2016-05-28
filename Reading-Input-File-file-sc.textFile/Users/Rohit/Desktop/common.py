#Finding Length of userlist and Common users
def common(m1,lister,m2,lister2):
	if(m1<m2) and m1!="" and m2!="":
		return ((m1,m2),len(set(lister).intersection(set(lister2))) , len(set(lister)), len(set(lister2)))
	else:
		return 0
