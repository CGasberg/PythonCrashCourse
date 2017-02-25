#3-6 more guests
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
