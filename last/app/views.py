from django.shortcuts import render
from app.forms import UserForm, UserInfoForm, PostForm, PublishForm
from app.models import Post, UserInfo, Publish
from django.contrib.auth.models import User
from django.shortcuts import get_list_or_404, get_object_or_404
from django.http import Http404
from django.utils import timezone

from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import (TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View)


# Create your views here.

def index(request):
    return render(request, 'index.html')


def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)
        details_form = UserInfoForm(request.POST)

        if user_form.is_valid() and details_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            details = details_form.save(commit=False)
            details.user = user
            details.save()

            registered = True

        else:
            print(user_form.errors, details_form.errors)

    else:
        user_form = UserForm()
        details_form = UserInfoForm()

    return render(request, 'register.html',
                  {'user_form': user_form, 'details_form': details_form, 'registered': registered})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_superuser:

                login(request, user)

                return render(request, 'super_login_page.html', {})

            else:

                login(request, user)
                return render(request, "login_page.html", {})

        else:

            return HttpResponse("Invalid Login Details")

    else:
        return render(request, 'login.html', {})


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def thankYou(request):
    return render(request, 'thankyou.html')


@login_required
def thanks(request):
    return render(request, "thanks.html")


@login_required
def home(request):
    return render(request, "home.html")


class PostListView(ListView):
    context_object_name = "list"
    model = Post

    def get_queryset(self):

        '''try:
            self.userpost_user = UserInfo.objects.prefetch_related('posts').get(userpost_id = self.kwargs.get('id'))

        except User.DoesNotExist:
            raise Http404

        else:
            return self.userpost_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['userpost_user'] = self.userpost_user
        return context

        #user_name = self.request.user.username
        #return Post.objects.get(userpost=user_name)'''

        # user_id = self.request.user.id
        # user_id_check = Post.userpost_id
        # user_check = self.request.user
        #user_recheck = Post.userpost
        # return Post.objects.filter(userpost=user_check)

        # results = Post.objects.filter(pk=self.request.user.id)
        # return results.posts.all()

        #return self.model.objects.filter(userpost=self.request.user)

        #self.userpost = get_object_or_404(Post,pk=id)
        #return Post.objects.filter(userpost=self.userpost)

        #return self.model.objects.filter(userpost=self.kwargs['userpost'])'''

        #return Post.objects.filter(userpost__id=self.request.id)
        return Post.objects.filter(userpost=UserInfo.objects.get(user=self.request.user))


class PostDetailView(DetailView):
    context_object_name = 'post_detail'
    model = Post

    template_name = "post_detail.html"

'''class PostDeleteView(LoginRequiredMixin,DeleteView):

    model = Post
    success_url = reverse_lazy("post_list")

    def get_object(self):
        return self.queryset.get(id=self.kwargs['id'])'''



class CreatePostView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'app/post_list.html'

    form_class=PostForm
    model = Post

    def form_valid(self,form):
        create_post = form.save(commit=False)
        form.userpost=UserInfo.objects.get(user=self.request.user)
        create_post.user=self.request.user
        form.save()
        return super(CreatePostView,self).form_valid(form)


'''def posts_delete_view(request,pk):
    post_del = get_object_or_404(Post,pk=pk)
    com = post_del.userpost.pk
    creator = Post.userpost.user.username

    if request.method == "POST" and request.user.is_authenticated and request.user.username == creator:
        #post_del.delete()
        post_del.delete()
        return HttpResponseRedirect("post_list")

    context = {'post_del': post_del,
               'creator': creator,
               }

    return render(request, 'posts_delete.html', context)'''


class UserPostListView(LoginRequiredMixin, ListView):
    context_object_name = "user_post_list"
    template_name = "app/user_post_list.html"
    model = Publish

    def get_queryset(self):
        return Publish.objects.all()


class UserPostDetailView(LoginRequiredMixin, DetailView):
    context_object_name = "user_post_detail"
    template_name = "app/user_post_detail.html"

    model = Publish


class CreatePublishView(LoginRequiredMixin, CreateView):
    login_url = '/super_login_page/'
    redirect_field_name = 'app/publish_list.html'

    form_class = PublishForm
    model = Publish


class PublishListView(ListView):
    context_object_name = 'publish'
    template_name = 'app/publish_list.html'
    model = Publish

    def get_queryset(self):
        return Publish.objects.all()


class PublishDetailView(DetailView):
    context_object_name = 'publish_detail'
    model = Publish

    template_name = 'app/publish_detail.html'


class SuperPostListView(ListView):
    context_object_name = 'super_post_list'
    template_name = 'app/super_post_list.html'
    model = Post

    def get_queryset(self):
        return Post.objects.all()


class SuperPostDetailView(DetailView):
    context_object_name = "super_post_detail"
    template_name = 'app/super_post_detail.html'

    model = Post
