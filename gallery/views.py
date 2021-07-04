from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
import datetime as dt
from .models import Image,Location,Category
from django.core.management import execute_from_command_line
from .models import Image


# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')
def index(request):
    '''
    Method to return all images, locations, categories
    '''
    images = Image.objects.all()
    location = Location.objects.all()
    categories = Category.get_all_categories()
    context = {
        "images":images,
        "location":location,
        "categorie": categories,
    }
    
    return render(request, 'all-images/welcome.html', context)

def image_of_day(request):
    date = dt.date.today()
    return render(request, 'all-images/today-image.html', {"date": date,})
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Images for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_image(request,past_date):
    try:
        # Converts data from the string Url
     date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
        
    if date == dt.date.today():
        return redirect(image_of_day)
    
        # Converts data from the string Url
    date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
    day = convert_dates(date)
    
    html = f'''
        <html>
            <body>
                <h1>Image for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)