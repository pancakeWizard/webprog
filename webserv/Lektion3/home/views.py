from django.shortcuts import render
content = "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Nemo odio deleniti modi. Eveniet, sunt ex rem nostrum ad totam facilis ea adipisci sequi tempore cum officiis voluptatibus officia neque eligendi. Dolore perferendis, libero voluptatem asperiores earum sequi suscipit neque? Perspiciatis perferendis architecto officia dolores sint voluptatibus quia culpa omnis aliquid nemo minus asperiores placeat, alias facilis iure sed quaerat, quidem harum laborum! Accusantium, sequi expedita saepe alias commodi nulla libero aliquam quaerat amet adipisci veniam iusto nobis laborum inventore tempora dolores id ad, soluta consectetur delectus illum, magnam praesentium. Sint a sed atque adipisci? Exercitationem eligendi voluptates beatae odit repellat!"

# Create your views here.
def home(request):
    ctype = ""
    return render(request, "index.html", {"content":content, "ctype":ctype})

def lists(request):
    ctype = "list"
    lists = ["item1", "item2", "item3"]
    return render(request,"index.html",{"ctype":ctype, "lists":lists})