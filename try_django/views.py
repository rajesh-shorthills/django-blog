from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
# def home_page(request):
#     return HttpResponse("<h1>Hello World</h1>")



#DRY means Don't repeat yourself
def home_page(request):
    title = "HomePage Love"
    context = {"title":"Title Hidden. Ypu Need Permissionfor this"}
    if request.user.is_authenticated:
        context = {"title":title,"my_list":[1,2,3,4,5]} ## NOte we can pass dict of variable
    # doc = "<h1>{title}</h1>".format(title=title)
    # django_rendered_doc = "<h1>{{title}}</h1>".format(title=title)## Django template engine use double curly bracket
    return render(request,"home.html",context)

def about_page(request):
     return render(request,"about.html",{"title":"About us"})

def contact_page(request):
    # Print what data is comming with request
    # print(request.POST)

    form = ContactForm(request.POST or None)
    context = {"title":"Contact us","form":form}
    if form.is_valid():
        print(form.cleaned_data)
        form = ContactForm()
    return render(request,"form.html",context)

def example_page(request):
    context = {"title":"Example"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    rendered_item = template_obj.render(context)
    return HttpResponse(rendered_item)