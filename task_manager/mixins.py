from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect


class AuthRequiredMessageMixin(LoginRequiredMixin):
    you_are_not = 'Вы не авторизованы! Пожалуйста, выполните вход.'
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.error(request, self.you_are_not)
            # иначе проваливается в IsOwner (не ясно - почему)
            return redirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class IsOwnerMixin(UserPassesTestMixin):
    raise_exception = False

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав \
                       для изменения другого пользователя.')
        return redirect(reverse_lazy('users:users')) 

    def test_func(self):
        target_user = self.get_object()
        return self.request.user == target_user



# class IsOwnerMixin:
#     """Разрешает доступ только владельцу или staff."""
#     def dispatch(self, request, *args, **kwargs):
#         if self.get_object() != request.user and not request.user.is_staff:
#             return HttpResponseForbidden()
#         return super().dispatch(request, *args, **kwargs)

# class UserPostsView(IsOwnerOrStaffMixin, ListView):
#     model = Post
#     template_name = 'users/posts.html'

#     def get_queryset(self):
#         return Post.objects.filter(author=self.request.user)



# from django.views.generic import DetailView
# from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserProfileView(UserPassesTestMixin, DetailView):
#     model = User
#     template_name = 'users/profile.html'
#     context_object_name = 'target_user'  # Имя объекта в шаблоне
#     login_url = '/login/'  # Перенаправление, если проверка не пройдена

#     def test_func(self):
#         # Разрешаем доступ только самому пользователю или staff
#         target_user = self.get_object()  # Получаем пользователя из URL (по pk/slug)
#         return self.request.user == target_user or self.request.user.is_staff

#     # Альтернатива: доступ по username
#     # def get_object(self, queryset=None):
#     #     return User.objects.get(username=self.kwargs['username'])