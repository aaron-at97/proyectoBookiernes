
from django.db import models
from django.contrib.auth.models import User
from datetime import date
# Create your models here.


class Notification(models.Model):
    book_key = models.ForeignKey(Book, related_name='About', on_delete=models.CASCADE)
    concept = models.TextField(blank=False, null=False, max_length=100)
    seen = models.BooleanField(default=False)
    date = models.DateField(default=date.today)

    def __str__(self):
        return u"%s" % self.concept

    def __unicode__(self):
        return u"%s" % self.concept


class Staff(models.Model):
    staff_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLES = (
        ('Writer', 'Writer')
        ('Editor', 'Editor'),
        ('Editor in chief', 'Editor in chief'),
        ('Chief designer', 'Chief designer'),
        ('Designer', 'Designer'),
        ('CTO', 'CTO'),
        ('Developer', 'Developer'),
    )

    name = models.CharField(blank=False, null=False, max_length=20)
    role = models.CharField('Role', blank=False, null=False, choices=ROLES, max_length=25)
    notification = models.ManyToManyField(Notification, blank=True)

    class Meta:
        abstract = True


class Book(models.Model):
    id_book = models.CharField(blank=False, null=False, max_length=64)
    title = models.CharField(blank=False, null=False, max_length=64)
    body = models.TextField(blank=False)
    deleted = models.BooleanField(default=False, null=False, blank=False)

    editor = models.ForeignKey(Staff, related_name='edited_by')
    writer = models.ForeignKey(Staff, related_name='images_by', blank=True, null=True)
    editor_chief = models.ForeignKey(Staff, related_name='validated_by', blank=True)
    designer = models.ForeignKey(Staff, blank=True, null=True)
    images = models.ManyToManyField(Staff, blank=True)

    STATUS = (
        (1, 'Revision'),
        (2, 'Accepted'),
        (3, 'Denied'),
        (4, 'Pending images'),
        (5, 'Images accepted'),
        (6, 'Images denied'),
        (7, 'Pending layout'),
        (8, 'Layout accepted'),
        (9, 'Layout denied'),
        (10, 'Translate'),
        (11, 'Published'),
    )

    state = models.PositiveIntegerField(default=1, choices=STATUS)

    def __str__(self):
        return u"%s" % self.title

    def __unicode__(self):
        return u"%s" % self.title










