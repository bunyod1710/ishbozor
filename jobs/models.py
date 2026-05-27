from django.db import models
from users.models import User
JOB_TYPE_CHOICES =(
    ("Construction","Qurilish"),
    ("Cleaning","Tozalash"),
    ("Repair","Ta'mirlash"),
    ("Moving","Ko'chirish"),
    ("other","Boshqa"),

)
STATUS_CHOICES = (
    ("open","ochiq"),
    ("closed","yopiq"),
    ("completed","Tugallangan"),
)
STATUS_CHOICES_APP=(
    ("pending","Kutilmoqda"),
    ("accepted","Qabul qilindi"),
    ("rejected","Rad etildi"),
)
class Job(models.Model):
    employer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posted_jobs" )
    title = models.CharField(max_length=255)
    description = models.TextField()
    job_type = models.CharField(choices=JOB_TYPE_CHOICES)
    location = models.CharField(max_length=255)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    required_workers = models.IntegerField(default=1)
    status = models.CharField(choices=STATUS_CHOICES,default="open")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.title} - {self.location}"
class Application(models.Model):
    worker = models.ForeignKey(User , on_delete=models.CASCADE,related_name="applications")
    job = models.ForeignKey(Job , on_delete=models.CASCADE , related_name="applications")
    status = models.CharField(choices=STATUS_CHOICES_APP, default="pending")
    applied_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.worker.username} - {self.job.title}"
