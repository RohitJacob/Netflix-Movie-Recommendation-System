checker = "\Users\RJ\fakepath\Checker.py"
common = "\Users\RJ\fakepath\Common.py"
jacquard = "\Users\RJ\fakepath\Jacquard.py"
import checker
import common
import jacquard


#Reading Input File
file = sc.textFile("/Users/Rohit/Desktop/data.txt")

#Filters Invalid Entries Out
validEntries = file.map(lambda x: checker.checker(x)).filter(lambda x: x)

#Splits Valid Entries and the mapper emits (Movie, User) to get list of users
splitEntries = validEntries.map(lambda x: (x.split("\t")[1], x.split("\t")[0])).reduceByKey(lambda x,y: x + "," + y) 

#Cartesian Product of userlist to get combinations
joinuser = splitEntries.cartesian(splitEntries)

#Mapping Length of Users and Common Users for a set of Movies
commonusers = joinuser.map(lambda x: (common.common(x[0][0], x[0][1], x[1][0], x[1][1]))).filter(lambda x: x)

#Using Jacquaard to find correlation between two movies
eq = commonusers.map(lambda ((m1,m2),l,n1,n2): ((m1, m2), jacquard.Jac(l,n1,n2))).filter(lambda x: x)

#Taking Top 100
eq.sortBy(lambda ((x,y), z): z, False).take(100)
