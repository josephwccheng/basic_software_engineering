from time import gmtime, strftime
now = strftime("%a-%d-%b-gmt-%Y-%H-%M-%S", gmtime())

print(now)