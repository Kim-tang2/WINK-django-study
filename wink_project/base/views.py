from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'base/index.html')

def posts(request):
    posts = [
        {
            'headline':'SmartFarm DashBoard in Flutter',
            'sub_headline':'콘캣이라는 회사에서 플러터를 이용해 자동화 농장 제어와 대시보드 기능을 수행하는 모바일 앱을 만들고 있습니다.',
        },
        {
            'headline':'Wink Project - Soldier meal',
            'sub_headline':'김급식을 이은 희대의 명작 군급식의 앱 프론트엔드를 맡고 있습니다. 재밌게 진행하고 있습니다 ^^',
        },
        {
            'headline':'True Love',
            'sub_headline':'정말 제대로 된 트루러브를 하고 있습니다...^^ 부럽죠?',
        },
    ]

    context = {'posts':posts}
    return render(request, 'base/posts.html', context)

def post(request):
    return render(request, 'base/post.html')

def profile(request):
    return render(request, 'base/profile.html')