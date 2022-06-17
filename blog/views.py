from django.shortcuts import render, get_object_or_404

from .models import Post
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.


def home(request):
    context = {'posts': Post.objects.all()}

    return render(request, "blog/home.html", context)


class PostListView(ListView):
    model = Post
    template_name = "blog/home.html"
    context_object_name = 'posts'
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = "blog/user_posts.html"
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        """
        to modify the queryset that list view returns
        :return:
        """
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        # to get username from url -> self.kwargs.get('username')
        # filter post by the user we got, then order it.
        return Post.objects.filter(author_id=user).order_by('-data_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # override this method  : to get the user who publish the post.
        form.instance.author_id = self.request.user
        return super().form_valid(form)  # just form valid method

    # def get_success_url(self):
    # if we want to redirect to home after add new post
    #     return reverse('blog-home')


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        # override this method  : to get the user who publish the post.
        form.instance.author_id = self.request.user
        return super().form_valid(form)  # just form valid method

    def test_func(self):
        """
        to restrict update for the logged-in user.
        :return:
        """
        post = self.get_object()
        if post.author_id == self.request.user:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post

    def test_func(self):
        """
        to restrict update for the logged-in user.
        :return:
        """
        post = self.get_object()
        if post.author_id == self.request.user:
            return True
        return False

    def get_success_url(self):
        return reverse('blog-home')


def about(request):
    return render(request, "blog/about.html", {'title': "about"})
