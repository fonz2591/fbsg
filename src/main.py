import facebook
from person import Person


everyone = {}
# key: UID (int)
# value: person object


API_KEY = '################################'
APP_SECRET = '################################'

fb = facebook.Facebook(API_KEY, APP_SECRET)
fb.auth.createToken()
print "please press ENTER after loging into facebook and allowing the application in the browser window that opens\n"
fb.login()
raw_input()
fb.auth.getSession()

myself = Person(fb.uid)
myself.who_i_know(fb, everyone)
myself.who_am_i(fb)
everyone[fb.uid] = myself

for friend in myself.mutual_friends:
    friend.who_i_know(fb, everyone)
    friend.who_am_i(fb)


print "\n\n\n"
print "graph facebook {"
print "node[width=\".5\", height=\".5\", color=\"blue\" penwidth=\"5\"]"
print "edge[width=\".3\" color=\"gray20\"]"
print "packMode=\"node\""
print "splines=spline"
print "overlap=false"

connections = {}
# key: (smaller_UID, bigger_UID)
# value: True

for person in everyone.itervalues():
    print str(person.uid) + " [label=\"" + person.name + "\"];"

for person1 in everyone.itervalues():
    for person2 in person1.mutual_friends:
        if (min(person1.uid, person2.uid), max(person1.uid, person2.uid)) not in connections:
            print str(person1.uid) + " -- " + str(person2.uid) + ";"
            connections[(min(person1.uid, person2.uid), max(person1.uid, person2.uid))] = True

print "}"

