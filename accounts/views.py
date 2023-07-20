# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import CustomUser, PasswordResetToken
# from django.contrib.auth import authenticate, login, logout
# from .helpers import send_forgot_password_mail
# import uuid
# from django.urls import reverse
# from django.core.exceptions import ObjectDoesNotExist
#
#
# # Create your views here.
# def register(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         username = request.POST['username']
#         password = request.POST['password']
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         confirm_password = request.POST['confirm_password']
#
#         if CustomUser.objects.filter(email=email).exists():
#             messages.error(request, 'Email is already taken.')
#             return redirect('users:register')
#
#         if CustomUser.objects.filter(username=username).exists():
#             messages.error(request, 'Username is already taken.')
#             return redirect('users:register')
#
#         if password != confirm_password:
#             messages.error(request, 'Passwords do not match.')
#             return redirect('users:register')
#
#         if len(password) < 8:
#             messages.error(request, 'Your password must be more than 8 characters.')
#             return redirect('users:register')
#
#         if not any(char.isupper() for char in password):
#             messages.error(request, 'The password must contain at least 1 uppercase letter (A-Z).')
#             return redirect('users:register')
#
#         if not CustomUser.objects.filter(username=username).exists():
#             user = CustomUser.objects.create_user(email=email, password=password, first_name=first_name,
#                                                   last_name=last_name, username=username)
#             login(request, user)
#
#         messages.success(request, 'Registration successful. You can now log in.')
#         return redirect('users:login')  # Redirect to the desired page after successful registration
#
#     return render(request, 'register.html', {'messages': messages.get_messages(request)})
#
#
# def user_login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         # Authenticate user
#         user = authenticate(request, username=username, password=password)
#
#         if user is not None:
#             login(request, user)
#             messages.success(request, 'Login successful.')
#             return redirect('home')
#         else:
#             messages.error(request, 'Invalid username or password.')
#             return redirect('users:login')
#
#     return render(request, 'login.html')
#
#
# def logout_user(request):
#     logout(request)
#     messages.success(request, 'Logout successful.')
#     return redirect("users:login")
#
#
# def ChangePassword(request, token):
#     context = {}
#
#     try:
#         change_password = PasswordResetToken.objects.filter(token=token).first()
#
#         if change_password is None:
#             messages.error(request, "Invalid or expired token.")
#             return redirect(reverse('users:password_reset', kwargs={'token': token}))
#
#         context['user_id'] = change_password.user.id
#
#         if request.method == 'POST':
#             new_password = request.POST.get('new_password')
#             confirm_password = request.POST.get('confirm_password')
#             user_id = request.POST.get('user_id')
#
#             if user_id is None:
#                 messages.error(request, "No user id found.")
#                 return redirect(reverse('users:password_reset', kwargs={'token': token}))
#
#             if new_password != confirm_password:
#                 messages.error(request, 'Passwords do not match.')
#                 return redirect(reverse('users:password_reset', kwargs={'token': token}))
#
#             try:
#                 user = CustomUser.objects.get(id=user_id)
#                 user.set_password(new_password)
#                 user.save()
#                 change_password.delete()  # Delete the used token
#                 messages.success(request, 'Password changed successfully.')
#                 return redirect('users:login')
#             except ObjectDoesNotExist:
#                 messages.error(request, 'User does not exist.')
#                 return redirect(reverse('users:password_reset', kwargs={'token': token}))
#
#     except Exception as e:
#         print(e)
#
#     return render(request, 'change-password.html', context)
#
#
# def ForgotPassword(request):
#     try:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             if not CustomUser.objects.filter(username=username).exists():
#                 messages.error(request, 'No user found with this username')
#                 return redirect('users:forgot_password')
#             user = CustomUser.objects.get(username=username)
#
#             # Retrieve or create the PasswordResetToken object
#             change_password, created = PasswordResetToken.objects.get_or_create(user=user)
#
#             if created:
#                 # If a new token was created, generate and save the token
#                 token = str(uuid.uuid4())
#                 change_password.token = token
#                 change_password.save()
#             else:
#                 # If an existing token was found, you can choose to handle it differently
#                 token = change_password.token
#
#             send_forgot_password_mail(user.email, token)
#             messages.success(request, 'An email has been sent.')
#             return redirect('users:reset_password')
#
#     except Exception as e:
#         error_message = str(e)
#         print(error_message)
#     return render(request, 'forgot-password.html')
#
#
# def profile(request):
#     return render(request, 'profile.html', {'user': request.user})
#
#
# def edit_profile(request):
#     if request.method == 'POST':
#         # Retrieve form data
#         new_username = request.POST.get('username')
#         new_email = request.POST.get('email')
#         new_first_name = request.POST.get('first_name')
#         new_last_name = request.POST.get('last_name')
#         new_phone = request.POST.get('phone')
#         new_address = request.POST.get('address')
#         new_avatar = request.FILES.get('avatar')
#
#         # Update user's profile if authenticated
#         if request.user.is_authenticated:
#             user = request.user
#             user.username = new_username
#             user.email = new_email
#             user.first_name = new_first_name
#             user.last_name = new_last_name
#             user.phone = new_phone
#             user.address = new_address
#
#             if new_avatar:
#                 user.avatar = new_avatar
#
#             user.save()
#
#             messages.success(request, 'Profile updated successfully.')
#             return redirect('users:profile')
#         else:
#             # Handle anonymous user (optional)
#             return redirect('users:login')  # Replace with your login view URL or name
#
#     return render(request, 'edit_profile.html', {'user': request.user})
