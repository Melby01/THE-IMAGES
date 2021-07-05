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
        "category": categories,
    }
    
    return render(request, 'all-images/index.html', context)

def image_of_day(request):
    date = dt.date.today()
    return render(request, 'all-images/today-image.html', {"date": date,})
    day = convert_dates(date)
    html = f'''
        <html>
            <body>
                <h1>Images {day} {date.day}-{date.month}-{date.year}</h1>
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
                <h1>Images {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def search_results(request):
    
    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'all-images/search.html',{"message":message,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-news/search.html',{"message":message})
    
def view_image(request,gallery_id):
    '''
    Method to get image by id
    '''
    try:
        image = Image.objects.get(id =  gallery_id)
    except DoesNotExist:
        raise Http404()
    return render(request, "all-images/view.html", {"gallery":image})