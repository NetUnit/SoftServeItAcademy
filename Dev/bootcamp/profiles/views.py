from django.shortcuts import render
from accounts.forms import CustomUserCreationForm
from django.contrib.admin.views.decorators import staff_member_required

# application for custom managing profiles
# @staff_member_required(login_url=f'/accounts/check-user-auth/')
# def profile_list_view(request, *args, **kwargs):
#     try:
#         profiles = CustomUser.get_all_users()
#         context = {'profiles': profiles}
#         return render(request, 'accounts/list_main.html', context)
#         # return HttpResponse(f'<h2> {profiles}  <h2>')
#     except ValidationError as error:
#         # change this afterwards to general template
#         # put error as general name of eror in a template for all views
#         return render(request, 'accounts/update_faied.html')
