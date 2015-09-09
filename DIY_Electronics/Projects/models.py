from django.db import models

# Create your models here.


# The projects model is for the creation and viewing of Electronic Prototyping User projects.
# These can be viewed anytime and added to after user has been approved.
class Projects(models.Model):
    title = models.CharField(60)
    user = models.OneToOneField(User)
    date = models.DateTimeField
    difficulty = models.CharField(choices=)
    instructions = models.TextField(max_length=365)
    tool_list = models.CharField(max_length=180)
    parts_list = models.CharField(max_length=180)
    scripts_code = models.TextField(max_length=365)
    script_language = models.CharField(max_length=180)
