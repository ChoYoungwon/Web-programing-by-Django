# TemplateView : 테이블 처리 없이 단순히 템플릿 렌더링 처리만 하는 뷰
from django.views.generic import ListView, DetailView, TemplateView, FormView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView
from blog.models import Post
from django.conf import settings

from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

# --- ListView
class PostLV(ListView):
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2

# --- DetailView
class PostDV(DetailView):
    model = Post

class PostAV(ArchiveIndexView):
    model = Post
    date_field = 'modify_dt'

class PostYAV(YearArchiveView):
    model = Post
    date_field = 'modify_dt'
    make_object_list = True
    month_format = '%b'  # 월을 영어 약어로 처리

class PostMAV(MonthArchiveView):
    model = Post
    date_field = 'modify_dt'
    month_format = '%b'  # 월을 영어 약어로 처리

class PostDAV(DayArchiveView):
    model = Post
    date_field = 'modify_dt'

class PostTAV(TodayArchiveView):
    model = Post
    date_field = 'modify_dt'

# 태그들에게 가중치를 부여해 태그들의 리스트를 효과적으로 시각화
class TagCloudTV(TemplateView):
    template_name = 'taggit/taggit_cloud.html'

class TaggedObjectLV(ListView):
    template_name = 'taggit/taggit_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(tags__name=self.kwargs.get('tag'))

    # tagging.taggit_post_list.html에 넘겨줄 컨텍스트 변수를 추가하기 위해 해당 메소드를 오버라이딩
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)        # 상위 클래스의 컨텍스트 변수 (변경 전의 컨텍스트 변수를 가져온다.)
        context['tagname'] = self.kwargs['tag']             #  url 패턴에서 넘어오는 값을 self.kwargs['tag']로 추출
        return context                                      # 컨택스트 변수들이 템플릿 파일로 전달

class PostDB(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['disqus_short'] = f"{settings.DISQUS_SHORT_NAME}"
        context['disqus_log'] = f"{settings.DISQUS_LOG}"
        context['disqus_url'] = f"{settings.DISQUS_MY_DOMAIN}{self.object.get_absolute_url()}"
        context['disqus_title'] = f"{self.object.slug}"
        return context

class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name='blog/post_search.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        post_list = Post.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
