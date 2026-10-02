from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from django.http.request import HttpRequest
from foodcategory.models import FoodCategory, FoodItem
from hotel.models import Hotel
from hotel.views import getHotel
from foodcategory.forms import FoodCategoryForm, FoodItemForm


# Create your views here.
def foodCategory_index(request:HttpRequest):
    hotel= getHotel(request)
    food_category_form=FoodCategoryForm()
    msg=""
    if FoodCategoryForm.create(request,hotel)!=None:
        msg="Success fully created food category"
    context ={
        "food_category":FoodCategory.find_all(hotel),
        "food_category_form":food_category_form,
        "msg":msg
    }
    return render(request, "foodCategory/index.html",context)

def foodCategory_edit(request:HttpRequest,category_id:int):
    foodCategory=FoodCategory.find_by_id(category_id)
    food_category_form=FoodCategoryForm(instance=foodCategory)
    if request.method=="POST":
        food_category_form=FoodCategoryForm(request.POST,instance=foodCategory)
        if food_category_form.is_valid():
            food_category_form.save()
            return redirect("foodCategory_index")
    context ={
        "food_category_form":food_category_form,
        "category_id":category_id
    }
    return render(request, "foodCategory/edit.html",context)

def food_category_manage_item(request:HttpRequest,category_id:int):

    food_item_form=FoodItemForm()
    category=FoodCategory.find_by_id(category_id)

    hotel = getHotel(request)
    FoodItemForm.create(request,category,hotel)
    food_items = FoodItem.find_by_category(category_id)
    print(food_items)
    context={
        "food_item_form":food_item_form,
        "category":category,
        "food_items":food_items
    }
    return render(request, "foodCategory/manageitem.html",context)



def foodItem_index(request:HttpRequest):
    hotel= getHotel(request)
    food_item_form=FoodItemForm()
    msg=""
    if FoodItemForm.create(request,hotel)!=None:
        msg="Success fully created food category"
    context ={
        "food_item":FoodItemForm.find_all(hotel),
        "food_item_form":food_item_form,
        "msg":msg
    }
    return render(request, "fooditem/index.html",context)

def foodItem_edit(request:HttpRequest,id:int):
    foodItem=FoodItem.find_by_id(id)
    foodItem_form=FoodItemForm(instance=foodItem)
    if request.method=="POST":
        foodItem_form=FoodItemForm(request.POST,instance=foodItem)
        if foodItem_form.is_valid():
            foodItem_form.save()
            return redirect("foodCategory_index")
    context ={
        "foodItem_form":foodItem_form,
        "foodItem":foodItem
    }
    return render(request, "fooditem/edit.html",context)


def foodItem_delete(request:HttpRequest,id:int):
    foodItem=FoodItem.find_by_id(id)
    category_id = foodItem.category.id
    if foodItem:
        foodItem.delete()
    return redirect("food_category_manage_item", category_id=category_id)


def foodCategory_delete(request:HttpRequest,category_id:int):
    foodCategory=FoodCategory.find_by_id(category_id)
    if foodCategory:
        foodCategory.delete()
    return redirect("foodCategory_index")