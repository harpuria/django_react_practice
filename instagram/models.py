from django.db import models
from django.conf import settings

# 유저
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # auth.Models 에 있는 유저 모델의 키를 외래키로 가져올 경우
    message = models.TextField()
    photo = models.ImageField(blank=True) # ImageField 를 사용하려면 pillow 설치해야함. upload_to 옵션에는 특정 경로에 파일을 저장할 수 있게 된다 (ex:instagram/post 로 정하면 MEDIA_ROOT/instagram/post 안에 저장됨)
    tag_set = models.ManyToManyField('Tag', blank=True) # 포스트에 태그가 없을 수도 있기 때문에 blank 는 True 로 두는 것이 좋음!
    is_public = models.BooleanField(default=False, verbose_name='공개여부')
    created_at = models.DateTimeField(auto_now_add=True) # 최초에만 입력
    updated_at = models.DateTimeField(auto_now=True) # 갱신될때마다 변경됨

    # java 에서 toString 과 유사
    # 반환값이 admin 에서 보여지게 된다.
    def __str__(self):
        #return f"Custom Post object({self.id})"
        return self.message

    # 모델의 메타 클래스 (쿼리셋을 불러올 때 무조건 아래의 내용을 토대로 쿼리가 수행된다)
    class Meta:
        ordering = ['-id'] # order_by 를 id 로 내림차순 정렬

# 유저(1) : 코멘트(N)
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) # 모델의 이름은 문자열 'Post' 로 써도 되며, 다른 앱의 모델을 지정할 수도 있다. ex) '앱이름.모델이름' post_id 라는 필드로 생성됨
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    #post_set = models.ManyToManyField(Post, blank=True) 이렇게 해도 되지만 권장하지 않음.
    
    def __str__(self):
        return self.name
