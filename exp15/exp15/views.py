from django.shortcuts import render, redirect

# Handles form submission and sets session data
def login_session_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')

        # Storing session data
        request.session['username'] = username
        request.session['mobile'] = mobile

        return redirect('session_success')
    return render(request, 'login.html')

# Handles form submission and sets cookie data
def login_cookie_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        mobile = request.POST.get('mobile')

        # Storing in cookies (expires in 30 days)
        response = redirect('cookie_success')
        response.set_cookie('username', username, max_age=30*24*60*60)
        response.set_cookie('mobile', mobile, max_age=30*24*60*60)

        return response
    return render(request, 'login.html')

# View for session success
def session_success_view(request):
    username = request.session.get('username')
    mobile = request.session.get('mobile')

    context = {
        'username': username,
        'mobile': mobile,
    }
    return render(request, 'session_success.html', context)

# View for cookie success
def cookie_success_view(request):
    username = request.COOKIES.get('username')
    mobile = request.COOKIES.get('mobile')

    context = {
        'username': username,
        'mobile': mobile,
    }
    return render(request, 'cookie_success.html', context)
