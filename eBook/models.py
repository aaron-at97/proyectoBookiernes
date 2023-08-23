from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Book(models.Model):
    id_book = models.CharField(blank=False, null=False, max_length=64)
    title = models.CharField(blank=False, null=False, max_length=64)
    genere = models.CharField(blank=False, null=True, max_length=64)
    body = models.TextField(blank=False)
    deleted = models.BooleanField(default=False, null=False, blank=False)
    date = models.DateField(default=date.today)

    STATUS = (
        (0, 'Presented'),
        (1, 'Accepted'),
        (2, 'Denied'),
        (3, 'Revision'),
        (4, 'Pending images'),
        (5, 'Images accepted'),
        (6, 'Images denied'),
        (7, 'Pending layout'),
        (8, 'Layout accepted'),
        (9, 'Layout denied'),
        (10, 'Translate'),
        (11, 'Published'),
    )

    state = models.PositiveIntegerField(default=0, choices=STATUS)

    def __str__(self):
        return u"%s" % self.title

    def __unicode__(self):
        return u"%s" % self.title


class Notification(models.Model):
    book_key = models.ForeignKey(Book, on_delete=models.CASCADE)
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
    name = models.CharField(blank=False, null=False, max_length=20)

    ROLES = (
        ('Writer', 'Writer'),
        ('Editor', 'Editor'),
        ('Editor in chief', 'Editor in chief'),
        ('Chief designer', 'Chief designer'),
        ('Designer', 'Designer'),
        ('CTO', 'CTO'),
        ('Developer', 'Developer'),
        ('Client', 'Client'),
    )

    role = models.CharField('Role', blank=False, null=False, choices=ROLES, max_length=25)
    notification = models.ManyToManyField(Notification, blank=True)

    class Meta:
        abstract = True

    def get_homepage(self):
        return "index/"


class Writer(Staff):
    books = models.ManyToManyField(Book, blank=True, related_name="escrip")

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name


class Editor(Staff):
    assigned = models.ManyToManyField(Book, blank=True)

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name


class EditorChief(Staff):

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name


class ChiefDesigner(Staff):

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name


class Designer(Staff):

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name


class CTO(Staff):

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name


class Developer(Staff):

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name


class Clients(Staff):
    nombre = models.CharField(blank=False, null=False, max_length=64)
    apellido = models.CharField(blank=False, null=False, max_length=64)
    telefon = models.IntegerField()
    codi_postal = models.IntegerField()
    correo = models.CharField(blank=False, null=False, max_length=64)
    direccion = models.CharField(blank=False, null=False, max_length=64)

    def __str__(self):
        return u"%s" % self.name

    def __unicode__(self):
        return u"%s" % self.name
