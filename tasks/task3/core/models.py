from django.db import models

class Developer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name  = models.CharField(max_length=100)
    email      = models.EmailField(unique=True)
    age        = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Project(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    developers  = models.ManyToManyField(Developer, related_name="projects")

    def __str__(self):
        return self.title

class Skill(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    developer   = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="skills")

    def __str__(self):
        return self.title
