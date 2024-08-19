from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
    def __str__(self):
        return f'{self.title} - {self.project.title}'