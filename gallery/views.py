from django.shortcuts import render,HttpResponse
from .models import Product
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')

def add(request):
 if request.method=='POST':
    name=request.POST['name']
    description=request.POST['description']

    new_product=Product(name=name,description=description)
    new_product.save()
    return HttpResponse('PRODUCT ADDED SUCCESSFULLY!!')


 elif request.method=='GET':
    return render(request, 'add.html')
 else:
    return HttpResponse('INVALID REQUEST!!')

def remove(request,pro_idea=0):
  if pro_idea:
      try:
        pro_to_be_removed=Product.objects.get(id=pro_idea)
        pro_to_be_removed.delete()
        return HttpResponse('PRODUCT REMOVED SUCCESSFULLY!!')
      except:
        return HttpResponse('PRODUCT NOT FOUND!!')

  pros=Product.objects.all()
  context={
        'pros':pros
    }
  return render(request, 'remove.html',context)


def filters(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        pros = Product.objects.all()
        if name:
            pros = pros.filter(Q(name__icontains=name))
        if description:
            pros = pros.filter(Q(description__icontains=description))

        context = {'pros': pros}
        return render(request, 'filters.html', context)
    elif request.method == 'GET':
        return render(request, 'filters.html')
    else:
        return HttpResponse('Invalid request method!', status=405)


def view(request):
    pro=Product.objects.all()
    context={
        'pro':pro
    }
    print(context)
    return render(request,'view.html',context)