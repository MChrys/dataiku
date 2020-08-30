from django.db import models

class Dataiku_account(models.Model):

    email = models.CharField(max_length=60, null=True, blank=True, primary_key=True)
    password = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.email



# Create your models here.
class Question(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('check', 'check')
    )
    CHOICES_TYPE = (

        ('checkbox', 'checkbox'),
        ('radio', 'radio')
    )
    text = models.CharField(max_length=255, null=True, blank=True, primary_key=True)
    session = models.models.ForeignKey(session)
    status = models.CharField(max_length=255, null=True, blank=True, choices = STATUS)
    choice_type = models.CharField(max_length=255, null=True,, blank=True, default= "radio" ,choices = CHOICES_TYPE)

    def __str__(self):
        return self.text


class Posibility(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE)
    text = models.CharField(max_length=255, null=True, blank=True)
    rank = models.models.ForeignKey(Answer)

class Answer(models.Model):
    CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
    )

    choice = models.IntegerField(max_length=10, null=True,, blank=True, choices = CHOICES)
    run = models.ForeignKey(Run)

class Run(models.Model):

    question = models.ForeignKey(
        Question,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    right = models.BooleanField()
    
class Session(models.Model):
    STATUS = (
        ('running','running'),
        ('finish','finish')
    )
    email = models.ForeignKey(Dataiku_account , on_delete=models.CASCADE)
    start = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    countdown = models.DateTimeField(auto_now_add=False, blank=True, null=True)
    score = models.IntegerField(default=0)
    lenght = models.IntegerField(default=0)


