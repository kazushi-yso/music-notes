
from django.urls import path
from .views import MemoCreateView
from .views import MemoDetailView
from .views import MemoListView
from .views import MemoDeleteView
from .views import MemoEditView
from .views import index

urlpatterns = [
    path('create/', MemoCreateView.as_view(), name="create_memo"),
    path("memos/", MemoListView.as_view(), name="memo_list"),
    path("memo/<int:memo_id>/view/", MemoDetailView.as_view(), name="memo_detail_view"),
    path("memo/<int:memo_id>/delete/", MemoDeleteView.as_view(), name="memo_delete"),
    path("memo/<int:memo_id>/edit/", MemoEditView.as_view(), name="memo_edit"),
    path('', index, name="index")
    ]