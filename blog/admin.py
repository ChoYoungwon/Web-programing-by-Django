from django.contrib import admin
from blog.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # tags 필드를 직접 등록할 수 없어 별도로 tag_list항목을 메소드로 정의해서 등록
    list_display = ('id', 'title', 'modify_dt', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

    # Post 테이블과 Tag 테이블이 M:N 관계이므로,
    # Tag 테이블의 관련 레코드를 한 번의 쿼리로 미리 가져오기 위해 get_queryset()메소드를 오버라이딩
    def get_queryset(self, request):
        # prefetch_related() 메소드를 사용해 쿼리 횟수를 줄여 성능을 높인다.
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())


