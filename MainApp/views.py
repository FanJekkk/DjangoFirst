from django.shortcuts import render, HttpResponse

name = "Денис"
surname = "Тепляков"
email = "denteplyakov2020@gmail.com"
phone = "8-923-600-01-02"
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]

def items_list(request):
    # result = "<ol>"
    # for i in items:
    #     result +=f"<li><a href='/item/{i['id']}'>{i['name']}</a></li>"
    # result += "</ol>"
    # return HttpResponse(result)
    context = {
        "items": items
    }
    return render(request,"items.html", context)

def about(request):
    context = {
        "name": name,"surname": surname, "email": email, "phone": phone
    }
    return render(request,"about.html",context)

def home(request):
    return render(request,"index.html")

def item_page(request,id):
    for item in items:
        if item["id"] == id:
            item_str = f"Товар: <b>{item['name']}</b> количество: {item['quantity']}"
            return HttpResponse(item_str)
    return HttpResponse(f"Товар с id={id} не найден")

