magicians = ['alice','david','carolina']


for magician,nm in zip(magicians, magicians[1:]):
    print(magician.title() + ", that was a great trick!")
    print("Your turn, " + nm)
