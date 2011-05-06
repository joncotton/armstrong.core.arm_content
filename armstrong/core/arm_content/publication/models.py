from django.db import models

from .constants import PUB_STATUS_CHOICES


class PublicationMixin(models.Model):
    pub_date = models.DateTimeField(db_index=True)
    pub_status = models.CharField((u'Publication status'), max_length=1,
        choices=PUB_STATUS_CHOICES, help_text=(
            u'Only published items will appear on the site'))

    class Meta:
        abstract = True
