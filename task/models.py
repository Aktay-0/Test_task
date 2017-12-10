from django.db import models

# Create your models here.

class Story():
    entrys = ["История:", ]

    def setEntry(self, entry):
        self.entrys.append(entry)

    def getEntrys(self):
        return self.entrys
        
class Storage(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    balance = models.FloatField()
    balance_story = Story()

    def addBalance(change):
        self.balance += change
        self.balance_story.setEntry("Зачисление: " + change)

    def subBalance(change):
        if self.balance - change < 0:
            return False
        else:
            self.balance -= change
            self.balance_story.setEntry("Списание: " + change)
            return True

    def getStory(self):
        return self.balance_story.getEntrys()
