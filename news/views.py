from django import views
from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm, SendEmail
from django.views import View
# Create your views here.


class Index(View):
    def get(self, request):

        return HttpResponse('xin chao')

class Add_post(View):
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html',{'f':a} )


class SaveNews(View):
    def post(self, request):
        if request.method == "POST":
            g = PostForm(request.POST)
            if g.is_valid():#is_valid là phù hợp với kiểu dữ liệu
                g.save()
                return HttpResponse("Thành công")
            else:return HttpResponse(g.errors)
        else:return HttpResponse("Không phải post")


class Send_email(View):
    def get(self, request):
        s = SendEmail()
        return render(request, 'news/send_email.html', {'f':s})



class Handle_send_email(View):
    def post(self, request):
        if request.method == "POST":
            r = SendEmail(request.POST)
            if r.is_valid():
                title = r.cleaned_data['title']
                email = r.cleaned_data['email']
                content = r.cleaned_data['content']
                cc= r.cleaned_data['cc']
                context = {
                    'title':title,
                    'content':content,
                    'email':email,
                    'cc':cc
                }
                context2 = {
                    'f':r
                }
                return render(request, 'news/print_content_send_email.html', context2)
            else:return HttpResponse('Không dúng kiểu dữ liệu')
        else:return HttpResponse('Không phải phương thức POST')