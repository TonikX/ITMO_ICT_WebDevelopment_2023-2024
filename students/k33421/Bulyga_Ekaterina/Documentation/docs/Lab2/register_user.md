<h1>Представление register_user</h1>
<p>Функция для регистрации пользователя в системе.</p>
<pre>
<code>
def register_user(request):
    try:
        user = request.user
        if str(user) != 'AnonymousUser':
            return redirect('/')
    except:
        pass
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            user = authenticate(username=username, password=password)
            User.objects.create(username=username, name=name, email=email)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
        return render(request, 'conferences/register.html', {'form': form})

    return render(request, 'conferences/register.html', {'form': form})
</code>
</pre>