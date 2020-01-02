from django.shortcuts import render,get_object_or_404
from .models import BlogPost
from django.http import Http404
from .forms import BlogPostForm,BlogPostModelForm
# Create your views here.

#GET-> 1 object
#filter-->[]


# def blog_post_detail_page(request, post_id): # This was based upon id

# #Below is based upon slug
# def blog_post_detail_page(request, slug):
#     print("Django Says..",request.method, request.path, request.user)
#     # print(post_id.__class__)
#     # try:
#     #     obj = BlogPost.objects.get(id=post_id) #query that goes into database and return data
#     # except BlogPost.DoesNotExist:
#     #     raise Http404
#     # except ValueError:
#     #     raise Http404
#     # obj = get_object_or_404(BlogPost,id=post_id)
#     # obj = get_object_or_404(BlogPost,slug=slug)
#     queryset = BlogPost.objects.filter(slug=slug)
#     if queryset.count() == 0:
#         raise Http404
        
#     obj = queryset.first()
    
#     template_name = 'blog_post_detail.html'
#     context = {"object":obj}
#     return render(request,template_name,context)


#CRUD -- Create Reterive Update Delete

# GET --> Reterive / list
#POST --> Create things / update things / Delete things


def blog_post_list_view(request):
    # List out objects
    # could be search
    qs = BlogPost.objects.all() # queryset --> Return a list of objects
    # qs = BlogPost.objects.filter(title__icontains="2nd") # Result with filter
    template_name = "blog/list.html" # These are just varbale name like template_name, context . These are not predefined namespace in django
    context = {"objects_list":qs}
    return render(request,template_name,context) 

def blog_post_create_view(request):
    print("*******************")
    # Create objects
    # ? use a form
    
    # form = BlogPostForm(request.POST or None)
    print(request.POST)
    # form1 = BlogPostForm(request.POST or None)
    form1 = BlogPostModelForm(request.POST or None)
    if form1.is_valid():
        print(form1.cleaned_data)
        # obj = BlogPost.objects.create(**form1.cleaned_data)
        # form1 = BlogPostForm()
        obj = form1.save(commit=False)# Do not save the form, only get data
        obj.title = form1.cleaned_data.get("title") +"New"## get the title and append something
        obj.save()
        form1 = BlogPostModelForm()# To clear form Data
    context = {"title":"New Post","form":form1}
    return render(request,"blog/form.html",context)
    # if form.is_valid():
    #     print(form.cleaned_data)
    #     # title = BlogPost.objects.create(title=form.title)# set only title
    #     # obj = BlogPost.objects.create(**form.cleaned_data)
    #     # obj.save()
    #     # form =BlogPostForm()

    # #Note we can data from form and can set in multiple model(means one to many)
    # context = {"form":form}
    # template_name = "blog/form.html"
    # return render(request,template_name,context) 

def blog_post_detail_view(request,slug):
    # Get 1 object
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj}
    template_name = "blog/detail.html"
    return render(request,template_name,context)  

def blog_post_update_view(request):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj,"form":None}
    template_name = "blog/update.html"
    return render(request,template_name,context)   

def blog_post_delete_view(request):
    obj = get_object_or_404(BlogPost,slug=slug)
    context = {"object":obj}
    template_name = "blog/delete.html"
    return render(request,template_name,context)   