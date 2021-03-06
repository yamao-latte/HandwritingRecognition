# managerの中でビューのURLの設定などをここに記述する。
# これをプロジェクトのurl.pyにインクルードさせることでURLを反映させる
from django.urls import path
from manager import views
from django.conf.urls import url

app_name = 'manager'

urlpatterns = [
    # 書籍
    path('book/', views.book_list, name='book_list'),     # 一覧
    path('book/add/', views.book_edit, name='book_add'),  # 登録
    path('book/mod/<int:book_id>/', views.book_edit, name='book_mod'),  # 修正
    path('book/del/<int:book_id>/', views.book_del, name='book_del'),  # 削除
    path('HandRecognize/', views.HandRecognize.as_view(), name='get'),  # 今回使うページ
    path('predicted/', views.Predicted.as_view(), name='get'),  # 今回使うページ
    # path('HandRecognize/', views.HandRecognize.as_view(), name='post'),  # 今回使うページ
    path('', views.HandRecognize.as_view(), name='get'),  # 今回使うページ
    # url(r'^HandRecognize/', views.HandRecognize.as_view()),
]

