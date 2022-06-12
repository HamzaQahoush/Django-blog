from django.shortcuts import render

from .models import Post
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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


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
