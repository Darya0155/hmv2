from typing import MutableMapping, Any

import django.forms as forms



from foodcategory.models import FoodCategory, FoodItem
from hotel.models import Hotel


class FoodCategoryForm(forms.ModelForm):
    class Meta:
        model = FoodCategory
        fields = '__all__'
        exclude = ['hotel']
    @staticmethod
    def create(request,hotel:Hotel)->FoodCategory|None:
        food_category=None
        if request.method=="POST":
            food_category_form=FoodCategoryForm(request.POST)
            if food_category_form.is_valid():
                food_category=food_category_form.save(commit=False)
                food_category.hotel=hotel
                food_category.save()
        return food_category

class FoodItemForm(forms.ModelForm):
    class Meta:
        model = FoodItem
        fields = '__all__'
        exclude = ['deleted_at','hotel','category']
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

    @staticmethod
    def create(request,category:FoodCategory,hotel:Hotel)->FoodItem|None:
        food_item=None
        if request.method=="POST":
            food_item_form=FoodItemForm(request.POST)
            if food_item_form.is_valid():
                food_item=food_item_form.save(commit=False)
                food_item.hotel=hotel
                food_item.category=category
                food_item.save()
        return food_item