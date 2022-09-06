from django.contrib import messages
from django.shortcuts import redirect, render
from .forms import SignupForm


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "회원가입 환영합니다.")
            return redirect("/")
    else:
        form = SignupForm()
    return render(request, 'accounts/signup_form.html', {
        'form': form,
    })
