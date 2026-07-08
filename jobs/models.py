from django.db import models
from django.utils import timezone
from datetime import timedelta
from users.models import User


# VILOYATLAR (Regions)
class Region(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = "Regions"

    def __str__(self):
        return self.name


# TUMANLAR (Districts)
class District(models.Model):
    name = models.CharField(max_length=100)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    class Meta:
        verbose_name_plural = "Districts"

    def __str__(self):
        return f"{self.name} - {self.region.name}"


# ISH TURLARI
JOB_TYPE_CHOICES = (
    ("construction", "Qurilish"),
    ("cleaning", "Tozalash"),
    ("repair", "Ta'mirish"),
    ("delivery", "Tashimoq"),
    ("other", "Boshqa"),
)

STATUS_CHOICES = (
    ("open", "Ochiq"),
    ("closed", "Yopiq"),
    ("completed", "Tugallangan"),
)


# ISHLAR
class Job(models.Model):
    employer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='posted_jobs',
        null=True,
        blank=True,
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE_CHOICES)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, default=1)
    district = models.ForeignKey(District, on_delete=models.CASCADE, default=1)
    location = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, default='', blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    required_workers = models.IntegerField(default=1)
    end_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.region.name}"

    def is_expired(self):
        return timezone.now() > self.end_date

    def save(self, *args, **kwargs):
        if self.is_expired():
            self.status = 'closed'
        super().save(*args, **kwargs)


# ARIZALAR
class Application(models.Model):
    APPLICATION_STATUS_CHOICES = (
        ("pending", "Kutilmoqda"),
        ("accepted", "Qabul qilindi"),
        ("rejected", "Rad etildi"),
    )
    worker = models.ForeignKey(User, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    status = models.CharField(max_length=20, choices=APPLICATION_STATUS_CHOICES, default='pending')
    applied_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-applied_at']
        unique_together = ('worker', 'job')

    def __str__(self):
        return f"{self.worker.username} - {self.job.title}"
