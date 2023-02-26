from django.db import models


# Create your models here(DB table).

#Drinks Category DB table 
class DrinksCategory(models.Model):
    category_name=models.CharField(max_length=200)

# Drinks Db Table with Fk making many-to-one relationship each drink assign to drink category 
class Drinks(models.Model):
    #two columns/attributes
    drink=models.CharField(max_length=200)
    price=models.IntegerField(null=True)
    #fk(asociated model,setting) relatedname:instead of showing in the Db by category_id it'll show the category_name
    #The PROTECT argument prevents the deletion of the model object that is referenced. 
    category_id=models.ForeignKey(DrinksCategory,on_delete=models.PROTECT,default=None)
    
    def __str__(self):
        return self.drink

#Model form that receive data from user and store it in db table (model->is a db table)
class Booking(models.Model):
    first_name=models.CharField(max_length = 200)
    last_name=models.CharField(max_length = 200)
    guest_count=models.IntegerField()
    reservation_time=models.DateField(auto_now=True)
    comments=models.CharField(max_length = 1000)

#to shows the customer name in admin site instead of showing as Booking obj1
    def __str__(self):
        return self.first_name+ ' ' + self.last_name


# Create employee model.
class Employee(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    role = models.CharField(max_length=100)
    shift = models.IntegerField()

    def __str__(self):
        return self.first_name       

#create menu model to display on the web page using templates
class Menu(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField()
    menu_item_description=models.TextField(max_length=1000,default="")
    #null=true doesnt have to have an image ,where we wanna upload
    menu_item_img=models.ImageField(null=True,blank=True,upload_to="images/")

#shows the drink name in django admin page
    def __str__(self):
        return self.name

