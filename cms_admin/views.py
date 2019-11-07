from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, TemplateView
from payments.models import Payment, AccountTransaction, WalletTransaction, CashTransaction


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "cms_admin/dashboard.html"


class PaymentListView(LoginRequiredMixin, ListView):

    model = Payment
    template_name = "cms_admin/payments/list.html"
    context_object_name = "payments"
    ordering = "-id"


class PaymentDetailView(LoginRequiredMixin, DetailView):

    template_name = "cms_admin/payments/detail.html"
    model = Payment
    context_object_name = "payment"
    slug_field = "id"
    slug_url_kwarg = "id"


class AccountTransactionListView(LoginRequiredMixin, ListView):

    model = AccountTransaction
    template_name = "cms_admin/payments/account_transactions/list.html"
    context_object_name = "account_transactions"
    ordering = "-id"


class AccountTransactionDetailView(LoginRequiredMixin, DetailView):

    model = AccountTransaction
    context_object_name = "account_transaction"
    template_name = "cms_admin/payments/account_transactions/detail.html"
    slug_field = "id"
    slug_url_kwarg = "id"
