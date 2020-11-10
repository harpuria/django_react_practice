from django.urls import path, re_path, register_converter
from . import views

app_name = 'instagram' # namespace 역할

# Custom Path Converter 작성
class YearConverter:
    regex = r"20\d{2}" # 20으로 시작하는 년도
    
    def to_python(self, value):
        return int(value)
    
    def to_url(self, value):
        return str(value)

# Custom Path Converter 등록
register_converter(YearConverter, 'year')

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>', views.post_detail), # pk 는 int 값으로 전달
    #path('archives/<int:year>', views.archives_year),
    #re_path(r'archives/(?P<year>20\d{2})', views.archives_year), # r'URL_PATTERN_STR/(?P<URL_PATTERN_STR>정규표현식)
    #path('archives/<year:year>', views.archives_year), # Custom Path Converter 이용
    #re_path(r'(?P<pk>\d+)/$'), views.post_detail) 정규표현식 이용. 이경우는 문자열로 전달
    path('archive/', views.post_archive),
    path('archive/<year:year>', views.post_archive_year),
    #path('archive/<year:year>/<month:month>', views.post_archive_month),
    #path('archive/<year:year>/<month:month>/<day:day>', views.post_archive_day),
]