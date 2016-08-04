from __future__ import unicode_literals
from django.db import models
from django import forms
from django.core.urlresolvers import reverse


class Message(models.Model):
    message_nick = models.CharField(max_length=64)
    message_email = models.EmailField()
    message_content = models.TextField()
    message_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message_email
