from django.shortcuts import render
from django.http import HttpResponse
from Base_App.models import BookTable, AboutUs, Feedback, ItemList, Items
# Create your views here.

def HomeView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    review = Feedback.objects.all()
    return render(request, 'home.html',{'items': items, 'list': list, 'review': review})


def AboutView(request):
    data = AboutUs.objects.all()
    return render(request, 'about.html',{'data': data})


def MenuView(request):
    items =  Items.objects.all()
    list = ItemList.objects.all()
    return render(request, 'menu.html', {'items': items, 'list': list})

# def MenuView(request):
#     # جلب الفئة المختارة من الـ GET request
#     selected_category = request.GET.get('category', 'all')

#     # جلب جميع الفئات من ItemList
#     categories = ItemList.objects.all()

#     # جلب العناصر بناءً على الفئة المختارة
#     if selected_category == 'all':
#         items = Items.objects.all()  # جلب كل العناصر إذا كانت الفئة "all"
#     else:
#         items = Items.objects.filter(Category_name__iexact=selected_category)  # تصفية حسب الفئة

#     return render(request, 'menu.html', {
#         'items': items, 
#         'categories': categories, 
#         'selected_category': selected_category  # تمرير الفئة المختارة للقالب
#     })


def BookTableView(request):
    if request.method=='POST':
        name = request.POST.get('user_name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('user_email')
        total_person = request.POST.get('total_person')
        booking_data = request.POST.get('booking_data')

        if name != '' and len(phone_number) == 10 and email != '' and total_person != 0 and booking_data != '':
            data = BookTable(Name=name, Phone_number=phone_number,
                             Email=email,Total_person=total_person,
                             Booking_date=booking_data)
            data.save()
    return render(request, 'book_table.html')

def FeedbackView(request):
    return render(request, 'feedback.html')