
class Person:
    def __init__(self, uid):
        self.uid = uid
        self.name = '???'
        self.mutual_friends = []
    def who_am_i(self, fb):
        '''download my name from facebook'''
        self.name = fb.users.getInfo([self.uid], ['name'])[0]['name']
        print "downloaded " + self.name

    def who_i_know(self, fb, everyone):
        uid1 = fb.uid
        uid2 = self.uid
        self.mutual_friends = []
        fql_query = 'SELECT uid1 FROM friend WHERE uid1 IN (SELECT uid2 FROM friend WHERE uid1=' + str(uid1) + ') AND uid2=' + str(uid2)
        for mutual_friend_uid_dict in fb.fql.query(fql_query):
            uid = int(mutual_friend_uid_dict['uid1'])
            if (uid not in everyone):
                mutual_friend = Person(uid)
                everyone[uid] = mutual_friend
            else:
                mutual_friend = everyone[uid]
            self.mutual_friends.append(mutual_friend)
        print 'uid: ' + str(self.uid)
        print 'mutual friends: ' + str(len(self.mutual_friends))


