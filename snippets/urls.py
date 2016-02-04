# from django.conf.urls import url, include
# from rest_framework.urlpatterns import format_suffix_patterns
# from snippets import views

# # API endpoints
# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^marcas/$',
#         views.MarcaList.as_view(),
#         name='marca-list'),
#     url(r'^marcas/(?P<pk>[0-9]+)/$',
#         views.MarcaDetail.as_view(),
#         name='marca-detail')
# ])

# # Login and logout views for the browsable API
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]