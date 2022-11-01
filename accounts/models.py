from ast import Assign
from email.policy import default
from pickletools import int4
from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class BusinessRegister(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    typeofuser = models.CharField(max_length=200, default="None")
    company_name = models.CharField(max_length=200)
    company_number = models.PositiveIntegerField()
    tax_id = models.PositiveIntegerField()
    company_industry = models.CharField(max_length=200)
    company_date = models.DateField()
    # company_email = models.EmailField(max_length=50)
    NIN = models.CharField(max_length=200)
    BVN = models.CharField(max_length=200)
    phoneno = models.PositiveIntegerField()
    houseno = models.CharField(max_length=200)
    street_name = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    em1 = models.CharField(max_length=200)
    em2 = models.CharField(max_length=200)
    em3 = models.CharField(max_length=200)
    em4 = models.CharField(max_length=200)
    signature = models.ImageField(upload_to='businesssignpic')
    photo = models.ImageField(upload_to='businessprofilepic')
    
    print(company_name)

    def str(self):
        return str(self.id)


class  IndividualRegister(models.Model):
   try:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    typeofuser = models.CharField(max_length=200, default="None")
    f_name = models.CharField(max_length=200)
    l_name = models.CharField(max_length=200)
    print(l_name)

    phone = models.PositiveIntegerField()
    house_number = models.CharField(max_length=200)
    street_name = models.CharField(max_length=500)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    birthdate = models.DateField()
    gender = models.CharField(max_length=200)
    occupation = models.CharField(max_length=200)
    NIN = models.CharField(max_length=200)
    BVN = models.CharField(max_length=200)
    joint_account = models.BooleanField(default=False)

    individual_signature = models.ImageField(upload_to='individualsignpic')
    individual_photo = models.ImageField(upload_to='individualprofilepic')

    kin_name = models.CharField(max_length=200)
    kin_relationship = models.CharField(max_length=200)
    kin_phone = models.PositiveIntegerField()
    kin_house_number = models.CharField(max_length=200)
    kin_street_name = models.CharField(max_length=500)
    kin_city = models.CharField(max_length=200)
    kin_state = models.CharField(max_length=200)
    kin_country = models.CharField(max_length=200)

    
    def str(self):
        return str(self.id)
   except Exception as e:
    print(e)

class  AnotherJoinAccountRegister(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    individual_user = models.ForeignKey(IndividualRegister, on_delete=models.CASCADE)
    another_name = models.CharField(max_length=200)
    another_phone = models.PositiveIntegerField()
    another_house_number = models.CharField(max_length=200)
    another_street_name = models.CharField(max_length=500)
    another_city = models.CharField(max_length=200)
    another_state = models.CharField(max_length=200)
    another_country = models.CharField(max_length=200)
    another_birthdate = models.DateField()
    another_gender = models.CharField(max_length=200)
    another_occupation = models.CharField(max_length=200)
    another_signature = models.ImageField(upload_to='anotherjointsignpic')
    another_photo = models.ImageField(upload_to='anotherjointprofilepic')

    def str(self):
        return str(self.id)


CATEGORY_CHOICES = (
('corporate','corporate'),
('individual','individual'),
)

class Product(models.Model):

    typeofuser = models.CharField(choices= CATEGORY_CHOICES, max_length=200)
    title = models.CharField(max_length=200)
    title2 = models.CharField(max_length=200)
    product_image = models.ImageField(upload_to='productpic')

    def str(self):
        return str(self.id)


class SubProduct(models.Model):
 try:
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sub_title = models.CharField(max_length=200)
    sub_title2 = models.CharField(max_length=200)
    # product_detail_title = models.TextField()
    duration_year = models.CharField(max_length=200,default='None')
    duration_month = models.CharField(max_length=200,default='None')
    selling_price = models.IntegerField()
    Principle = models.IntegerField()
    Rate = models.IntegerField()
    Date = models.DateField()
    benifits = models.TextField(default='None')
    plan_feature = models.TextField(default='None')
    sub_product_image = models.ImageField(upload_to='subproductpic')
    Total_S = models.FloatField(default='None')
    Minemun_O = models.FloatField(default='None')
    Scope =  models.TextField()
    Assign = models.CharField(max_length=200)
    

    def str(self):
        return str(self.id)
 except Exception as e:
    print(e)

class assign_products(models.Model):
 try:
    product_id = models.IntegerField()
    user_id = models.IntegerField()
  
    def str(self):
        return str(self.id)
 except Exception as e:
    print(e)


class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(SubProduct, on_delete=models.SET_NULL, default= None, null=True)
    product_title = models.CharField(max_length=100,default=None,null=True)
    price = models.FloatField()
    modeofpayment = models.CharField(max_length=100)
    payment_id = models.CharField(max_length=100)
    ordered_date_time = models.DateTimeField(auto_now_add =True)
    ordered_date = models.DateField(auto_now_add =True)
    due_date = models.DateField(default='1970-01-01')
    updated = models.DateTimeField(auto_now=True)
    payment_status = models.CharField(max_length=50)
    quantity = models.FloatField()
    frequency = models.CharField(max_length=200, default='Null')
    def str(self):
        return str(self.id)


class Quote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(SubProduct, on_delete=models.SET_NULL, default= None, null=True)
    quote_date_time = models.DateTimeField(auto_now_add =True)
    quote_date = models.DateField()
    quote_quantity = models.IntegerField(default = 1)
    total_p = models.IntegerField()
    frequency = models.CharField(max_length=200)
    def str(self):
        return str(self.id)


class Contact(models.Model):

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=50)
    contact = models.PositiveIntegerField()
    message = models.TextField()
    checked = models.BooleanField(default=False)

    def str(self):
        return str(self.id)

class Subscriber(models.Model):

    email = models.EmailField(max_length=50)

    def str(self):
        return str(self.id)




class HomeBanner(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='home/banner')

    def str(self):
        return str(self.id)

class HomeExploreProducts(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    exp_image = models.ImageField(upload_to='home/exploreproduct')

    def str(self):
        return str(self.id)

class HomeTestinomials(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    testi_image = models.ImageField(upload_to='home/testinomials')

    def str(self):
        return str(self.id)

class HomeWhatWeDo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    icon_image = models.ImageField(upload_to='home/whatwedo')
    icon_image_hover = models.ImageField(upload_to='home/whatwedo')

    def str(self):
        return str(self.id)


class HomeInfoSection(models.Model):
    home_box1_title = models.CharField(max_length=200)
    box1_description = models.TextField()
    home_box2_title= models.CharField(max_length=200)
    box2_description = models.TextField()
    home_box3_title = models.CharField(max_length=200)
    box3_description = models.TextField()
    about_head = models.TextField()
    about_description = models.TextField()
    about_mission = models.TextField()
    about_vision = models.TextField()
    about_commitment = models.TextField()
    about_image = models.ImageField(upload_to='home/homeinfosection')

    contact_image = models.ImageField(upload_to='home/homeinfosection', default="img/123.png")

    hotline = models.PositiveIntegerField()
    email = models.EmailField(max_length=50)

    market_update = models.CharField(max_length=200)
    news = models.CharField(max_length=200)
    sectornews = models.CharField(max_length=200)
    upcomingevents = models.CharField(max_length=200)


    def str(self):
        return str(self.id)


class AboutInfoSection(models.Model):
    about_description = models.TextField()
    about_description2 = models.TextField()
    about_description3 = models.TextField()
    about_image = models.ImageField(upload_to='home/aboutinfosection')

    def str(self):
        return str(self.id)

class AboutTestinomials(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    description = models.TextField()
    testi_image = models.ImageField(upload_to='home/testinomials')

    def str(self):
        return str(self.id)

class AboutCompanyCore(models.Model):
    description = models.TextField()
    core_image = models.ImageField(upload_to='home/companycore')

    def str(self):
        return str(self.id)


class AboutTeamMembers(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    description = models.TextField()
    member_image = models.ImageField(upload_to='home/teammembers')

    def str(self):
        return str(self.id)
class AboutBoardMembers(models.Model):
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    description = models.TextField()
    member_image = models.ImageField(upload_to='home/boardmembers')
    
    def str(self):
        return str(self.id)

class News(models.Model):
    title = models.CharField(max_length=500,null=True)
    description = models.TextField(null=True)
    doc = models.CharField(max_length=500,default='None',null=True)
    newspic = models.ImageField(upload_to='newspic',null=True)
    def str(self):
        return str(self.id)