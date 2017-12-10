from django.db import models

# Create your models here.
   
class Storage(models.Model):
    user = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    balance = models.FloatField()
    balance_story = models.TextField(blank = True)

    def addBalance(self, change):
        self.balance += change
        self.balance_story += "Зачисление: " + str(change) + ";"
        self.save()

    def subBalance(self, change):
        if self.balance - change < 0:
            return False
        else:
            self.balance -= change
            self.balance_story += "Списание: " + str(change) + ";"
            self.save()
            return True

    def getStory(self):
        return self.balance_story.split(';')
