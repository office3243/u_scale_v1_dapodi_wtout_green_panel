from django.conf.urls import url
from . import views

app_name = "cms_admin"

urlpatterns = [
    url(r"^dashboard/$", views.DashboardView.as_view(), name="dashboard"),
    url(r'^payments/list/$', views.PaymentListView.as_view(), name="payments_list"),
    url(r'^payments/detail/(?P<id>[0-9]+)$', views.PaymentDetailView.as_view(), name="payments_detail"),
    url(r'^payments/account_transactions/list/$', views.AccountTransactionListView.as_view(), name="account_transactions_list"),
]
