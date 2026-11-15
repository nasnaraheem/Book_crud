from django.shortcuts import render
from django.views.generic import View
from json import loads
from library.models import Book
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator


# Create your views here.
@method_decorator(csrf_exempt,name="dispatch")
class BookListCreateView(View):
    def get(self,request):
        qs=Book.objects.all().values()
        response_data=list(qs)
        return JsonResponse(response_data,safe=False)

    def post(self,request):
        json_data=request.body
        form_data=loads(json_data)
        Book.objects.create(**form_data)
        response_data={"message" : "created"}
        return JsonResponse(response_data)

    
@method_decorator(csrf_exempt,name="dispatch")
class BookRetriveUpdateDelete(View):
    def get(self,request,pk=None):
        qs=Book.objects.filter(id=pk).values()
        response_data=list(qs)
        return JsonResponse(response_data)

    def put(self,request,pk=None):
        json_data=request.body
        form_data=loads(json_data)
        Book.objects.filter(id=pk).update(**form_data)
        response_data={"message" : "updated"}
        return json_data(response_data)

    def delete(self,request,pk=None):
        Book.objects.filter(id=pk).delete()
        response_data={"message" : "deleted"}
        return JsonResponse(response_data)



