from django.contrib import admin
from .models import Post, Comment, Tag
from django.utils.safestring import mark_safe

'''
# 등록법 1
admin.site.register(Post)

# 등록법 2
class PostAdmin(admin.ModelAdmin):
    pass
admin.site.register(Post, PostAdmin)
'''

# 등록법 3 (장식자 사용 권장!)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # 리스트 안에 모델의 필드를 넣어주면 됨. pk 는 기본키. (id 를 넣어줘도 됨)
    # 리스트에는 함수를 넣어서 그 결과를 어드민에 보여줄 수도 있다. (photo_tag, message_length)
    # 이 함수는 models.py 에서 만들어도 되고, admin.py 에서 만들어도 된다.
    list_display = ['pk', 'photo_tag', 'message', 'is_public', 'created_at', 'updated_at', 'message_length', 'tag']
    # 특정 필드에 링크 걸기
    list_display_links = ['message']
    # 검색 대상 필드 지정
    search_fields = ['message']
    # 필터 지정 (어드민 우측에 나옴)
    list_filter = ['created_at', 'is_public']

    # self, 모델명 으로 인자를 넣으면 모델명쪽에는 장고에서 자동으로 Post 모델 객체를 넣어준다.
    def message_length(self, post):
        return len(post.message)

    def photo_tag(self, post):
        if post.photo:
            return mark_safe(f'<img src="{post.photo.url}"/>')
        return None

    def tag(self, post):
        qs = Post.objects.all().filter(id=post.id).values('tag_set__name')
        str_tag = ""
        for i in qs:
            str_tag += i['tag_set__name'] + " "
        return str_tag
        #return Tag.objects.all().filter('post_id'=post.id)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

# 기억해두자
# Post.objects.all().filter(id=2).values('tag_set__name')