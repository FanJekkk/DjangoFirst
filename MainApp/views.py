from django.shortcuts import render, HttpResponse

name = "Денис"
surname = "Тепляков"
email = "denteplyakov2020@gmail.com"
items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]

def items_list(request):
    result = "<ol>"
    for i in items:
        result +=f"<li><a href='/item/{i['id']}'>{i['name']}</a></li>"
    result += "</ol>"
    return HttpResponse(result)

def about(request):
    info = f"""Имя: <strong>{name}</strong><br>
             Фамилия: <strong>{surname}</strong><br>
             телефон: <strong>8-923-600-01-02</strong><br>
             email: <strong>{email}</strong>"""
    return HttpResponse(info)

def home(request):
    text = f"""<h1> "Изучаем django" </h1>
    <strong> Автор </strong>: <i> {surname}
    {name[0]}. </i>"""
    return HttpResponse(text)

def item_page(request,id):
    for item in items:
        if item["id"] == id:
            item_str = f"Товар: <b>{item['name']}</b> количество: {item['quantity']}"
            return HttpResponse(item_str)
    return HttpResponse(f"Товар с id={id} не найден")

