from django.shortcuts import render
from django.http import HttpResponse
from myapp.forms import BookingForm
from .models import Menu


def form_view(request):
    form =BookingForm()
    if request.method=='POST':
       form =BookingForm(request.POST)
       if form.is_valid():
        form.save()
    context = {"form" : form}
    return render(request, "booking.html", context)    

def home(request):
    return render(request,'home.html')



# Create your views here ,pass the dish param u added in urls.py path.
def dishesitems(request,dish):
    
     #dictionary called items
    items={
        #keys values pair
        'Pasta':'Pasta is a type of food typically made from an unleavened dough of wheat flour mixed with water or eggs, and formed into sheets or other shapes, then cooked by boiling or baking.',
        'Falafel':"Falafel is a deep-fried ball or patty-shaped fritter in Middle Eastern cuisine made from ground chickpeas, broad beans, or both.",
        'cheesecake':"Cheesecake is a sweet dessert consisting of one or more layers."
    }
#pass the dic items to dish save the values to var name description
    description =items[dish]

    return HttpResponse(f"<h1> {dish} </h1>"+ description)

#new view func to add drinks items    
def drinksitems(request,drink):
    ditem={
        'mocha':"A caffè mocha, also called mocaccino, is a chocolate-flavoured warm beverage that is a variant of a caffè latte,",
        'tea': "Tea is an aromatic beverage prepared by pouring hot or boiling water over cured or fresh leaves of Camellia sinensis",
        'lemonade':"Lemonade is a sweetened lemon-flavored beverage. There are varieties of lemonade found throughout the world."
    }
    drinkdesc=ditem[drink]
    return HttpResponse(f"<h1>{drink}</h1>"+drinkdesc)

def about(request):
    #dict var key-value pair , pass the key to html <p> tag in html page(about.html)
    about_content={'about':" Based in Atlanta,Illinois,Little Lemon is a family owned Mediterranean restaurant,focused on traditional recipes served woith a modern twist. The chefs draw inspiration from Italians,Greek, and Turkish culture and have a menu of 12-15 items that they rotate seasonally.The restaurant has a rustic and relaxed atmosphere with moderate prices, making it popular place for a meal any time of the day."}
    #the render func takes 3 param request obj,path(name of the html file),dict var|
    return render(request, "about.html", about_content)   


#display the menu item from db using template
def menu(request):
    #get all obj in menu model
      menu_items = Menu.objects.all().values()
      items_dict = {"menu": menu_items}
      return render(request, "menu.html", items_dict)
   #pass menu to html for loop, menu is the key of the dict
   

#display_menu_item
def display_menu_items(request,id=None):
  if (id):
    menu_item=Menu.objects.get(id=id)
  else:
     menu_item=""
  return render(request,'menu_item.html',{"menu_item": menu_item})  
