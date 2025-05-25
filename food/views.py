from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm

# Create your views here.

def index(request):
    item_list = Item.objects.all()
    template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return HttpResponse(template.render(context, request))

def item(request):
    return HttpResponse("You're looking at item ")

def detail(request, item_id):
    item = Item.objects.get(pk=item_id)
    context = {
        'item': item,
    }
    
    return render(request, 'food/detail.html', context)

def create_item(request):
    form = ItemForm(request.POST or None,)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form})

def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form': form, 'item': item})

def delete_item(request, id):
    item = Item.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    # To upload your code to GitHub, follow these steps:
    # 1. Initialize a git repository in your project folder:
    #    git init
    # 2. Add your files:
    #    git add .
    # 3. Commit your changes:
    #    git commit -m "Initial commit"
    # 4. Create a new repository on GitHub.
    # 5. Link your local repo to GitHub:
    #    git remote add origin https://github.com/your-username/your-repo-name.git
    # 6. Push your code:
    #    git push -u origin master