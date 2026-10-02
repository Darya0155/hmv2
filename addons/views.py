from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from addons.forms import AddonForm
from addons.models import Addon
from hotel.views import getHotel


@login_required
def index(request):
    addons = Addon.find_all(getHotel(request))
    context = {'addons': addons}
    return render(request, 'addons/index.html',context)

@login_required
def add_new_addon(request):
    add_on_forms = AddonForm()
    context = {'add_on_forms': add_on_forms}
    if request.method == 'POST':
        add_on_forms = AddonForm(request.POST)
        if add_on_forms.is_valid():
            add_on_forms=add_on_forms.save(commit=False)
            add_on_forms.hotel=getHotel(request)
            add_on_forms.save()
            return redirect("addon_view")
    return render(request, 'addons/add_new_addons.html',context)

@login_required
def edit_new_addon(request,id):
    addon = Addon.objects.get(pk=id)
    add_on_forms = AddonForm(instance=addon)
    context = {'add_on_forms': add_on_forms}
    if request.method == 'POST':
        add_on_forms = AddonForm(request.POST,instance=addon)
        if add_on_forms.is_valid():
            add_on_forms.save()
            return redirect("addon_view")
    return render(request, 'addons/add_new_addons.html',context)