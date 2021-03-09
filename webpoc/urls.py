from .views import logindata, ArticleAPIDetails, GenericAPIView
from django.urls import path
urlpatterns = [
    # path('start/<int:pk>', customer_detail),
    path('login/', logindata ),
    #path('article/', ArticleAPIView.as_view()),
    path('detail/<int:id>', ArticleAPIDetails.as_view()),
    path('generic/article/<int:id>', GenericAPIView.as_view()),
    
]