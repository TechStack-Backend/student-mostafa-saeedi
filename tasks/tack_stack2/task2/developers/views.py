from django.shortcuts import render
def home_page(request):
    return render(request,'developers/home_page.html' )
def developer_list(request):
    context = {'developers': DEVELOPERS}
    return render(request, 'developers/developers_list.html', context)
def developer_cv(request, username):
    developer = None
    for dev in DEVELOPERS:
        if dev['username'] == username:
            developer = dev
            break
        if developer:
            context = {'developer': developer}
            return render(request, 'developers/developer_cv.html', context)
        else:
            return render(request, 'developers/developer_not_found.html')
DEVELOPERS = [
    {
        'first_name': 'Mostafa',
        'last_name': 'Saeedi',
        'username': 'M0S1',
        'skills': ['Python', 'C', 'C++']
    }
]