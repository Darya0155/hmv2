from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required


# Create your views here.
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "user/signup.html", {
        "form": form
    })



def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def change_password(request):
    if request.method == "POST":
        old_password = request.POST.get("old_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        user = request.user

        # Check old password
        if not user.check_password(old_password):
            return render(request, "user/change_password.html", {
                "error": "Old password is incorrect"
            })

        # Check new passwords match
        if new_password != confirm_password:
            return render(request, "user/change_password.html", {
                "error": "New passwords do not match"
            })

        # Change password
        user.set_password(new_password)
        user.save()

        # Keep user logged in
        update_session_auth_hash(request, user)

        return redirect("home")

    return render(request, "user/change_password.html")