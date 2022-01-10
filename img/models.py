from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _, get_language
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

class Github(models.Model):
    githubuser = models.CharField(_("Github Username"), max_length=150, db_index=True)
    image_link = models.CharField(_("Image Link"), max_length=150, db_index=True, blank=True)
    user_name = models.CharField(_("User Name"), max_length=150, db_index=True)

    def __str__(self):
        return self.githubuser
