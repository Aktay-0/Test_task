from django.db import models

# Create your models here.

class Story():
    entrys = []

    def setEntry(self, entry):
        self.entrys.append(entry)

    def getEntrys(self):
        return entrys
        
class Storage(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    balance = models.FloatField()
    balance_story = Story()

    def addBalance(change):
        balance += change

    def subBalance(change):
        if balance - change < 0:
            return False
        else:
            balance -= change
            return True

    def getStory(self):
        return balance_story.getEntrys()
