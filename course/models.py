from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

class Destination(models.Model):

    place_name = models.CharField(max_length=250, blank=True, null=True,)
    # ID PLACE COUNTRY TIME PRICE
    country = models.CharField(max_length=250, blank=True, null=True,)
    time = models.CharField(max_length=250, blank=True, null=True,)
    price = models.CharField(max_length=250, blank=True, null=True,)

    thumbnail = models.ImageField(upload_to='thumbnails/', null =True, blank=True)
    video = models.FileField(upload_to='videos/', null =True, blank=True)

    slug = models.SlugField(max_length=255, unique=True, blank=False, null=True)

    class Meta:
        db_table = 'destination'

    def __str__(self):
        return self.place

    def destination_name(self):
        return self.place_name
    def destination_country(self):
        return self.country
    def time_of_trip(self):
        return self.time
    def price_of_trip(self):
        return self.price

    def delete(self, *args, **kwargs):
        self.thumbnail.delete()
        self.video.delete()
        super.delete(*args, **kwargs)

class Company(models.Model):

    name = models.CharField(max_length=250, blank=True, null=True,)

    reviews = models.CharField(max_length=250, blank=True, null=True,)

    # link to destination table through place
    place_name = models.ManyToManyField(Destination, related_name='companies')

    class Meta:
        db_table = 'company'

    def __str__(self):
        return self.name

    def company_name(self):
        return self.name

    def company_reviews(self):
        return self.reviews.all()


class UserProfile(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    # Already has first name, last name, email and username

    nationality = models.CharField(max_length=250, blank=True, null=True,)
    address = models.CharField(max_length=250, blank=True, null=True,)
    phone_number = models.CharField(max_length=250, blank=True, null=True,)
    wishlist = models.CharField(max_length=250, blank=True, null=True,)

    class Meta:
        verbose_name_plural = "UserProfiles"
        db_table = 'user_profile'

    def __str__(self):
        return self.username

class Booking(models.Model):

    name = models.CharField(max_length=250, blank=True, null=True,)
    #user_id = models.CharField(max_length=250, blank=True, null=True,)
    #destination_id = models.CharField(max_length=250, blank=True, null=True,)

    # Creating Many to One with Destination ( 1 Destination, many bookings)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    # Creating Many to One with User ( 1 User, many bookings)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    class Meta:
        db_table = 'booking'

    def __str__(self):
        return self.name

    def booking_destination(self):
        return self.destination

    def users_booked(self):
        return self.user

class Booking_status(models.Model):

    name = models.CharField(max_length=250, blank=True, null=True,)
    status = models.CharField(max_length=250, blank=True, null=True, )
    booking = models.ForeignKey(Booking, related_name="bookings", on_delete=models.CASCADE)



# Creating a One to One with Booking
    #   destination_id = models.OneToOneField(Booking, related_name='booking_statuses', on_delete=models.CASCADE)
    #   destination_id not needed


    class Meta:
        db_table = 'booking_status'

    def __str__(self):
        return self.name
