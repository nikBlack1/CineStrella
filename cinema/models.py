import json
from django.db import models


# Create your models here.


# ---------------------- PAGES ----------------------


class Page(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.name}'


# ---------------------- COMPONENTS ----------------------


class Component(models.Model):
    name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class ComponentText(models.Model):
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.name} ({self.component_id.name})'

    class Meta:
        verbose_name_plural = 'ComponentText'


class ComponentMedia(models.Model):
    component_id = models.ForeignKey(Component, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    media_src = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.name} ({self.component_id.name})'

    class Meta:
        verbose_name_plural = 'ComponentMedia'


# ---------------------- USER DATA ----------------------


class UserGroup(models.Model):
    group_id = models.IntegerField
    name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class UserAuthenticationData(models.Model):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=2048)
    user_group_id = models.ForeignKey(UserGroup, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name_plural = 'UserAuthenticationData'


class UserPersonalData(models.Model):
    user_id = models.IntegerField(primary_key=True)
    auth_id = models.ForeignKey(UserAuthenticationData, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    created = models.DateField(auto_now_add=True, auto_now=False, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = 'UserPersonalData'


class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(UserPersonalData, on_delete=models.CASCADE)
    total_price = models.CharField(max_length=200)
    invoice_details = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.invoice_id} {self.user_id}'


# ---------------------- COMPANY DATA ----------------------


def generate_sits(_hall: str):
    sits = []
    row = int()

    if _hall == 'A' or _hall == 'B' or _hall == 'C':
        if _hall == 'A':
            row = 14
        if _hall == 'B':
            row = 12
        if _hall == 'C':
            row = 9

        # sits setting begins here
        for i in range(row):
            i = i + 1
            sits.append("A" + str(i))
        for i in range(row):
            i = i + 1
            sits.append("B" + str(i))
        for i in range(row):
            i = i + 1
            sits.append("C" + str(i))
        for i in range(row):
            i = i + 1
            sits.append("D" + str(i))

        # if hall is "A" or "B" - they get more sits then "C"
        if _hall == 'A' or _hall == 'B':

            for i in range(row):
                i = i + 1
                sits.append("E" + str(i))
            for i in range(row):
                i = i + 1
                sits.append("F" + str(i))

    return sits


class Hall(models.Model):
    HALL_NAME = (
        ('A', 'Hall A'),
        ('B', 'Hall B'),
        ('C', 'Hall C')
    )
    HALL_STRUCTURE = (
        ('Hall A', json.dumps(generate_sits('A'))),
        ('Hall B', json.dumps(generate_sits('B'))),
        ('Hall C', json.dumps(generate_sits('C')))
    )

    hall_name = models.CharField(choices=HALL_NAME, max_length=30)
    hall_structure = models.CharField(max_length=10000, editable=False)

    @property
    def get_sits(self):
        if self.hall_name == 'Hall A':
            return generate_sits(json.dumps(generate_sits('A')))
        if self.hall_name == 'Hall B':
            return generate_sits(json.dumps(generate_sits('B')))
        if self.hall_name == 'Hall C':
            return generate_sits(json.dumps(generate_sits('C')))

    def __str__(self):
        return f'{self.hall_name}'


class Movie(models.Model):

    MOVIE_STATUS = (
        ('on', 'Ongoing'),
        ('com', 'Coming'),
        ('off', 'Past'),
    )
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    age_rating = models.IntegerField()
    duration = models.IntegerField()
    genre = models.CharField(max_length=200)
    cast = models.CharField(max_length=100)
    poster = models.ImageField(upload_to='images/posters')
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=15, choices=MOVIE_STATUS, default=MOVIE_STATUS[1])

    def __str__(self):
        return f'{self.name}'


class Event(models.Model):
    end_default = "for this Event was assigned yet"

    EVENT_DAYS = (
        ('mon', 'Monday'),
        ('tu', 'Tuesday'),
        ('we', 'Wednesday'),
        ('th', 'Thursday'),
        ('fr', 'Friday'),
    )
    days_default = "No day "

    EVENT_TIME_SLOT = (
        ('1', '10:00'),
        ('2', '13:30'),
        ('3', '17:00'),
        ('4', '20:30'),
        ('5', '00:00'),
    )
    time_default = "No time "

    EVENT_TYPE = (
        ('2d', '2D'),
        ('3d', '3D'),
    )

    hall_default = "No hall "

    # id = models.IntegerField(primary_key=True)
    week_day = models.CharField(max_length=10, choices=EVENT_DAYS, default=days_default + end_default)
    time_slot = models.CharField(max_length=10, choices=EVENT_TIME_SLOT, default=time_default + end_default)
    type = models.CharField(max_length=2, choices=EVENT_TYPE, default=EVENT_TYPE[0])
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE)

    film = models.ForeignKey(Movie, on_delete=models.CASCADE)

    start_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)
    end_date = models.DateField(auto_now_add=False, auto_now=False, blank=True)

    # Taking the hall map and creating a dictionary with status-values for the sits out of it
    # default_sits_map = dict.fromkeys(hall.get_sits(), 'Empty')

    def __str__(self):
        return f'{self.film.name}'

