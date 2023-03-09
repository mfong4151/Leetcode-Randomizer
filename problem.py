

##Object for individual problems

class Problem:
    def __init__(self, title,  url, notes, rt, memory,  group_membership,  passed):
        self.title = title
        self.url = url
        self.notes = notes
        self.rt = rt
        self.mem = memory
        self.group_membership = group_membership
        self.passed = passed
