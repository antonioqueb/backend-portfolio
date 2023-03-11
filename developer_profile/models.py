from django.db import models

class DeveloperProfile(models.Model):
    artistic_name = models.CharField(max_length=50, blank=True, null=True)
    full_name = models.CharField(max_length=50, blank=True, null=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    nationality = models.CharField(max_length=50, blank=True, null=True)
    short_description = models.CharField(max_length=80, blank=True, null=True)
    long_description = models.TextField(blank=True, null=True)
    identity = models.CharField(max_length=50, blank=True, null=True) #Im a developer
    actual_job = models.CharField(max_length=50, blank=True, null=True)
    tag_line = models.CharField(max_length=50, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)
    github = models.CharField(max_length=50, blank=True, null=True)
    linkedin = models.CharField(max_length=50, blank=True, null=True)
    twitter = models.CharField(max_length=50, blank=True, null=True)
    whatsapp = models.IntegerField(blank=True, null=True)
    languages = models.JSONField(blank=True, null=True)
    website = models.CharField(max_length=50, blank=True, null=True)
    strength = models.JSONField(blank=True, null=True)
    soft_skills = models.JSONField(blank=True, null=True)
    hard_skills = models.JSONField(blank=True, null=True)
    goals = models.JSONField(blank=True, null=True)
    technologies = models.JSONField(blank=True, null=True)
    libraries = models.JSONField(blank=True, null=True)
    frameworks = models.JSONField(blank=True, null=True)
    microframeworks = models.JSONField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='files', blank=True, null=True)
    illustrations = models.ImageField(upload_to='files', blank=True, null=True)
    graphics_design = models.ImageField(upload_to='files', blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    certifications = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.artistic_name or self.full_name
