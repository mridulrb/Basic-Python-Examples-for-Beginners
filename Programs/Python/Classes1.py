class match:
    '''Runs & Wickets'''
    runs=281
    wickets=5
    def __init__(self,runs,wickets):
        self.runs=runs
        self.wickets=wickets
        def disp(self):
            print "Runs scored are:",self.runs
            print "Wickets taken are:",self.wickets
m=match(300,50)
m.marks=90
print "Test.__doc__",match.__doc__
print "Test.__name__",match.__name__
print "Test.__module__",match.__module__
print "Test.__bases__",match.__bases__
print "Test.__dict__",match.__dict__
print dir(m)
print vars(m)
print dir(match)
print vars(match)

