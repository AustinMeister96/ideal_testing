from django.db import models
import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.conf import settings

""" class User(AbstractUser):


    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('data_entry', 'Data Entry'),
        ('lab_processing', 'Lab'),
    )

    role = models.CharField(max_length=200, choices=ROLE_CHOICES, default='data_entry')
    
    def __str__(self):              # __unicode__ on Python 2
        return self.username """
class UserAccounts(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    email = models.EmailField()
    def __str__(self):    
        return self.username + ' ' + self.first_name + ' ' + self.last_name
    


class Participant(models.Model):
    participant_number = models.CharField(primary_key=True, unique=True, max_length=7)

    def __str__(self):
        return self.participant_number


class testParticipant(models.Model):
    number = models.IntegerField()
    birthday = models.DateField()
    email = models.EmailField()
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    house_address = models.TextField()
    UserAccounts = models.ManyToManyField(UserAccounts, blank=True)


# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    

    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field='pub_date'
    was_published_recently.boolean=True 
    was_published_recently.short_description='Published recently?'
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
    

    
#create a blood_collection class with the following attributes: Ideal_participant_num, Date_of_birth, Visit_type, Comments , Date_of_collection, Collected_by, Time_collected, Processing_start_time, Time_placed_freezer, Freezer_box_num , Y_Plasma_barcode_1, Y_Plasma_barcode_2, P_plasma_barcode_1 , p_plasma_barcode_2, r_rbc_barcode_1, r_rbc_barcode_2, y_bottom_barcode_1, y_bottom_barcode_2, p_bottom_barcode_1, p_bottom_barcode_2
class Blood_Collection(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    ideal_participant_num = models.IntegerField(default=0)
    date_of_birth = models.DateTimeField('date of birth')
    visit_type = models.CharField(max_length=200)
    comments = models.CharField(max_length=200)
    date_of_collection = models.DateTimeField('date of collection')
    collected_by = models.CharField(max_length=200)
    time_collected = models.DateTimeField('time collected')
    processing_start_time = models.DateTimeField('processing start time')
    time_placed_freezer = models.DateTimeField('time placed freezer')
    freezer_box_num = models.IntegerField(default=0)
    y_plasma_barcode_1 = models.IntegerField(default=0)
    y_plasma_barcode_2 = models.IntegerField(default=0)
    p_plasma_barcode_1 = models.IntegerField(default=0)
    p_plasma_barcode_2 = models.IntegerField(default=0)
    r_rbc_barcode_1 = models.IntegerField(default=0)
    r_rbc_barcode_2 = models.IntegerField(default=0)
    y_bottom_barcode_1 = models.IntegerField(default=0)
    y_bottom_barcode_2 = models.IntegerField(default=0)
    p_bottom_barcode_1 = models.IntegerField(default=0)
    p_bottom_barcode_2 = models.IntegerField(default=0)
    
    def __str__(self):
        return self.ideal_participant_num

#create a breath_collection class with the following attributes: Collection_date, collection_time, collected_by, location, brush_teeth, brush_teeth_time, mouthwash, face_cream, perfume_cologne, deodorant, smoke_exposure, fuel_car, arrival_type, last_meal, last_meal_time, last_drink, last_drink_time, short_of_breath, fever, cough, cold, no_symptoms, halitosis, reciva_barcode, tennax_number, casper_flow, collection_start_time, collection_stop_time, collection_duration, breathing_rate, aborted, incomplete, declined, room_air_barcode, room_air_tennax, casper_barcode, casper_tennax, notes
class Breath_Collection(models.Model):
    mask_type = (
        ('Mask', 'Mask'),
        ('Mouthpiece', 'Mouthpiece'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    collection_date = models.DateTimeField()
    collection_time = models.TimeField('collection time')
    collected_by = models.CharField(max_length=200, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)
    brush_teeth = models.BooleanField(default=False, null=True, blank=True)
    brush_teeth_time = models.TimeField('brush teeth time', null=True, blank=True)
    mouthwash = models.BooleanField(default=False, null=True, blank=True)
    face_cream = models.BooleanField(default=False, null=True, blank=True)
    perfume_cologne = models.BooleanField(default=False, null=True, blank=True)
    deodorant = models.BooleanField(default=False, null=True, blank=True)
    smoke_exposure = models.BooleanField(default=False, null=True, blank=True)
    fuel_car = models.BooleanField(default=False, null=True, blank=True)
    arrival_type = models.CharField(max_length=200, null=True, blank=True)
    last_meal = models.CharField(max_length=200, null=True, blank=True)
    last_meal_time = models.TimeField('last meal time', null=True, blank=True)
    last_drink = models.CharField(max_length=200, null=True, blank=True)
    last_drink_time = models.TimeField('last drink time', null=True, blank=True)
    short_of_breath = models.BooleanField(default=False, null=True, blank=True)
    fever = models.BooleanField(default=False, null=True, blank=True)
    cough = models.BooleanField(default=False, null=True, blank=True)
    cold = models.BooleanField(default=False, null=True, blank=True)
    no_symptoms = models.BooleanField(default=False, null=True, blank=True)
    halitosis = models.BooleanField(default=False, null=True, blank=True)
    tennax_number = models.IntegerField(null=True, blank=True)
    casper_flow = models.IntegerField(default=0, null=True, blank=True)
    collection_start_time = models.TimeField('collection start time', null=True, blank=True)
    collection_stop_time = models.TimeField('collection stop time', null=True, blank=True)
    collection_duration = models.IntegerField(default=0, null=True, blank=True)
    breathing_rate = models.IntegerField(default=0, null=True, blank=True)
    aborted = models.BooleanField(default=False, null=True, blank=True)
    incomplete = models.BooleanField(default=False, null=True, blank=True)
    declined = models.BooleanField(default=False, null=True, blank=True)
    room_air_tennax = models.CharField(max_length=6, null=True, blank=True)
    casper_tennax = models.CharField(max_length=6, null=True, blank=True)
    notes = models.CharField(max_length=200, null=True, blank=True)
    casper_caps = models.IntegerField(default=0, null=True, blank=True)
    volume_collected = models.CharField(default=0, max_length=7, null=True, blank=True)
    birth_control = models.BooleanField(default=False, null=True, blank=True)
    birth_control_duration = models.IntegerField(default=0, null=True, blank=True)
    menopausal = models.BooleanField(default=False, null=True, blank=True)
    hrt_menopause = models.BooleanField(default=False, null=True, blank=True)
    grt_menopause_duration = models.IntegerField(default=0, null=True, blank=True)
    gender_affirming_surgery = models.BooleanField(default=False, null=True, blank=True)
    gender_affirming_type = models.CharField(max_length=200, null=True, blank=True)
    inhaled_medication = models.BooleanField(default=False, null=True, blank=True)
    inhaled_medication_type = models.CharField(max_length=200, null=True, blank=True)
    inhaled_medication_brand = models.CharField(max_length=200, null=True, blank=True)
    inhaled_medication_name = models.CharField(max_length=200, null=True, blank=True)
    pneumonia = models.BooleanField(default=False, null=True, blank=True)
    smoke_exposure = models.BooleanField(default=False, null=True, blank=True)
    smoke_exposure_type = models.CharField(max_length=200, null=True, blank=True)
    room_air_collection_time = models.TimeField('room air collection time', null=True, blank=True)
    casper_collection_time = models.TimeField('casper collection time', null=True, blank=True)
    reciva_mouthpiece_type = models.CharField(max_length=10, choices=mask_type, null=True, blank=True)


    def __str__(self):
        return self.location

class lab_processing(models.Model):

    lab_processing_upload = models.FileField(upload_to='lab_processing', null=True, blank=True)



    def __str__(self):
        return self.int_std_sln


class lab_processing2(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    da_hs_blk_spiked = models.TextField(max_length=20)
    da_hs_blk_int_std = models.TextField(max_length=20)
    da_hs_blk_method = models.TextField(max_length=20)
    da_hs_blk_date = models.TextField(max_length=20)
    da_hs_blk_wbrush_spiked = models.TextField(max_length=20)
    da_hs_blk_wbrush_int_std = models.TextField(max_length=20)
    da_hs_blk_wbrush_method = models.TextField(max_length=20)
    da_hs_blk_wbrush_date = models.TextField(max_length=20)
    da_hs_l_spiked = models.TextField(max_length=20)
    da_hs_l_int_std = models.TextField(max_length=20)
    da_hs_l_method = models.TextField(max_length=20)
    da_hs_l_date = models.TextField(max_length=20)
    da_hs_r_spiked = models.TextField(max_length=20)
    da_hs_r_int_std = models.TextField(max_length=20)
    da_hs_r_method = models.TextField(max_length=20)
    da_hs_r_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    da_hs_r_wbrush_spiked = models.TextField(max_length=20)
    da_hs_r_wbrush_int_std = models.TextField(max_length=20)
    da_hs_r_wbrush_method = models.TextField(max_length=20)
    da_hs_r_wbrush_date = models.TextField(max_length=20)
    da_hs_l_wbrush_spiked = models.TextField(max_length=20)
    da_hs_l_wbrush_int_std = models.TextField(max_length=20)
    da_hs_l_wbrush_method = models.TextField(max_length=20)
    da_hs_l_wbrush_date = models.TextField(max_length=20)
    
    def __str__(self):
        return self.da_hs_l_int_std



class Exposure(models.Model):

    yes_no_dk = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Dont Know', 'Dont Know'),
        ('N/A', 'N/A'),
    )
    total_exposure = (
        ('No or almost no exposure = 1', 'No or almost no exposure = 1'),
        ('Light exposure = 2', 'Light exposure = 2'),
        ('Moderate exposure = 3', 'Moderate exposure = 3'),
        ('Heavy exposure = 4', 'Heavy exposure = 4'),
        ('N/A', 'N/A'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    total_exposure = models.TextField(max_length=30, choices=total_exposure)
    asbestos_exposure = models.TextField(max_length=100, choices=yes_no_dk)
    asbestos_exposure_duration = models.TextField(max_length=20)
    asbestos_exposure_age = models.TextField(max_length=20)
    silica_exposure_age = models.TextField(max_length=20)
    silica_exposure_duration = models.TextField(max_length=20)
    silica_exposure = models.TextField(max_length=20, choices=yes_no_dk)
    diesel = models.TextField(max_length=20)
    diesel_duration = models.TextField(max_length=20)
    diesel_exposure_age = models.TextField(max_length=20)
    radon = models.TextField(max_length=20)
    radon_duration = models.TextField(max_length=20)
    radon_exposure_age = models.TextField(max_length=20)
    cadmium = models.TextField(max_length=20)
    cadmium_duration = models.TextField(max_length=20)
    cadmium_exposure_age = models.TextField(max_length=20)
    chromium = models.TextField(max_length=20)
    chromium_duration = models.TextField(max_length=20)
    chromium_exposure_age = models.TextField(max_length=20)
    coal = models.TextField(max_length=20)
    coal_duration = models.TextField(max_length=20)
    coal_exposure_age = models.TextField(max_length=20)
    arsenic = models.TextField(max_length=20)
    arsenic_duration = models.TextField(max_length=20)
    arsenic_exposure_age = models.TextField(max_length=20)
    nickel = models.TextField(max_length=20)
    nickel_duration = models.TextField(max_length=20)
    nickel_exposure_age = models.TextField(max_length=20)
    plutonium = models.TextField(max_length=20)
    plutonium_duration = models.TextField(max_length=20)
    plutonium_exposure_age = models.TextField(max_length=20)
    beryllium = models.TextField(max_length=20)
    beryllium_duration = models.TextField(max_length=20)
    beryllium_exposure_age = models.TextField(max_length=20)
    ether = models.TextField(max_length=20)
    ether_duration = models.TextField(max_length=20)
    ether_exposure_age = models.TextField(max_length=20)
    soot = models.TextField(max_length=20)
    soot_duration = models.TextField(max_length=20)
    soot_exposure_age = models.TextField(max_length=20)
    welding = models.TextField(max_length=20)
    welding_duration = models.TextField(max_length=20)
    welding_exposure_age = models.TextField(max_length=20)
    radiation = models.TextField(max_length=20)
    radiation_duration = models.TextField(max_length=20)
    radiation_exposure_age = models.TextField(max_length=20)
    munitions = models.TextField(max_length=20)
    munitions_duration = models.TextField(max_length=20)
    munitions_exposure_age = models.TextField(max_length=20)
    warfare = models.TextField(max_length=20)
    warfare_duration = models.TextField(max_length=20)
    warfare_exposure_age = models.TextField(max_length=20)
    acheson = models.TextField(max_length=20)
    acheson_duration = models.TextField(max_length=20)
    acheson_exposure_age = models.TextField(max_length=20)
    aluminum = models.TextField(max_length=20)
    aluminum_duration = models.TextField(max_length=20)
    aluminum_exposure_age = models.TextField(max_length=20)
    coal_gasification = models.TextField(max_length=20)
    coal_gasification_duration = models.TextField(max_length=20)
    coal_gasification_exposure_age = models.TextField(max_length=20)
    coke = models.TextField(max_length=20)
    coke_duration = models.TextField(max_length=20)
    coke_exposure_age = models.TextField(max_length=20)
    mining = models.TextField(max_length=20)
    mining_duration = models.TextField(max_length=20)
    mining_exposure_age = models.TextField(max_length=20)
    iron = models.TextField(max_length=20)
    iron_duration = models.TextField(max_length=20)
    sand = models.TextField(max_length=20)
    sand_duration = models.TextField(max_length=20)
    sand_exposure_age = models.TextField(max_length=20)
    def __str__(self):
        return self.total_exposure 

    
class Exposure2(models.Model):
    yes_no_dk = (
    ('Yes', 'Yes'),
    ('No', 'No'),
    ('Dont Know', 'Dont Know'),
    ('N/A', 'N/A'),
    )
    cooking_freq = (
    ('N/A', 'N/A'),
    ('Everyday', 'Everyday'),
    ('Every Week', 'Every Week'),
    ('Every Month', 'Every Month'),
    )
    cooking_fuel = (
        ('Wood or Charcoal', 'Wood or Charcoal'),
        ('Bitumous, Briquettes or Kerosene', 'Bitumous, Briquettes or Kerosene'),
        ('Gas (liquefied petroleum, natural gas)', 'Gas (liquefied petroleum, natural gas)'),
        ('Electricity', 'Electricity'),
        ('Other', 'Other'),
    )
    cooking_oils = (
        ('Animal Fat Store bought', 'Animal Fat Store bought'),
        ('Animal Fat Homemade', 'Animal Fat Homemade'),
        ('Vegetable Oil', 'Vegetable Oil'),
        ('Other', 'Other'),
    )
    total_exposure = (
        ('No or almost no exposure = 1', 'No or almost no exposure = 1'),
        ('Light exposure = 2', 'Light exposure = 2'),
        ('Moderate exposure = 3', 'Moderate exposure = 3'),
        ('Heavy exposure = 4', 'Heavy exposure = 4'),
        ('N/A', 'N/A'),
    )

    eating_freq = (
        ('Never', 'Never'),
        ('Less than 1 time per month', 'Less than 1 time per month'),
        ('1 - 3 times per month', '1 - 3 times per month'),
        ('1 - 2 times per week', '1 - 2 times per week'),
        ('3 - 6 times per week', '3 - 6 times per week'),
        ('7 or more times per week', '7 or more times per week'),
    )

    cooking_location_choices = (
        ('Inside the house in a separate kitchen', 'Inside the house in a separate kitchen'),
        ('Inside the house in the central living space', 'Inside the house in the central living space'),
        ('Outside the house', 'Outside the house'),
        ('Inside and outside the house', 'Inside and outside the house'),
    )

    cooking_appliance_choices = (
        ('Open Window', 'Open Window'),
        ('Chimney', 'Chimney'),
        ('Exhaust Fan', 'Exhaust Fan'),
        ('Partially open to outside', 'Partially open to outside'),
    )

    frequency_in_cooking_location_choices = (
        ('All of the time', 'All of the time'),
        (' Most of the time', ' Most of the time'),
        ('Some of the time', 'Some of the time'),
        ('Never', 'Never'),
        ("Don’t know", "Don’t know"),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    total_exposure = models.TextField(max_length=40, choices=total_exposure)
    asbestos_exposure = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    asbestos_exposure_duration = models.TextField(max_length=20, blank=True, null=True)
    asbestos_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    silica_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    silica_exposure_duration = models.TextField(max_length=20, blank=True, null=True)
    silica_exposure = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    diesel = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    diesel_duration = models.TextField(max_length=20, blank=True, null=True)
    diesel_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    radon = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    radon_duration = models.TextField(max_length=20, blank=True, null=True)
    radon_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    cadmium = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    cadmium_duration = models.TextField(max_length=20, blank=True, null=True)
    cadmium_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    chromium = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    chromium_duration = models.TextField(max_length=20, blank=True, null=True)
    chromium_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    coal = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    coal_duration = models.TextField(max_length=20, blank=True, null=True)
    coal_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    arsenic = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    arsenic_duration = models.TextField(max_length=20, blank=True, null=True)
    arsenic_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    nickel = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    nickel_duration = models.TextField(max_length=20, blank=True, null=True)
    nickel_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    plutonium = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    plutonium_duration = models.TextField(max_length=20, blank=True, null=True)
    plutonium_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    beryllium = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    beryllium_duration = models.TextField(max_length=20, blank=True, null=True)
    beryllium_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    ether = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    ether_duration = models.TextField(max_length=20, blank=True, null=True)
    ether_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    soot = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    soot_duration = models.TextField(max_length=20, blank=True, null=True)
    soot_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    welding = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    welding_duration = models.TextField(max_length=20, blank=True, null=True)
    welding_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    radiation = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    radiation_duration = models.TextField(max_length=20, blank=True, null=True)
    radiation_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    munitions = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    munitions_duration = models.TextField(max_length=20, blank=True, null=True)
    munitions_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    warfare = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    warfare_duration = models.TextField(max_length=20, blank=True, null=True)
    warfare_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    acheson = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    acheson_duration = models.TextField(max_length=20, blank=True, null=True)
    acheson_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    aluminum = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    aluminum_duration = models.TextField(max_length=20, blank=True, null=True)
    aluminum_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    coal = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    coal_duration = models.TextField(max_length=20, blank=True, null=True)
    coal_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    coke = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    coke_duration = models.TextField(max_length=20, blank=True, null=True)
    coke_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    coal_gasification = models.TextField(max_length=20, choices=yes_no_dk, blank=True, null=True, default='No')
    coal_gasification_duration = models.TextField(max_length=20, blank=True, null=True)
    coal_gasification_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    sulfur = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, null=True, default='No')
    sulfur_duration = models.TextField(max_length=20, blank=True, null=True)
    sulfur_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    mining = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    mining_duration = models.TextField(max_length=20, blank=True, null=True)
    mining_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    iron = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    iron_duration = models.TextField(max_length=20, blank=True, null=True)
    iron_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    painting = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    painting_duration = models.TextField(max_length=20, blank=True, null=True)
    painting_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    rubber = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    rubber_duration = models.TextField(max_length=20, blank=True, null=True)
    rubber_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    burn_pits = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    burn_pits_duration = models.TextField(max_length=20, blank=True, null=True)
    burn_pits_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    oil_fires = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    oil_fires_duration = models.TextField(max_length=20, blank=True, null=True)
    oil_fires_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    sulfur_fires = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    sulfur_fires_duration = models.TextField(max_length=20, blank=True, null=True)
    sulfur_fires_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    atsugi = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    atsugi_duration = models.TextField(max_length=20, blank=True, null=True)
    atsugi_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    sand_storms = models.TextField(max_length=10, choices=yes_no_dk,  blank=False, default='No')
    sand_storms_duration = models.TextField(max_length=20, blank=True, null=True)
    sand_storms_exposure_age = models.TextField(max_length=20, blank=True, null=True)
    job_held = models.TextField(max_length=20, blank=True, null=True)
    job_held_duration = models.TextField(max_length=20, blank=True, null=True)
    job_held_industry = models.TextField(max_length=20, blank=True, null=True)
    job_held_2 = models.TextField(max_length=20, blank=True, null=True)
    job_held_2_duration = models.TextField(max_length=20, blank=True, null=True)
    job_held_2_industry = models.TextField(max_length=20, blank=True, null=True)
    job_held_3 = models.TextField(max_length=20, blank=True, null=True)
    job_held_3_duration = models.TextField(max_length=20, blank=True, null=True)
    job_held_3_industry = models.TextField(max_length=20, blank=True, null=True)
    duration_outdoor_pollution = models.TextField(max_length=20, blank=True, null=True)
    duraiton_indoor_pollution = models.TextField(max_length=20, blank=True, null=True)
    cooking_location = models.TextField(max_length=128, choices=cooking_location_choices, blank=False, null=False)
    cooking_appliances = models.CharField(max_length=30, choices=cooking_appliance_choices, blank=True, null=True)
    cooking = models.BooleanField()
    frequency_in_cooking_location = models.TextField(max_length=30, choices=frequency_in_cooking_location_choices, blank=True, null=True)
    kitchen_range = models.BooleanField()
    kitchen_range_age = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_frequency = models.TextField(max_length=25, choices=cooking_freq, blank=True, null=True)
    cooking_0_20_frequency_times = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_fuel = models.TextField(max_length=40, choices=cooking_fuel, blank=True, null=True)
    cooking_0_20_fuel_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_cooking_oil = models.TextField(max_length=25,choices=cooking_oils, blank=True, null=True)
    cooking_0_20_cooking_oil_store = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_cooking_oil_homemade = models.TextField(max_length=2, blank=True, null=True)
    cooking_0_20_cooking_oil_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_saute_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_fry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_0_20_deepfry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_frequency = models.TextField(max_length=25, choices=cooking_freq, blank=True, null=True)
    cooking_21_40_frequency_times = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_fuel = models.TextField(max_length=40, choices=cooking_fuel, blank=True, null=True)
    cooking_21_40_fuel_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_cooking_oil = models.TextField(max_length=25,choices=cooking_oils, blank=True, null=True)
    cooking_21_40_cooking_oil_store = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_cooking_oil_homemade = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_cooking_oil_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_saute_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_fry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_21_40_deepfry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_frequency = models.TextField(max_length=25, choices=cooking_freq, blank=True, null=True)
    cooking_41_60_frequency_times = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_fuel = models.TextField(max_length=40, choices=cooking_fuel, blank=True, null=True)
    cooking_41_60_fuel_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_cooking_oil = models.TextField(max_length=25,choices=cooking_oils, blank=True, null=True)
    cooking_41_60_cooking_oil_store = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_cooking_oil_homemade = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_cooking_oil_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_saute_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_fry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_41_60_deepfry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_frequency = models.TextField(max_length=25, choices=cooking_freq, blank=True, null=True)
    cooking_61_above_frequency_times = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_fuel = models.TextField(max_length=40, choices=cooking_fuel, blank=True, null=True)
    cooking_61_above_fuel_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_cooking_oil = models.TextField(max_length=25,choices=cooking_oils, blank=True, null=True)
    cooking_61_above_cooking_oil_store = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_cooking_oil_homemade = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_cooking_oil_other = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_saute_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_fry_frequency = models.TextField(max_length=20, blank=True, null=True)
    cooking_61_above_deepfry_frequency = models.TextField(max_length=20, blank=True, null=True)
    processed_meat_frequency = models.TextField(max_length=50, choices=eating_freq, blank=True, null=True)
    red_meat_frequency = models.TextField(max_length=50, choices=eating_freq, blank=True, null=True)

    def __str__(self):
        return self.user.username

class Exposure3(models.Model):
    house_types = (
        ('Single Family', 'Single Family'),
        ('Duplex', 'Duplex'),
        ('Townhouse', 'Townhouse'),
        ('Apartment', 'Apartment'),
        ('Basement Suite', 'Basement Suite'),
        ('Other', 'Other'),
        ("Don’t Know", "Don’t Know"),
    )

    primary_heat_sources = (
        ('Electric', 'Electric'),
        ('Wood', 'Wood'),
        ('Natural Gas / Propane', 'Natural Gas / Propane'),
        ('Kerosene', 'Kerosene'),
        ('Agriculture / Crop ', 'Agriculture / Crop '),
        ('Gobar gas', 'Gobar gas'),
        ('Coal', 'Coal'),
        ('Animal dung', 'Animal dung'),
        ('Shrub / Grass', 'Shrub / Grass'),
        ('Other', 'Other'),
        ('None', 'None'),
        ('Don’t Know', 'Don’t Know'),
    )

    water_sources = (
        ('Municipal treated', 'Municipal treated'),
        ('Private well (dug)', 'Private well (dug)'),
        ('Private well (drilled)', 'Private well (drilled)'),
        ('Other', 'Other'),
        ('Don’t Know', 'Don’t Know'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    home_1_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_1_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_1_country = models.TextField(max_length=20, blank=True, null=True)
    home_1_city = models.TextField(max_length=20, blank=True, null=True)
    home_1_province = models.TextField(max_length=20, blank=True, null=True)
    home_1_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_1_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_1_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_1_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_1_housing_type = models.TextField(max_length=20, choices=house_types, blank=True, null=True)
    home_1_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_1_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_1_water_src = models.TextField(max_length=25, choices=water_sources, blank=True, null=True)
    home_1_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_1_heat_src = models.TextField(max_length=30, choices=primary_heat_sources, blank=True, null=True)
    home_1_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_2_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_2_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_2_country = models.TextField(max_length=20, blank=True, null=True)
    home_2_city = models.TextField(max_length=20, blank=True, null=True)
    home_2_province = models.TextField(max_length=20, blank=True, null=True)
    home_2_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_2_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_2_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_2_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_2_housing_type = models.TextField(max_length=20,  choices=house_types, blank=True, null=True)
    home_2_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_2_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_2_water_src = models.TextField(max_length=25, choices=water_sources, blank=True, null=True)
    home_2_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_2_heat_src = models.TextField(max_length=30, choices=primary_heat_sources,blank=True, null=True)
    home_2_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_3_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_3_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_3_country = models.TextField(max_length=20, blank=True, null=True)
    home_3_city = models.TextField(max_length=20, blank=True, null=True)
    home_3_province = models.TextField(max_length=20, blank=True, null=True)
    home_3_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_3_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_3_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_3_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_3_housing_type = models.TextField(max_length=20, choices=house_types,  blank=True, null=True)
    home_3_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_3_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_3_water_src = models.TextField(max_length=25, choices=water_sources, blank=True, null=True)
    home_3_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_3_heat_src = models.TextField(max_length=30, choices=primary_heat_sources, blank=True, null=True)
    home_3_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_4_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_4_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_4_country = models.TextField(max_length=20, blank=True, null=True)
    home_4_city = models.TextField(max_length=20, blank=True, null=True)
    home_4_province = models.TextField(max_length=20, blank=True, null=True)
    home_4_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_4_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_4_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_4_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_4_housing_type = models.TextField(max_length=20, choices=house_types,  blank=True, null=True)
    home_4_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_4_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_4_water_src = models.TextField(max_length=25, choices=water_sources, blank=True, null=True)
    home_4_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_4_heat_src = models.TextField(max_length=30, choices=primary_heat_sources, blank=True, null=True)
    home_4_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_5_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_5_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_5_country = models.TextField(max_length=20, blank=True, null=True)
    home_5_city = models.TextField(max_length=20, blank=True, null=True)
    home_5_province = models.TextField(max_length=20, blank=True, null=True)
    home_5_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_5_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_5_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_5_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_5_housing_type = models.TextField(max_length=20, choices=house_types,  blank=True, null=True)
    home_5_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_5_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_5_water_src = models.TextField(max_length=25, choices=water_sources, blank=True, null=True)
    home_5_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_5_heat_src = models.TextField(max_length=30, choices=primary_heat_sources, blank=True, null=True)
    home_5_heat_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_6_start_yr = models.TextField(max_length=20, blank=True, null=True)
    home_6_end_yr = models.TextField(max_length=20, blank=True, null=True)
    home_6_country = models.TextField(max_length=20, blank=True, null=True)
    home_6_city = models.TextField(max_length=20, blank=True, null=True)
    home_6_province = models.TextField(max_length=20, blank=True, null=True)
    home_6_postal_code = models.TextField(max_length=20, blank=True, null=True)
    home_6_street_address = models.TextField(max_length=20, blank=True, null=True)
    home_6_map_coordinates = models.TextField(max_length=20, blank=True, null=True)
    home_6_avg_monthly_stay = models.TextField(max_length=20, blank=True, null=True)
    home_6_housing_type = models.TextField(max_length=20, choices=house_types,  blank=True, null=True)
    home_6_housing_type_other = models.TextField(max_length=20, blank=True, null=True)
    home_6_trucks = models.TextField(max_length=20, blank=True, null=True)
    home_6_water_src = models.TextField(max_length=25, choices=water_sources, blank=True, null=True)
    home_6_water_src_other = models.TextField(max_length=20, blank=True, null=True)
    home_6_heat_src = models.TextField(max_length=30, choices=primary_heat_sources, blank=True, null=True)
    home_6_heat_src_other = models.TextField(max_length=20, blank=True, null=True)   

    def __str__(self):
        return self.total_exposure
    

class Indirect_costs(models.Model):
    procedure_choices = (
        ('Spiral CT', 'Spiral CT'),
        ('Spirometry', 'Spirometry'),
        ('Blood Collection', 'Blood Collection'),
        ('Other', 'Other'),
    )
    true_false_choices = (
        (True, 'Yes'),
        (False, 'No')
    )
    affected_pay_choices = (
        ('It affected by pay', 'It affected by pay'),
        ('It was time granted by my employer', 'It was time granted by my employer'),
    )
    transportation_choices = (
        ('private', 'Private: (car)'),
        ('public', 'Public transportation (bus, metro, train, taxi)'),
    )
    income_choices = (
        ('< $10,000', '< $10,000'),
        ('$10,000 to $19,999', '$10,000 to $19,999'),
        ('$20,000 to $29,999', '$20,000 to $29,999'),
        ('$30,000 to $39,999', '$30,000 to $39,999'),
        ('$40,000 to $49,999', '$40,000 to $49,999'),
        ('$50,000 to $59,999', '$50,000 to $59,999'),
        ('$60,000 to $69,999', '$60,000 to $69,999'),
        ('$70,000 to $79,999', '$70,000 to $79,999'),
        ('$80,000 to $89,999', '$80,000 to $89,999'),
        ('$90,000 to $99,999', '$90,000 to $99,999'),
        ('$100,000 to $124,999', '$100,000 to $124,999'),
        ('$125,000 to $149,999', '$125,000 to $149,999'),
        ('≥ $150,000', '≥ $150,000')
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    visit_date = models.DateField()
    procedure = models.TextField(max_length=20, choices=procedure_choices, blank=False, default=None, verbose_name='What procedure(s) have you come in for?')
    procedure_other = models.TextField(max_length=100, null=True, blank=True, verbose_name='Other Procedure')
    missed_work = models.BooleanField(max_length=50, choices=true_false_choices, default=False, verbose_name='Did you miss work to attend this medical appointment?')
    missed_work_hours = models.FloatField(blank=True, null=True, verbose_name='How many hours of work did you miss today to attend your appointment?')
    affected_pay = models.TextField(max_length=50, choices=affected_pay_choices, null=True, default=None, verbose_name='Other Procedure')
    appointment_time_hours = models.FloatField(blank=True, null=True, verbose_name='Hours')
    appointment_time_minutes = models.FloatField(blank=True, null=True, verbose_name='Minutes')
    transportation = models.TextField(max_length=50, choices=transportation_choices, default=None, verbose_name='What means of transportation did you use to come to this appointment?')
    trip_distance = models.FloatField(null=True, blank=True, verbose_name='Estimate the round trip distance in kilometers')
    parking_cost = models.FloatField(default=0)
    public_transportation_cost = models.FloatField(default=0)
    babysitter_cost = models.FloatField(default=0)
    other_cost = models.FloatField(default=0)
    other_costs_description = models.TextField(max_length=255, blank=True)
    income = models.TextField(max_length=40, choices=income_choices, blank=True, verbose_name='What is your annual income (gross income, before taxes)?')
    income_household = models.TextField(max_length=40, choices=income_choices, blank=True, verbose_name='What is the annual income of your household (gross income, before taxes)?')


class Mandatory_questionaire(models.Model):
    gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Trans Female to Male','Trans Female to Male'),
        ('Trans Male to Female','Trans Male to Female'),
        ('Intersex', 'Intersex'),
        ('Other', 'Other'),
        ('Prefer not to answer','Prefer not to answer'),
        ('Do not know','Do not know'),
    )
    sex_assinged_birth = (
        ('Male', 'Male'),
        ('Female', 'Female'),   
    )
    ethnicity = (
        ('Indigenous ancestry (e.g., First Nations, North American Indian, Metis, Inuit)', 'Indigenous ancestry (e.g., First Nations, North American Indian, Metis, Inuit)'),
        ('Middle Eastern (e.g., Turkey, Iran, Afghanistan, Iraq, Jordan, Lebanon)', 'Middle Eastern (e.g., Turkey, Iran, Afghanistan, Iraq, Jordan, Lebanon)'),
        ('African or Caribbean descent', 'African or Caribbean descent'),
        ('European descent / White', 'European descent / White'),
        ('Filipino', 'Filipino'),
        ('Jewish', 'Jewish'),
        ('Latin American', 'Latin American'),
        ('South Asian (e.g. India, Sri Lanka, Pakistan, Bangladesh)', 'South Asian (e.g. India, Sri Lanka, Pakistan, Bangladesh)'),
        ('Southeast Asian (e.g., Malaysia, Indonesia, Vietnam)', 'Southeast Asian (e.g., Malaysia, Indonesia, Vietnam)'),
        ('East Asian (e.g., China, Japan, Korea, Taiwan)', 'East Asian (e.g., China, Japan, Korea, Taiwan)'),
        ('Other ethnic group not specified above', 'Other ethnic group not specified above'),
        ('Prefer not to answer', 'Prefer not to answer'),     
     )
    born_in_canada_choice = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Dont know', 'Dont know'),
    )
    highest_education_lvl = (
        ('Less than high school', 'Less than high school'),
        ('High school graduate', 'High school graduate'),
        ('Post High School Training', 'Post High School Training'),
        ('Some college', 'Some college'),
        ('College or University diploma', 'College or University diploma'),
        ('Post graduate degree or Professional Degree', 'Post graduate degree or Professional Degree'),
        ('Other', 'Other'),
        ('Prefer not to say', 'Prefer not to say'),
        
    )
   
    gender_surgery = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Prefer not to answer', 'Prefer not to answer'),
        
    )
    gender_hormone = (
        ('Feminizing', 'Feminizing'),
        ('Masculinizing', 'Masculinizing'),
    )
    height_unit = (
        ('cm', 'cm'),
        ('in', 'in'),
    )
    weight_unit = (
        ('kg', 'kg'),
        ('lbs', 'lbs'),
    )

    biological_cancer = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Dont know', 'Dont know'),
    )
    height_unit = (
        ('cm', 'cm'),
        ('inches', 'in'),
    )
    weight_unit = (
        ('kg', 'kg'),
        ('lbs', 'lbs'),
    )
    gender_affirming_therapy_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Prefer not to answer', 'Prefer not to answer'),
    )
    gender_therapy_type = (
        ('Feminizing hormone therapy', 'Feminizing hormone therapy'),
        ('Masculinizing hormone therapy', 'Masculinizing hormone therapy'),
    )
    biological_relatives_cancer = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Don\'t Know', 'Don\'t Know')
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    form_pdf_upload = models.FileField(upload_to='form_pdf_upload', null=True, blank=True)
    form_pdf_upload_link = models.TextField(max_length=200, null=True, blank=True)
    visit_date = models.DateField()
    date_of_birth = models.DateField()
    current_height = models.IntegerField()
    current_height_unit = models.TextField(max_length=20, choices=height_unit)
    current_weight = models.IntegerField()
    current_weight_unit = models.TextField(max_length=20, choices=weight_unit)
    sex_birth = models.TextField(max_length=200, choices=sex_assinged_birth)
    postal_code = models.TextField(max_length=6)
    current_age = models.IntegerField()
    gender_identity = models.TextField(max_length=200, choices=gender, null=True, blank=True)
    gender_surgery  = models.TextField(max_length=50, choices=gender_surgery, null=True, blank=True)
    gender_surgery_harmone = models.TextField(max_length=200, choices=gender_hormone, null=True, blank=True)
    gender_identity_other = models.TextField(max_length=50, null=True, blank=True)
    gender_affirming_therapy = models.TextField(max_length=50, choices=gender_affirming_therapy_choices, null=True, blank=True)
    gender_affirming_therapy_type = models.TextField(max_length=50, choices=gender_therapy_type, null=True, blank=True)
    ethnicity = models.TextField(max_length=78, choices=ethnicity, null=True, blank=True)
    ethnicity_other = models.TextField(max_length=20, null=True, blank=True)
    born_in_canada = models.TextField(max_length=20, choices=born_in_canada_choice, null=True, blank=True)
    year_moved_to_canada = models.TextField(default='N/A', null=True, max_length=4)
    birthplace = models.TextField(default=False, null=True, max_length=20)
    highest_education_lvl = models.TextField(max_length=43, choices=highest_education_lvl)
    highest_education_lvl_other = models.TextField(default=False, null=True, max_length=20)
    copd = models.BooleanField(default=False)
    emphysema = models.BooleanField(default=False)
    chronic_bronchitis = models.BooleanField(default=False)
    asthma = models.BooleanField(default=False)
    diabetes = models.BooleanField(default=False)
    hypertension = models.BooleanField(default=False)
    tuberculosis = models.BooleanField(default=False)
    adult_pneumonia = models.BooleanField(default=False)
    pulmonary_fibrosis = models.BooleanField(default=False)
    hiv = models.BooleanField(default=False)
    long_covid = models.BooleanField(default=False)
    personal_cancer_history = models.BooleanField(default=False, null=True, blank=True)
    personal_cancer_history_youngest_age = models.TextField(max_length=3, null=True, blank=True)
    personal_history_cancer_type = models.TextField(max_length=20, null=True, blank=True)
    num_sisters = models.TextField( null=True,max_length=20)
    num_brothers = models.TextField( null=True,max_length=20)
    num_half_sisters = models.TextField( null=True,max_length=20)
    num_half_brothers = models.TextField( null=True,max_length=20)
    children = models.TextField(null=True,max_length=20)
    # biological_relatives_cancer = models.TextField(max_length=25, choices=biological_relatives_cancer, null=True, blank=True)

class biological_relatives_with_cancer(models.Model):
    mandatory_questionaire = models.ForeignKey(Mandatory_questionaire, on_delete=models.CASCADE)
    biological_relationship = models.TextField(max_length=20)
    type_of_cancer = models.TextField(max_length=20)
    diagnosis_age = models.TextField(max_length=20)


class Mandatory_questionaire_c(models.Model):
    waking_cigs = (
    ('After 60 min', 'After 60 min'),
    ('31-60 min', '31-60 min'),
    ('5-30 min', '5-30 min'),
    ('Within 5 min', 'Within 5 min'),
    ('N/A', 'N/A'),
    )
    chew_snuff = (
        ('Never', 'Never'),
        ('Occasionally', 'Occasionally'),
        ('Regularly', 'Regularly'),
        ('N/A', 'N/A'),
    )   
    give_up = (
        ('First thing in the morning', 'First thing in the morning'),
        ('Any Other', 'Any Other'),
        ('N/A', 'N/A'),
    )
    mode_of_use_choices = (
        ('Joints', 'Joints'),
        ('Pipe', 'Pipe'),
        ('Bong', 'Bong'),
        ('N/A', 'N/A'),
    )
    unit_choices = (
        ('Joints', 'Joints'),
        ('Ounces', 'Ounces'),
        ('Hits', 'Hits'),
        ('N/A', 'N/A'),
    )
    quantity_choices = (
        ('Daily', 'Daily'),
        ('Weekly', 'Weekly'),
        ('Monthly', 'Monthly'),
        ('Yearly', 'Yearly'),
        ('N/A', 'N/A'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    smoked_more_100_cigs = models.BooleanField(default=False)
    age_regular_smoking = models.TextField(max_length=20)
    avg_cig_per_day = models.TextField(max_length=20)
    stopped_smoking = models.TextField(max_length=20, null=True, blank=True)
    last_cig_date = models.DateField(max_length=20, null=True, blank=True)
    last_cig_age = models.TextField(max_length=20)
    marajuana_use = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_1 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_to_age_1 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_1_quantity = models.TextField(max_length=20, null=True, blank=True, choices=quantity_choices)
    marajuana_use_age_1_mode = models.TextField(max_length=20, null=True, blank=True, choices=mode_of_use_choices)
    marajuana_use_age_1_units = models.TextField(max_length=20, null=True, blank=True, choices=unit_choices)
    marajuana_use_age_2 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_to_age_2 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_2_quantity = models.TextField(max_length=20, null=True, blank=True, choices=quantity_choices)
    marajuana_use_age_2_mode = models.TextField(max_length=20, null=True, blank=True, choices=mode_of_use_choices)
    marajuana_use_age_2_units = models.TextField(max_length=20, null=True, blank=True, choices=unit_choices)
    marajuana_use_age_3 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_to_age_3 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_3_quantity = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_3_mode = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_3_units = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_4 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_to_age_4 = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_4_quantity = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_4_mode = models.TextField(max_length=20, null=True, blank=True)
    marajuana_use_age_4_units = models.TextField(max_length=20, null=True, blank=True)
    smoked_pipe = models.BooleanField(default=False)
    smoked_pipe_avg_ounces = models.TextField(max_length=20, null=True, blank=True)
    smoked_pipe_avg_age = models.TextField(max_length=20, null=True, blank=True)
    still_smoking_pipe = models.BooleanField(default=False)
    still_smoking_pipe_stop_date = models.TextField(max_length=20, null=True, blank=True)
    still_smoking_pipe_stop_age = models.TextField(max_length=20, null=True, blank=True)
    smoked_cigars = models.BooleanField(default=False)
    avg_num_cigars = models.TextField(max_length=20, null=True, blank=True)
    avg_cigar_age = models.TextField(max_length=20, null=True, blank=True)
    still_smoke_cigars = models.TextField(max_length=20, null=True, blank=True)
    still_smoke_cigars_start_date  = models.DateField(max_length=20, null=True, blank=True)
    still_smoke_cigars_start_age = models.TextField(max_length=20, null=True, blank=True)
    still_smoke_cigars_stop_date = models.DateField(max_length=20, null=True, blank=True)
    still_smoke_cigars_stop_age = models.TextField(max_length=20, null=True, blank=True)

    chewing_tobacco = models.TextField(max_length=20, choices=chew_snuff)
    chewing_tobacco_age = models.TextField(max_length=20, null=True, blank=True)
    chewing_tobacco_years = models.TextField(max_length=20, null=True, blank=True)
    snuff = models.TextField(max_length=20, choices=chew_snuff)
    snuff_age = models.TextField(max_length=20, null=True, blank=True)
    snuff_years = models.TextField(max_length=20, null=True, blank=True)
    vape = models.BooleanField(default=False)
    vape_num_times = models.TextField(max_length=20, null=True, blank=True)
    vape_start_date = models.DateField(max_length=20, null=True, blank=True)
    vape_stop_date = models.DateField(max_length=20, null=True, blank=True)
    vape_start_age = models.TextField(max_length=20, null=True, blank=True)
    still_vape = models.TextField(max_length=20, null=True, blank=True)
    still_vape_stop_age = models.TextField(max_length=20, null=True, blank=True)
    still_vape_stop_date = models.DateField(max_length=20, null=True, blank=True)
    vape_flavor = models.TextField(max_length=20, null=True, blank=True)
    cigs_waking_up = models.TextField(max_length=20, choices=waking_cigs)
    smoke_refrain = models.TextField(max_length=20, null=True, blank=True)
    cig_giveup = models.TextField(max_length=26, choices=give_up)
    smoke_morning = models.TextField(max_length=20, null=True, blank=True)
    smoke_sick = models.TextField(max_length=20, null=True, blank=True)
    quit_smoking = models.BooleanField(default=False)
    quit_smoking_times = models.TextField(max_length=20)

class Mandatory_questionaire_de(models.Model):
    second_hand_youth_choices = (
    ('Zero', 'Zero'),
    ('Mild', 'Mild'),
    ('Moderate', 'Moderate'),
    ('Heavy', 'Heavy'),
    ('N/A', 'N/A'),
    )
    second_hand_smoke= (
        ('Zero', 'Zero'),
        ('Mild', 'Mild'),
        ('Moderate', 'Moderate'),
        ('Heavy', 'Heavy'),
        ('N/A', 'N/A'),
    )
    second_hand_home_choices = (
        ('Exposure at Home', 'Exposure at Home'),
        ('Exposure at Work', 'Exposure at Work'),
        ('Exposure During leisure activities', 'Exposure During leisure activities'),
        ('N/A', 'N/A'),
    )

    timepoints = (
        ('Less than 2 hours', 'Less than 2 hours'),
        ('2-4 hours', '2-4 hours'),
        ('4-6 hours', '4-6 hours'),
        ('6 plus hours', '6 plus hours'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    second_hand_smoke = models.TextField(max_length=20, choices=second_hand_smoke, null=True, blank=True)
    
    second_hand_home = models.TextField(max_length=34, choices = second_hand_home_choices, null=True, blank=True)
    second_hand_work = models.TextField(max_length=20, null=True, blank=True)
    second_hand_leisure = models.TextField(max_length=20, null=True, blank=True)
    
    second_hand_4days = models.TextField(max_length=20, null=True, blank=True)
    second_hand_13days = models.TextField(max_length=20, null=True, blank=True)
    second_hand_occasionally = models.TextField(max_length=20, null=True, blank=True)
    second_hand_exposure_time = models.TextField(max_length=20, choices=timepoints,  null=True, blank=True)
    second_hand_yrs = models.TextField(max_length=20, null=True, blank=True)
    second_hand_freq = models.TextField(max_length=20, null=True, blank=True)
    second_hand_avg_exposure = models.TextField(max_length=20, null=True, blank=True)
    second_hand_youth = models.TextField(max_length=40, choices=second_hand_youth_choices, null=True, blank=True)
    
    alcohol_from_age1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor4 = models.TextField(max_length=20, null=True, blank=True)
    
    alcohol_stop_age = models.TextField(max_length=20, null=True, blank=True)

    second_hand_1yr = models.TextField( null=True, blank=True, default=None)
    alcohol = models.TextField(null=True, blank=True)
    alcohol_current = models.TextField( null=True, blank=True)
    second_hand_daily = models.TextField(max_length=20, null=True, blank=True)

class Mandatory_questionaire_fg(models.Model):
    medication_frequency = (
    ('Less than 1 time per month', 'Less than 1 time per month'),
    ('1 - 3 times per month', '1 - 3 times per month'),
    ('1 - 2 times per month', '1 - 2 times per month'),
    ('3 - 6 times per month', '3 - 6 times per month'),
    ('7 or more times per week', '7 or more times per week'),
    ('N/A', 'N/A'),
    )
    working_situation = (
    ('Working', 'Working'),
    ('Retired', 'Retired'),
    ('Unemployed', 'Unemployed'), 
    ('Disabled', 'Disabled'),
    ('On extended sick leave', 'On extended sick leave'),
    ('Other', 'Other'),

    )
    drug_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Don’t Know', 'Don’t Know'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inhaled_drugs = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_day = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_month = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_year = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    bronchodialators = models.TextField(max_length=20,choices=drug_choices, null=True, blank=True)
    bronchodialators_day = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_month = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_year = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    statins = models.TextField(max_length=20, choices=drug_choices, null=True, blank=True)
    statins_day = models.TextField(max_length=20, null=True, blank=True)
    statins_month = models.TextField(max_length=20, null=True, blank=True)
    statins_year = models.TextField(max_length=20, null=True, blank=True)
    statins_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    metformin = models.TextField(max_length=20,choices=drug_choices, null=True, blank=True)
    metformin_day = models.TextField(max_length=20, null=True, blank=True)
    metformin_month = models.TextField(max_length=20, null=True, blank=True)
    metformin_year = models.TextField(max_length=20, null=True, blank=True)
    metformin_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    current_working_situation = models.TextField(max_length=30, choices=working_situation)
    current_working_situation_other = models.TextField(max_length=20, null=True, blank=True)
    occupation_longest = models.TextField(max_length=20, null=True, blank=True)    
    occupation_longest_activities = models.TextField(max_length=20, null=True, blank=True)
    occupation_longest_years = models.TextField(max_length=20, null=True, blank=True)
    occupation_exposure = models.TextField(max_length=20, null=True, blank=True)
    occupation_fumes = models.TextField(max_length=20, null=True, blank=True)
    occupation_years = models.TextField(null=True, blank=True)


class last_mandatory_questionnaire(models.Model):
    second_hand_youth_choices = (
    ('Zero', 'Zero'),
    ('Mild', 'Mild'),
    ('Moderate', 'Moderate'),
    ('Heavy', 'Heavy'),
    ('N/A', 'N/A'),
    )
    second_hand_smoke= (
        ('Zero', 'Zero'),
        ('Mild', 'Mild'),
        ('Moderate', 'Moderate'),
        ('Heavy', 'Heavy'),
        ('N/A', 'N/A'),
    )
    second_hand_home_choices = (
        ('Exposure at Home', 'Exposure at Home'),
        ('Exposure at Work', 'Exposure at Work'),
        ('Exposure During leisure activities', 'Exposure During leisure activities'),
        ('N/A', 'N/A'),
    )

    timepoints = (
        ('Less than 2 hours', 'Less than 2 hours'),
        ('2-4 hours', '2-4 hours'),
        ('4-6 hours', '4-6 hours'),
        ('6 plus hours', '6 plus hours'),
    )
    medication_frequency = (
    ('Less than 1 time per month', 'Less than 1 time per month'),
    ('1 - 3 times per month', '1 - 3 times per month'),
    ('1 - 2 times per month', '1 - 2 times per month'),
    ('3 - 6 times per month', '3 - 6 times per month'),
    ('7 or more times per week', '7 or more times per week'),
    ('N/A', 'N/A'),
    )
    working_situation = (
    ('Working', 'Working'),
    ('Retired', 'Retired'),
    ('Unemployed', 'Unemployed'), 
    ('Disabled', 'Disabled'),
    ('On extended sick leave', 'On extended sick leave'),
    ('Other', 'Other'),

    )
    second_hand_daily_choices = (
    ('Daily', 'Daily'),
    ('At Least 4 Days/Week but not everyday', 'At Least 4 Days/Week but not everyday'),
    ('1 - 3 Days/Week', '1 - 3 Days/Week'),
    ('Occasionally', 'Occasionally'),
    )
    drug_choices = (
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Don’t Know', 'Don’t Know'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    second_hand_smoke = models.TextField(max_length=20, choices=second_hand_smoke, null=True, blank=True)
    second_hand_home = models.TextField(max_length=34, choices = second_hand_home_choices, null=True, blank=True)
    second_hand_work = models.TextField(max_length=20, null=True, blank=True)
    second_hand_leisure = models.TextField(max_length=20, null=True, blank=True)
    second_hand_4days = models.TextField(max_length=20, null=True, blank=True)
    second_hand_13days = models.TextField(max_length=20, null=True, blank=True)
    second_hand_occasionally = models.TextField(max_length=20, null=True, blank=True)
    second_hand_exposure_time = models.TextField(max_length=20, choices=timepoints,  null=True, blank=True)
    second_hand_yrs = models.TextField(max_length=20, null=True, blank=True)
    second_hand_freq = models.TextField(max_length=20, null=True, blank=True)
    second_hand_avg_exposure = models.TextField(max_length=20, null=True, blank=True)
    second_hand_youth = models.TextField(max_length=40, choices=second_hand_youth_choices, null=True, blank=True)
    alcohol_from_age1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor1 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor2 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor3 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_from_age4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_to_age4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_beer4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_wine4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_liquor4 = models.TextField(max_length=20, null=True, blank=True)
    alcohol_stop_age = models.TextField(max_length=20, null=True, blank=True)
    second_hand_1yr = models.TextField( null=True, blank=True, default=None)
    alcohol = models.TextField(null=True, blank=True)
    alcohol_current = models.TextField( null=True, blank=True)
    second_hand_daily = models.TextField(choices=second_hand_daily_choices, max_length=70, null=False, blank=False)
    inhaled_drugs = models.TextField(max_length=20, choices=drug_choices, null=True, blank=True)
    inhaled_drugs_day = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_month = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_year = models.TextField(max_length=20, null=True, blank=True)
    inhaled_drugs_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    bronchodialators = models.TextField(max_length=20,choices=drug_choices, null=True, blank=True)
    bronchodialators_day = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_month = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_year = models.TextField(max_length=20, null=True, blank=True)
    bronchodialators_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    statins = models.TextField(max_length=20,choices=drug_choices, null=True, blank=True)
    statins_day = models.TextField(max_length=20, null=True, blank=True)
    statins_month = models.TextField(max_length=20, null=True, blank=True)
    statins_year = models.TextField(max_length=20, null=True, blank=True)
    statins_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    metformin = models.TextField(max_length=20,choices=drug_choices, null=True, blank=True)
    metformin_day = models.TextField(max_length=20, null=True, blank=True)
    metformin_month = models.TextField(max_length=20, null=True, blank=True)
    metformin_year = models.TextField(max_length=20, null=True, blank=True)
    metformin_freq = models.TextField(max_length=30, choices=medication_frequency, null=True, blank=True)
    current_working_situation = models.TextField(max_length=30, choices=working_situation)
    current_working_situation_other = models.TextField(max_length=20, null=True, blank=True)
    occupation_longest = models.TextField(max_length=20, null=True, blank=True)    
    occupation_longest_activities = models.TextField(max_length=20, null=True, blank=True)
    occupation_longest_years = models.TextField(max_length=20, null=True, blank=True)
    occupation_exposure = models.TextField(max_length=20, null=True, blank=True)
    occupation_fumes = models.TextField(max_length=20, null=True, blank=True)
    occupation_years = models.TextField(null=True, blank=True)

class Cat_5_findings(models.Model):
    CONDITION_CHOICES = (
        ('Suspicious Lymph Node', 'Suspicious Lymph Node'),
        ('Suspicious Lung Lesion', 'Suspicious Lung Lesion'),
        ('Endobronchial Nodule', 'Endobronchial Nodule'),
    )

    name = models.CharField(max_length=50, choices=CONDITION_CHOICES)

    def __str__(self):
        return self.name

class Emphysema_type(models.Model):
    emphysema_type = [
        ('Centrilobular', 'Centrilobular'),
        ('Paraseptal', 'Paraseptal'),
        ('Panacinar', 'Panacinar'),
    ]

    name = models.CharField(max_length=50, choices=emphysema_type)

    def __str__(self):
        return self.name

class Airways_type(models.Model):
    airways_type = [
        ('Mucous Impaction', 'Mucous Impaction'),
        ('Wall Thickening', 'Wall Thickening'),
        ('Bronchiectasis', 'Bronchiectasis'),
        ('Bronchiolectasis', 'Bronchiolectasis'),
    ]

    name = models.CharField(max_length=50, choices=airways_type)

    def __str__(self):
        return self.name




class ct_scan(models.Model):
    ct_scan_type_choices = (
        ('Philips', 'Philips'),
        ('Viality', 'Viality'),
    )
    reading_options = (
        ('just CAD', 'just CAD'),
        ('just radiologist', 'just radiologist'),
        ('CAD and radiologist', 'CAD and radiologist'),
    )
    findings_choices = (
        ('normal', 'normal'),
        ('actionable', 'actionable'),
        ('non-actionable', 'non-actionable'),
    )
    PLEURA_CHOICES = (
        ('effusion', 'Pleural Effusion'),
        ('asbestos', 'Asbestos-Related'),
    )
    ilst_categories = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    fu_dates = (
        (1, 1),
        (3, 3),
        (6, 6),
        (9, 9),
        (12, 12),
        (24, 24),
    )
    emphysema_choices = (
        ('yes', 'Yes'),
        ('no', 'No'),
        ('unclear', 'Unclear'),
        ('not assessed', 'Not Assessed'),
        ('not reported', 'Not Reported'),
    )
    emphysema_extent = (
        ('None', 'None'),
        ('Trace', 'Trace'),
        ('Mild', 'Mild'),
        ('Moderate', 'Moderate'),
        ('Severe', 'Severe'),
    )

    emphysema_distrobution = (
        ('upper zone', 'Upper Zone'),
        ('lower zone', 'Lower Zone'),
        ('Diffuse or Homogenous', 'Diffuse / Homogenous'),
    )
    cor_art_calc = (
        ('absent', 'Absent'),
        ('mild', 'Mild'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    )
    airways = (
        ('normal', 'Normal'),
        ('abnormal', 'Abnormal'),

    )

    ct_scan_visit_id = (
        ('0', 'T0_Baseline'),
        ('1', 'T0_3_Months'),
        ('2', 'T0_6_Months'),
        ('3', 'T1_12_Months'),
        ('4', 'T2_24_Months'),
        ('5', 'T3_36_Months'),
        ('6', 'T4_48_Months'),
        ('7', 'T5_60_Months'),
    )

    yes_no = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE, null=False, blank=False)
    ct_scan_date = models.DateField(null=True, blank=True)
    ct_scan_visitID = models.TextField(max_length=20, choices=ct_scan_visit_id, default=None, blank=True)
    ct_scan_location = models.TextField(max_length=20, blank=True)
    ct_scan_radiologist = models.TextField(max_length=20, blank=True)
    ct_scan_review_date = models.DateField(null=True, blank=True)
    ct_scan_familty_history = models.BooleanField(null=True, blank=True)
    ct_scan_pt_lung_cancer = models.BooleanField(null=True, blank=True)
    ct_scan_dlp = models.TextField(max_length=20, blank=True)
    radiologist_fu_mnths = models.IntegerField(choices=fu_dates, null=True, blank=True)
    radiologist_fu_mnths_date = models.DateField(null=True, blank=True)
    cad_fu_mnths = models.IntegerField(choices=fu_dates, null=True, blank=True)
    cad_fu_mnths_date = models.DateField(null=True, blank=True)
    ilst_cat = models.IntegerField(choices=ilst_categories, null=True, blank=True)
    final_rec_fu_mnths = models.IntegerField(choices=fu_dates, null=True, blank=True)
    final_rec_fu_mnths_date = models.DateField(null=True, blank=True)
    copd_emphysema = models.TextField(max_length=20, choices=emphysema_choices, default=None)
    copd_emphysema_extent = models.TextField(max_length=20, choices=emphysema_extent, default=None)
    copd_emphysema_type = models.ManyToManyField(Emphysema_type, blank=True)
    copd_emphysema_distribution = models.TextField(max_length=45, choices=emphysema_distrobution, default=None)
    cor_art_calc = models.TextField(max_length=20, choices=cor_art_calc, default=None, blank=True)
    cor_art_agatson = models.TextField(max_length=20)
    airways = models.TextField(max_length=20, choices=airways, default=None)
    airways_type = models.ManyToManyField(Airways_type, blank=True)
    airways_type_muc_impaction = models.TextField(max_length=20, blank=True)
    aiways_type_wall_thickening = models.TextField(max_length=20, blank=True)
    airways_type_bronchiectasis = models.TextField(max_length=20, blank=True)
    ariways_type_bronchiolectasis = models.TextField(max_length=20, blank=True)
    cat_5_findings = models.ManyToManyField(Cat_5_findings, blank=True)
    cat_5_lymph_nodes = models.TextField(max_length=20, blank=True)
    cat_5_suspicious_nodes = models.TextField(max_length=20, blank=True)
    cat_5_endobronchial = models.TextField(max_length=20, blank=True)
    cat_5_comments = models.TextField(max_length=500, blank=True)
    other_cardiovascular = models.TextField(max_length=20, choices=findings_choices, default=None, blank=True)
    other_cardiovascular_comments = models.TextField(max_length=20, blank=True)
    other_vertebral = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_vertebral_comments = models.TextField(max_length=20, blank=True)
    other_GI = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_GI_comments = models.TextField(max_length=20, blank=True)
    other_breast = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_breast_comments = models.TextField(max_length=20, blank=True)
    other_endocrine = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_endocrine_comments = models.TextField(max_length=20, blank=True)
    other_lymph = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_lymph_comments = models.TextField(max_length=20, blank=True)
    other_pleura = models.TextField(max_length=20, choices=findings_choices, blank=True)
    other_pleura_comments = models.TextField(max_length=20, choices=PLEURA_CHOICES, default=None, blank=True)
    other_pulmonary_fibrosis = models.TextField(max_length=20, choices=findings_choices, default=None, blank=True)
    other_pulmonary_fibrosis_comments = models.TextField(max_length=20, blank=True)
    other_musculoskeletal = models.TextField(max_length=20, choices=findings_choices, default=None, blank=True)
    other_musculoskeletal_comments = models.TextField(max_length=20, blank=True)
    other_other = models.TextField(max_length=20, choices=findings_choices, default=None, blank=True)
    other_other_comments = models.TextField(max_length=20, blank=True)
    general_comments = models.TextField(max_length=200, blank=True)



class ct_scan_nodule_1(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('New', 'New'),
        ('Stable', 'Stable'),
        ('Increased', 'Increased'),
        ('Decreased', 'Decreased'),

    )
    nodule_type_choices =(
        ('Solid', 'Solid'),
        ('Non-Solid', 'Non-Solid'),
        ('Part Solid', 'Part Solid'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('Smooth', 'Smooth'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
    )
    location_choices = (
        ('Parenchymal', 'Parenchymal'),
        ('Airway', 'Airway'),
        ('Juxtapleural', 'Juxtapleural'),
        ('Fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=1)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)

class ct_scan_nodule_2(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('Solid', 'Solid'),
        ('Non-Solid', 'Non-Solid'),
        ('Part Solid', 'Part Solid'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=2)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)

class ct_scan_nodule_3(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('Solid', 'Solid'),
        ('Non-Solid', 'Non-Solid'),
        ('Part Solid', 'Part Solid'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=3)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)

class ct_scan_nodule_4(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('Solid', 'Solid'),
        ('Non-Solid', 'Non-Solid'),
        ('Part Solid', 'Part Solid'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=4)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)
    def str(self):
        return self.ct_scan_date

class ct_scan_nodule_5(models.Model):
    status_options = (
        ('new', 'New'),
        ('old', 'Old'),
        ('retro', 'Retro'),
        ('first seen', 'First Seen'),
    )
    radiologist_Accepted = (
        ('accepted', 'Accepted'),
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    technician = (
        ('deleted', 'Deleted'),
        ('added', 'Added')
    )
    interval_change_choices = (
        ('unchanged', 'Unchanged'),
        ('smaller', 'Smaller'),
        ('density increased', 'Density Increased'),
        ('benign', 'Benign'),
        ('resolved', 'Resolved'),
        ('rescted', 'Resected'),
        ('growing', 'Growing'),
    )
    nodule_type_choices =(
        ('Solid', 'Solid'),
        ('Non-Solid', 'Non-Solid'),
        ('Part Solid', 'Part Solid'),
        ('Calcified', 'Calcified'),
        ('PFN', 'PFN'),
        ('Cystic', 'Cystic'),
        ('N/A', 'N/A'),

    )
    description_choices = (
        ('well defined', 'Well Defined'),
        ('lobulated', 'Lobulated'),
        ('spiculated', 'Spiculated'),
        ('halo', 'Halo-Like'),
    )
    location_choices = (
        ('parenchymal', 'Parenchymal'),
        ('subpleural', 'Subpleural'),
        ('fissural', 'Fissural'),
    )
    follow_up_choices = (
        ('3 Months', '3 Months'),
        ('6 Months', '6 Months'),
        ('12 Months', '12 Months'),
        ('24 Months', '24 Months'),
    )
    fleicher_fu_choices = (
        ('No Routine Follow-up', 'No Routine Follow-up'),
        ('3-6 Month Follow-up', '3-6 Month Follow-up'),
        ('6-12 Month Follow-up', '6-12 Month Follow-up'),
        ('12 Month Follow-up', '12 Month Follow-up'),
        )
    nodule_location_choices = (
        ('RUL', 'RUL'),
        ('RML', 'RML'),
        ('RLL', 'RLL'),
        ('LUL', 'LUL'),
        ('LLL', 'LLL'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    nodule_rank = models.TextField(max_length=20, default=5)
    nodule_slice_num = models.TextField(max_length=20)
    nodule_segment = models.TextField(max_length=20)
    nodule_cad_found = models.TextField(max_length=20)
    nodule_location_selection = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_status = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_interval_change = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long = models.TextField(max_length=20)
    nodule_axis_short = models.TextField(max_length=20)
    nodule_axis_mean = models.TextField(max_length=20)
    nodule_axis_volume = models.TextField(max_length=20)
    nodule_axis_density = models.TextField(max_length=20)
    nodule_axis_sd = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long = models.TextField(max_length=20)
    nodule_ssn_short = models.TextField(max_length=20)
    nodule_description = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam = models.TextField(max_length=20)
    nodule_change_dd = models.TextField(max_length=20)
    nodule_change_volume = models.TextField(max_length=20)
    nodule_change_volsperc = models.TextField(max_length=20)
    nodule_change_mean = models.TextField(max_length=20)
    nodule_comments = models.TextField(max_length=20)
    nodule_risk_index = models.TextField(max_length=20)
    nodule_key_nodule = models.TextField(max_length=20)
    nodule_cancer_confirmed = models.TextField(max_length=20)
    nodule_recommended_fu = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders = models.TextField(max_length=100)
    # CAD Nodule
    nodule_status_cad = models.TextField(max_length=20, choices=status_options, default=None)
    nodule_location_selection_cad = models.TextField(max_length=3, choices=nodule_location_choices, default=None)
    nodule_interval_change_cad = models.TextField(max_length=20, choices=interval_change_choices, default=None)
    nodule_type_cad = models.TextField(max_length=20, choices=nodule_type_choices, default=None)
    nodule_axis_long_cad = models.TextField(max_length=20)
    nodule_axis_short_cad = models.TextField(max_length=20)
    nodule_axis_mean_cad = models.TextField(max_length=20)
    nodule_axis_volume_cad = models.TextField(max_length=20)
    nodule_axis_density_cad = models.TextField(max_length=20)
    nodule_axis_sd_cad = models.TextField(max_length=20, blank=True, null=True)
    nodule_ssn_long_cad = models.TextField(max_length=20)
    nodule_ssn_short_cad = models.TextField(max_length=20)
    nodule_description_cad = models.TextField(max_length=20, choices=description_choices, default=None)
    nodule_location_cad = models.TextField(max_length=20, choices=location_choices, default=None)
    nodule_change_avediam_cad = models.TextField(max_length=20)
    nodule_change_dd_cad = models.TextField(max_length=20)
    nodule_change_volume_cad = models.TextField(max_length=20)
    nodule_change_volsperc_cad = models.TextField(max_length=20)
    nodule_change_mean_cad = models.TextField(max_length=20)
    nodule_comments_cad = models.TextField(max_length=20)
    nodule_risk_index_cad = models.TextField(max_length=20)
    nodule_key_nodule_cad = models.TextField(max_length=20)
    nodule_cancer_confirmed_cad = models.TextField(max_length=20)
    nodule_recommended_fu_cad = models.TextField(max_length=20, choices=follow_up_choices, default=None)
    nodule_fleicher_fu_cad = models.TextField(max_length=20, choices=fleicher_fu_choices, default=None)
    nodule_orders_cad = models.TextField(max_length=100)


class MyForm(models.Model):
    variable1 = models.CharField(max_length=100)
    variable2 = models.CharField(max_length=100)
    variable3 = models.CharField(max_length=100)

class CancerHistory(models.Model):
    biological_rel = models.TextField(max_length=20)
    type_of_cancer = models.TextField(max_length=20)
    age_diagnosis = models.TextField(max_length=20)



class inclusion(models.Model):
    inclusion_status_choices = (
        ('eligible and willing to participate', 'eligible and willing to participate'),
        ('eligible but unwilling to participate', 'eligible but unwilling to participate'),
        ('ineligible', 'ineligible'),
        ('ineligible but willing to participate', 'ineligible but willing to participate'),

    )
    consent_status_choices = (
        ('consented', 'consented'),
        ('not consented', 'not consented'),
    )
    screening = (
        ('enrolled', 'enrolled'),
        ('pending interview', 'pending interview'),
        ('pending enrollment', 'pending enrollment'),
        ('ineligible', 'ineligible'),
        ('declined study', 'declined study'),
        ('off study', 'off study'),
        ('confirmed study', 'confirmed study'),
    )
    participant_status = (
        ('IPN', 'IPN'),
        ('Cancer', 'Cancer'),
        ('Control', 'Control'),
        ('Stable Nodule', 'Stable Nodule'),
    )

    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    inclusion_criteria_1 = models.BooleanField()
    inclusion_criteria_2 = models.BooleanField()
    inclusion_criteria_3 = models.BooleanField()
    inclusion_criteria_4 = models.BooleanField()
    inclusion_criteria_5 = models.BooleanField()
    inclusion_criteria_6 = models.BooleanField()
    inclusion_criteria_7 = models.BooleanField()
    inclusion_criteria_8 = models.BooleanField()
    inclusion_criteria_9 = models.BooleanField()
    inclusion_status = models.TextField(max_length=80, choices=inclusion_status_choices, null=True, blank=True)
    consent_form = models.FileField(upload_to='static/', blank=True, null=True)
    consent_form_path = models.CharField(max_length=255, blank=True, null=True)
    screening_status = models.TextField(max_length=50, choices=screening, null=True, blank=True)
    consent_status = models.TextField(max_length=20, choices=consent_status_choices, null=True, blank=True)
    participant_status = models.TextField(max_length=20, choices=participant_status, null=True, blank=True)
    comments = models.TextField(max_length=500, null=True, blank=True)


class participant_info(models.Model):
    first_name = models.TextField(max_length=20)
    last_name = models.TextField(max_length=20)
    date_of_birth = models.DateField()
    recruitment_age = models.TextField(max_length=20)
    phn_num = models.TextField(max_length=20)
    email = models.TextField(max_length=20)
    telephone = models.TextField(max_length=20)
    alt_telephone = models.TextField(max_length=20)
    address = models.TextField(max_length=20)
    city = models.TextField(max_length=20)
    postal_code = models.TextField(max_length=20)
    gp_name = models.TextField(max_length=20)
    gp_msp = models.TextField(max_length=20)
    gp_address = models.TextField(max_length=20)
    gp_telephone = models.TextField(max_length=20)
    gp_fax = models.TextField(max_length=20)




class History(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    field_name = models.CharField(max_length=100, null=True, blank=True)
    old_value = models.TextField(null=True, blank=True)
    new_value = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.content_type} #{self.object_id} - {self.field_name}: {self.old_value} -> {self.new_value}"


class PLCO_score(models.Model):
    education_choices = (
        ('Less than high school graduate', 'Less than high school graduate'),
        ('High school graduate', 'High school graduate'),
        ('Post high school training', 'Post high school training'),
        ('Some college', 'Some college'),
        ('College graduate', 'College graduate'),
        ('Postgraduate', 'Postgraduate'),
    )
    race_choices = (
        ('White, Hispanic, Asian, Other', 'White, Hispanic, Asian, Other'),
        ('Black', 'Black'),
        ('First Nations', 'First Nations'),
    )

    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    age = models.TextField(max_length=20)
    education = models.TextField(max_length=60, choices=education_choices)
    bmi = models.TextField(max_length=20)
    copd = models.BooleanField(default=False)
    cancer_history = models.BooleanField(default=False)
    lung_cancer_history = models.BooleanField(default=False)
    race = models.TextField(max_length=50, choices=race_choices)
    smoking_status = models.BooleanField(default=False)
    avg_num_cigs_smoked_day = models.TextField(max_length=20)
    duration_smoked = models.TextField(max_length=20)
    years_quit = models.TextField(max_length=20)
    




class Protocol_Deviations(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    deviation_type = models.TextField(max_length=20)
    deviation_date = models.DateField()
    clinical_staff_notified = models.BooleanField(default=False)
    deviation_comments = models.TextField(max_length=200)
    


class annual_study_update_part_a(models.Model):

    time_period_choices = (
        ('1Y', '1Y'),
        ('2Y', '2Y'),
        ('3Y', '3Y'),
        ('4Y', '4Y'),
        ('5Y', '5Y'),
        ('6Y', '6Y'),
        ('7Y', '7Y'),
        ('8Y', '8Y'),
    )

    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    update_starting_date = models.DateField()
    update_end_sate = models.TextField(max_length=20)
    followup_time_period = models.TextField(max_length=2, choices=time_period_choices)
    regular_family_doc = models.BooleanField(default=False)
    gp_name = models.TextField(max_length=20)
    gp_address = models.TextField(max_length=20)
    gp_telephone = models.TextField(max_length=20)
    gp_msp = models.TextField(max_length=20)
    gp_fax = models.TextField(max_length=20)
    gp_visit = models.BooleanField(default=False)
    chest_xray = models.BooleanField(default=False)
    chest_xray_date = models.DateField()
    ct_scan_chest = models.BooleanField(default=False)
    ct_scan_chest_date = models.DateField()
    ct_scan_heart = models.BooleanField(default=False)
    ct_scan_heart_date = models.DateField()
    chest_mri = models.BooleanField(default=False)
    chest_mri_date = models.DateField()
    pet_scan = models.BooleanField(default=False)
    pet_scan_date = models.DateField()
    nuclear_scan = models.BooleanField(default=False)
    nuclear_scan_date = models.DateField()
    surgery_chest_lung = models.BooleanField(default=False)
    surgery_chest_lung_date = models.DateField()
    biopsy_chest_lung = models.BooleanField(default=False)
    biopsy_chest_lung_date = models.DateField()
    bronchoscopy = models.BooleanField(default=False)
    bronchoscopy_date = models.DateField()
    lung_cancer_chemo = models.BooleanField(default=False)
    lung_cancer_chemo_date = models.DateField()
    lung_cancer_radiation = models.BooleanField(default=False)
    lung_cancer_radiation_date = models.DateField()
    other_lung_cancer_treatment = models.BooleanField(default=False)
    other_lung_cancer_treatment_date = models.DateField()
    other_lung_cancer_treatment_info = models.TextField(max_length=20)
    other_medical_procedures = models.BooleanField(default=False)
    other_medical_procedures_date = models.DateField()
    other_medical_procedures_info = models.TextField(max_length=20)
    lung_cancer_diagnosis = models.BooleanField(default=False)
    lung_cancer_diagnosis_date = models.DateField()
    lung_cancer_diagnosis_info = models.TextField(max_length=20)
    lung_cancer_treatment = models.BooleanField(default=False)
    lung_cancer_treatment_date = models.DateField()
    lung_cancer_treatment_info = models.TextField(max_length=20)
    lung_chest_care = models.BooleanField(default=False)
    lung_chest_care_date = models.DateField()
    lung_chest_care_info = models.TextField(max_length=20)
    other_cancer_diagnosis = models.BooleanField(default=False)
    other_cancer_diagnosis_date = models.DateField()
    other_cancer_diagnosis_info = models.TextField(max_length=20)
    other_condition_diagnosis = models.BooleanField(default=False)
    other_condition_diagnosis_date = models.DateField()
    other_condition_diagnosis_info = models.TextField(max_length=20)
    heart_disease_heat_attack = models.BooleanField(default=False)
    heart_disease_heat_attack_date = models.DateField()
    heart_disease_heart_info= models.TextField(max_length=20)
    high_cholesterol = models.BooleanField(default=False)
    high_cholestrol_date = models.DateField()
    high_cholerstrol_info = models.BooleanField(default=False)
    new_meds_cholestrol = models.BooleanField(default=False)
    new_meds_cholestrol_date = models.DateField()
    new_meds_cholestrol_info = models.TextField(max_length=20)


class annual_study_update_medications(models.Model):
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    medication_name = models.TextField(max_length=50)
    medication_dose = models.TextField(max_length=50)
    medication_frequency = models.TextField(max_length=50)
    medication_reason = models.TextField(max_length=50)
    medication_start_date = models.DateField()
    medication_last_taken = models.DateField()



class annual_study_update_part_b(models.Model):
    nic_replacement = (
        ('Nicotine Patches', 'Nicotine Patches'),
        ('Nicotine Gum', 'Nicotine Gum'),
        ('Nicotine Nasal Spray', 'Nicotine Nasal Spray'),
        ('Nicotine Lozenges', 'Nicotine Lozenges'),
        ('None', 'None'),
        ('N/A', 'N/A'),
    )
    nic = (
        ('With Nicotine', 'With Nicotine'),
        ('Without Nicotine', 'Without Nicotine'),
    )
    person = (
        ('Participant', 'Participant'),
        ('Participant with assistance from other person', 'Participant with assistance from other person'),
        ('Proxy (family member or friend), participant unable to provide information', 'Proxy (family member or friend), participant unable to provide information'),
    )
    assistance = (
        ('IDEAL study staff member', 'IDEAL study staff member'),
        ('Family member', 'Family member'),
        ('Other', 'Other'),
    )
    
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    smoked_past_12_months = models.BooleanField(default=False)
    smoked_past_12_months_date = models.DateField()
    current_smoker = models.BooleanField(default=False)
    cigs_per_day = models.TextField(max_length=20)
    cigs_per_day_amount = models.TextField(max_length=20)
    reduced_cigs_per_day = models.BooleanField()
    fam_doc_cig_smoking = models.BooleanField(default=False)
    fam_doc_stop_smoking = models.BooleanField(default=False)
    fam_doc_nic_replacement = models.BooleanField(default=False)
    fam_doc_counselling = models.BooleanField(default=False)
    fam_doc_fuvisit = models.BooleanField(default=False)
    past_yr_nic_replacement = models.TextField(max_length=50, choices=nic_replacement)
    past_yr_zyban = models.BooleanField(default=False)
    past_yr_champix = models.BooleanField(default=False)
    past_yr_ecigs = models.BooleanField(default=False)
    past_yr_ecigs_nic = models.TextField(max_length=50, choices=nic)
    past_yr_cessation_program = models.BooleanField(default=False)
    past_yr_cessation_program_study = models.TextField(max_length=20)
    past_yr_smoke_councellor = models.BooleanField(default=False)
    past_yr_smoke_councellor_info = models.TextField(max_length=20)    
    past_yr_quit_24hrs = models.BooleanField(default=False)
    past_yr_quit_24hrs_length = models.PositiveIntegerField()
    completed_form = models.TextField(max_length=75, choices=person)
    person_assisted = models.TextField(max_length=20)
    person_assisted_other = models.TextField(max_length=20)
    date_completed = models.DateField()
    checked_by = models.TextField(max_length=20)
    checked_by_date = models.DateField()

class annual_study_update(models.Model):
    nic_replacement = (
    ('Nicotine Patches', 'Nicotine Patches'),
    ('Nicotine Gum', 'Nicotine Gum'),
    ('Nicotine Nasal Spray', 'Nicotine Nasal Spray'),
    ('Nicotine Lozenges', 'Nicotine Lozenges'),
    ('None', 'None'),
    ('N/A', 'N/A'),
    )
    nic = (
        ('With Nicotine', 'With Nicotine'),
        ('Without Nicotine', 'Without Nicotine'),
    )
    person = (
        ('Participant', 'Participant'),
        ('Participant with assistance from other person', 'Participant with assistance from other person'),
        ('Proxy (family member or friend), participant unable to provide information', 'Proxy (family member or friend), participant unable to provide information'),
    )
    assistance = (
        ('IDEAL study staff member', 'IDEAL study staff member'),
        ('Family member', 'Family member'),
        ('Other', 'Other'),
    )
    time_period_choices = (
    ('1Y', '1Y'),
    ('2Y', '2Y'),
    ('3Y', '3Y'),
    ('4Y', '4Y'),
    ('5Y', '5Y'),
    ('6Y', '6Y'),
    ('7Y', '7Y'),
    ('8Y', '8Y'),
    )
    participant_num = models.ForeignKey(Participant, on_delete=models.CASCADE)
    smoked_past_12_months = models.BooleanField(default=False, blank=True, null=True)
    smoked_past_12_months_date = models.DateField()
    current_smoker = models.BooleanField(default=False, blank=True, null=True)
    cigs_per_day = models.TextField(max_length=20, blank=True, null=True)
    cigs_per_day_amount = models.TextField(max_length=20, blank=True, null=True)
    reduced_cigs_per_day = models.BooleanField()
    fam_doc_cig_smoking = models.BooleanField(default=False, blank=True, null=True)
    fam_doc_stop_smoking = models.BooleanField(default=False, blank=True, null=True)
    fam_doc_nic_replacement = models.BooleanField(default=False, blank=True, null=True)
    fam_doc_counselling = models.BooleanField(default=False, blank=True, null=True)
    fam_doc_fuvisit = models.BooleanField(default=False, blank=True, null=True)
    past_yr_nic_replacement = models.TextField(max_length=50, choices=nic_replacement, blank=True, null=True)
    past_yr_zyban = models.BooleanField(default=False, blank=True, null=True)
    past_yr_champix = models.BooleanField(default=False, blank=True, null=True)
    past_yr_ecigs = models.BooleanField(default=False, blank=True, null=True)
    past_yr_ecigs_nic = models.TextField(max_length=50, choices=nic, blank=True, null=True)
    past_yr_cessation_program = models.BooleanField(default=False, blank=True, null=True)
    past_yr_cessation_program_study = models.TextField(max_length=20, blank=True, null=True)
    past_yr_smoke_councellor = models.BooleanField(default=False, blank=True, null=True)
    past_yr_smoke_councellor_info = models.TextField(max_length=20, blank=True, null=True)    
    past_yr_quit_24hrs = models.BooleanField(default=False, blank=True, null=True)
    past_yr_quit_24hrs_length = models.PositiveIntegerField(blank=True, null=True)
    completed_form = models.TextField(max_length=75, choices=person, blank=True, null=True)
    person_assisted = models.TextField(max_length=20, blank=True, null=True)
    person_assisted_other = models.TextField(max_length=20, blank=True, null=True)
    date_completed = models.DateField( blank=True, null=True)
    checked_by = models.TextField(max_length=20, blank=True, null=True)
    checked_by_date = models.DateField( blank=True, null=True)
    medication_name = models.TextField(max_length=50, blank=True, null=True)
    medication_dose = models.TextField(max_length=50, blank=True, null=True)
    medication_frequency = models.TextField(max_length=50, blank=True, null=True)
    medication_reason = models.TextField(max_length=50, blank=True, null=True)
    medication_start_date = models.DateField( blank=True, null=True)
    medication_last_taken = models.DateField( blank=True, null=True)
    update_starting_date = models.DateField( blank=True, null=True)
    update_end_sate = models.TextField(max_length=20, blank=True, null=True)
    followup_time_period = models.TextField(max_length=2, choices=time_period_choices, blank=True, null=True)
    regular_family_doc = models.BooleanField(default=False, blank=True, null=True)
    gp_name = models.TextField(max_length=20, blank=True, null=True)
    gp_address = models.TextField(max_length=20, blank=True, null=True)
    gp_telephone = models.TextField(max_length=20, blank=True, null=True)
    gp_msp = models.TextField(max_length=20, blank=True, null=True)
    gp_fax = models.TextField(max_length=20, blank=True, null=True)
    gp_visit = models.BooleanField(default=False, blank=True, null=True)
    chest_xray = models.BooleanField(default=False, blank=True, null=True)
    chest_xray_date = models.DateField(blank=True, null=True)
    ct_scan_chest = models.BooleanField(default=False, blank=True, null=True)
    ct_scan_chest_date = models.DateField( blank=True, null=True)
    ct_scan_heart = models.BooleanField(default=False, blank=True, null=True)
    ct_scan_heart_date = models.DateField( blank=True, null=True)
    chest_mri = models.BooleanField(default=False, blank=True, null=True)
    chest_mri_date = models.DateField( blank=True, null=True)
    pet_scan = models.BooleanField(default=False, blank=True, null=True)
    pet_scan_date = models.DateField( blank=True, null=True)
    nuclear_scan = models.BooleanField(default=False, blank=True, null=True)
    nuclear_scan_date = models.DateField( blank=True, null=True)
    surgery_chest_lung = models.BooleanField(default=False, blank=True, null=True)
    surgery_chest_lung_date = models.DateField(blank=True, null=True)
    biopsy_chest_lung = models.BooleanField(default=False, blank=True, null=True)
    biopsy_chest_lung_date = models.DateField( blank=True, null=True)
    bronchoscopy = models.BooleanField(default=False, blank=True, null=True)
    bronchoscopy_date = models.DateField( blank=True, null=True)
    lung_cancer_chemo = models.BooleanField(default=False, blank=True, null=True)
    lung_cancer_chemo_date = models.DateField(blank=True, null=True)
    lung_cancer_radiation = models.BooleanField(default=False, blank=True, null=True)
    lung_cancer_radiation_date = models.DateField( blank=True, null=True)
    other_lung_cancer_treatment = models.BooleanField(default=False, blank=True, null=True)
    other_lung_cancer_treatment_date = models.DateField( blank=True, null=True)
    other_lung_cancer_treatment_info = models.TextField(max_length=20, blank=True, null=True)
    other_medical_procedures = models.BooleanField(default=False, blank=True, null=True)
    other_medical_procedures_date = models.DateField( blank=True, null=True)
    other_medical_procedures_info = models.TextField(max_length=20, blank=True, null=True)
    lung_cancer_diagnosis = models.BooleanField(default=False, blank=True, null=True)
    lung_cancer_diagnosis_date = models.DateField( blank=True, null=True)
    lung_cancer_diagnosis_info = models.TextField(max_length=20, blank=True, null=True)
    lung_cancer_treatment = models.BooleanField(default=False, blank=True, null=True)
    lung_cancer_treatment_date = models.DateField( blank=True, null=True)
    lung_cancer_treatment_info = models.TextField(max_length=20, blank=True, null=True)
    lung_chest_care = models.BooleanField(default=False, blank=True, null=True)
    lung_chest_care_date = models.DateField( blank=True, null=True)
    lung_chest_care_info = models.TextField(max_length=20, blank=True, null=True)
    other_cancer_diagnosis = models.BooleanField(default=False, blank=True, null=True)
    other_cancer_diagnosis_date = models.DateField( blank=True, null=True)
    other_cancer_diagnosis_info = models.TextField(max_length=20, blank=True, null=True)
    other_condition_diagnosis = models.BooleanField(default=False, blank=True, null=True)
    other_condition_diagnosis_date = models.DateField( blank=True, null=True)
    other_condition_diagnosis_info = models.TextField(max_length=20, blank=True, null=True)
    heart_disease_heat_attack = models.BooleanField(default=False, blank=True, null=True)
    heart_disease_heat_attack_date = models.DateField( blank=True, null=True)
    heart_disease_heart_info= models.TextField(max_length=20, blank=True, null=True)
    high_cholesterol = models.BooleanField(default=False, blank=True, null=True)
    high_cholestrol_date = models.DateField( blank=True, null=True)
    high_cholerstrol_info = models.BooleanField(default=False, blank=True, null=True)
    new_meds_cholestrol = models.BooleanField(default=False, blank=True, null=True)
    new_meds_cholestrol_date = models.DateField( blank=True, null=True)
    new_meds_cholestrol_info = models.TextField(max_length=20, blank=True, null=True)