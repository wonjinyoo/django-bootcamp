from django.shortcuts import render
from AppThird.models import User

# Create your views here.
# Homepage
def index(request):
    return render(request, 'AppThird/index.html')

# Userpage
# Tagging
def users(request):
    user_list = User.objects.order_by('fname')
    user_dict = {'users': user_list}
    return render(request, 'AppThird/users.html', context=user_dict)