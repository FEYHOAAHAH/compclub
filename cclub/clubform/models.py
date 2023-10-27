from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class Form(models.Model):
    def validate_name(self):
        if any(char.isdigit() for char in self):
            raise ValidationError("Поле 'name' не должно содержать цифры.")

    name = models.CharField(max_length=30, validators=[validate_name])

    def validate_surname(self):
        if any(char.isdigit() for char in self):
            raise ValidationError("Поле 'surname' не должно содержать цифры.")

    surname = models.CharField(max_length=30, validators=[validate_surname])

    def validate_age(self):
        if self < 18:
            raise ValidationError("Вам должно быть 18 или больше лет", code='odd', params={'age': self})

    age = models.IntegerField(validators=[validate_age])

    CHOICE = (('m', 'male'),
              ('f', 'female'),
              ('o', 'other'),
              ('nd', 'non defined'),
              ('ah', 'apache helicopter'))

    gender = models.CharField(max_length=100, choices=CHOICE)

    class ValidateEmail:
        def __call__(self, value):
            email_validator = EmailValidator("Введите корректный адрес электронной почты.")
            email_validator(value)

        def __eq__(self, other):
            return isinstance(other, self.__class__)

    email = models.EmailField(validators=[ValidateEmail()])
    schedule_time = models.TimeField()
    phone_number = PhoneNumberField()

    class NoDigitsValidator:

        def __call__(self, value):
            if any(char.isdigit() for char in value):
                raise ValidationError("Имя пользователя не может содержать цифры.")

        def __eq__(self, other):
            return isinstance(other, self.__class__)

    username = models.CharField(max_length=100, validators=[NoDigitsValidator()])

    class NoCyrillicValidator:
        def __call__(self, value):
            if any(ord(char) > 127 for char in value):
                raise ValidationError("Поле 'favourite_game' не должно содержать кириллицу.")

        def __eq__(self, other):
            return isinstance(other, self.__class__)

    favourite_game = models.CharField(max_length=100, validators=[NoCyrillicValidator()])

    CHOICES = (('YOUTUBE', 'Youtube'),
               ('INSTAGRAM', 'Instagram'),
               ('FRIENDS', 'Friends'),
               ('X', 'X'))

    place_of_notice = models.CharField(max_length=60, choices=CHOICES)
