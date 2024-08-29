from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rate = models.FloatField(default=0)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title 

    def final_rating(self, new_rating):
        self.rate = (self.rate * self.count + new_rating) / (self.count + 1)
        self.count += 1
        self.save()

class Lecture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

def __str__(self):
    return f"{self.user.username} - {self.course.title}"

