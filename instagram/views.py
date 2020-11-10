from django.http import HttpResponse, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, ArchiveIndexView, YearArchiveView
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

# 함수 기반 뷰 (Function based view)
# 함수 기반 뷰에서 login_required 사용하기
'''
@login_required
def post_list(request):
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
'''

# 클래스 기반 뷰 예시
# 이 경우에는 검색기능은 동작하지 않기 때문에 따로 작성해야하지만, 기본적으로 모델의 전체 레코드를 가져와서 반환처리는 잘 된다.
# post_list = login_required(ListView.as_view(model=Post, paginate_by=10))

# 클래스형뷰에서 login_required 를 쓰려면 이 방법을 추천
#@method_decorator(login_required, name='dispatch')
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 10

post_list = PostListView.as_view()

# /instagram/10
# 여기서 10 을 처리하기 위해서 두 번째 인자에 그 10을 담을 수 있는 매개변수가 들어간다. (pk)
# 이 10이 URL Captured Values 라고 한다\
'''
def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    # 로우가 없으면 DoesNotExist 예외 발생 (500 에러)
    # 그래서 만약 404 에러를 띄워주려면 아래와 같이 해야한다
    #try:
    #    post = Post.objects.get(pk=pk)
    #except Post.DoesNotExist:
    #    raise Http404

    # get_objects_404(모델명, 조회조건) 로 할 때 로우가 없으면 404 에러
    post = get_object_or_404(Post, pk=pk)

    return render(request, 'instagram/post_detail.html', {
        'post': post
    })
'''

# 클래스 기반 뷰 (DetailView)
#post_detail = DetailView.as_view(model=Post)

# DetailView 를 상속받아서 커스텀도 가능함
class PostDetailView(DetailView):
    model = Post

    # get_queryset() 오버라이딩
    def get_queryset(self):
        qs = super().get_queryset()
        if not self.request.user.is_authenticated:
            qs = qs.filter(is_public=True)    
        return qs

post_detail = PostDetailView.as_view(model=Post)

# 타입 힌트
# def 함수명(인자: 타입, 인자: 타입 ...) -> 반환타입
def post_detail_hint(request: HttpRequest, pk: int) -> HttpResponse:
    # HttpRequest, HttpResponse  예시 코드
    # 주요 request 속성
    '''
    request.method # 'GET', 'POST', etc
    request.META
    request.GET
    request.POST
    request.FILES
    request.body
    등등...
    '''

    content = '''
        <html></html>
        여기에 문자열, 이미지, 각종 파일 등의 컨텐츠 작성
    '''

    response = HttpResponse(content)
    response.write(content) # response -> file-like object
    response['Custom-Header'] = 'Custom Header Value'
    return response

#def archives_year(request, year):
#    return HttpResponse(f"{year}년 archives")

# ArchiveIndexView 이용
post_archive = ArchiveIndexView.as_view(model=Post, date_field='created_at', paginate_by=10)

# YearArchiveView 이용
post_archive_year = YearArchiveView.as_view(model=Post, date_field='created_at', make_object_list=True)