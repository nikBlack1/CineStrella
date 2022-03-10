from django.db import models


# Create your models here.

# class Weapon(models.Model):
#     name = models.CharField(max_length=200)
#     type = models.CharField(max_length=200)
#     damage = models.FloatField()
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(upload_to='images')
#
#     def __str__(self):
#         return f'{self.name} ({self.type})'
#
#
# class Vampire(models.Model):
#     name = models.CharField(max_length=200)
#     title = models.CharField(max_length=200)
#     slug = models.SlugField(unique=True)
#     image = models.ImageField(upload_to='images')
#     weapon = models.ForeignKey(Weapon, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.name} -  {self.title}'


# ---------------------- PAGES ----------------------


class Pages(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.name}'


# ---------------------- COMPONENTS ----------------------


class Components(models.Model):
    name = models.CharField(max_length=200)
    identifier = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.name}'


class ComponentText(models.Model):
    component_id = models.ForeignKey(Components, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    content = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.name} ({self.component_id.name})'


class ComponentMedia(models.Model):
    component_id = models.ForeignKey(Components, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    media_src = models.CharField(max_length=2048)

    def __str__(self):
        return f'{self.name} ({self.component_id.name})'


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

    def __str__(self):
        return f'{self.email}'


class UserPersonalData(models.Model):
    user_id = models.IntegerField(primary_key=True)
    auth_id = models.ForeignKey(UserAuthenticationData, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birthday = models.DateField

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Invoice(models.Model):
    invoice_id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(UserPersonalData.user_id, on_delete=models.CASCADE)
    total_price = models.CharField(max_length=200)
    invoice_details = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.invoice_id} {self.user_id}'


# ---------------------- COMPANY DATA ----------------------


class Halls(models.Model):
    hall_name = models.CharField(max_length=2)
    sits_structure = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.hall_name}'


class Movie(models.Model):
    name = models.CharField(max_length=200)
    age_rating = models.IntegerField
    duration = models.IntegerField
    genre = models.CharField(max_length=200)
    cast = models.CharField(max_length=100)
    start_date = models.DateField
    poster = models.ImageField(upload_to='images')
    description = models.CharField(max_length=500)
    sits_structure = ""

    def __str__(self):
        return f'{self.name}'

