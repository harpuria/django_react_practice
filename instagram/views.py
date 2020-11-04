from django.shortcuts import render
from .models import Post

# 함수 기반 뷰 (Function based view)
def item_list(request):
    #request.Post
    #request.FILES
    qs = Post.objects.all()
    q = request.GET.get('q', '') # get(가져올 파라미터, 없으면 디폴트로 받을 값)
    
    if q:
        qs = qs.filter(message__icontains=q)
    
    # render(request, 'tempate_path', dict)
    return render(request, 'instagram/post_list.html', {
        'post_list':qs,
        'q':q,
    })
