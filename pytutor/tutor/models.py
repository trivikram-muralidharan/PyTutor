from django.db import models


# Create your models here.

class Usr(models.Model):
    level = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Question(models.Model):

    question_content = models.CharField(max_length=1000)
    
    

    def __str__(self):
        return self.question_content


class TestCase(models.Model):

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    input_case = models.CharField(max_length=200)
    

    def __str__(self):
        return self.input_case


class CourseMat(models.Model):

    coursecontent = models.CharField(max_length=1000)
    level = models.IntegerField(default=0)

    def __str__(self):
        return str(self.level)

