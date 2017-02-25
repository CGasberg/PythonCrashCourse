#3-7 shrinking Guest list
guestlist = ["Me","Myself","I"]
for guests in guestlist:
    print("Hello %s, I would like to invite you to dinner" % guests)

print ("%s can't make it" % guestlist[1])

cant_come = "Myself"
guestlist.remove(cant_come)
guestlist.insert(1, "Henry")

for guests in guestlist:
    print("Hello %s, I would like to invite you to dinner" % guests)

print ("Hello, I've found a new table")

guestlist.insert(0, "Per")
guestlist.insert(2, "Bets")
guestlist.append("Chris")

for guests in guestlist:
    print("Hello %s, I would like to invite you to dinner" % guests)

print ("I can only invite 2 people")

print (len(guestlist))

while len(guestlist) > 2:
    print("Hello %s, you are no longer invited" % guestlist.pop())

for guests in guestlist:
    print("Hello %s, I would like to invite you to dinner" % guests)

del guestlist[:len(guestlist)]
print (guestlist)
