from django.urls import path,include
from . import views
from cws.views import CwsListView,CwsCreateView
from farmers.views import FileUploadAPIView
from transactions.views import *



urlpatterns=[
    path('farmers/',views.FarmerListView.as_view(),name="get_farmers"),
    path('farmers/create/',views.FarmerCreateView.as_view(),name="create_farmer"),
    path('cws/',CwsListView.as_view(),name="create-cws"),
    path('cws/create/',CwsCreateView.as_view(),name="get-cws"),
    path('uploadfarmers/', FileUploadAPIView.as_view(), name='file-upload-api'),
    path('processtransaction/', process_transaction_data, name='process-transaction'),
    path('gettransactions/', TransactionsListView.as_view(), name='transactions-list'),
    path('getfinancialreport/', get_financial_report, name='get-financialreport'),
    path('getdpr/',get_dpr,name="get-dpr"),
]