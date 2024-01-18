# In your views.py file
from rest_framework.decorators import api_view, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .models import Transactions
from datetime import datetime,date
from .serializer import TransactionsSerializer
from rest_framework.views import APIView

@api_view(['POST'])
@parser_classes([MultiPartParser, FormParser, JSONParser])
def process_transaction_data(request):
    mutable_data = request.data.copy()

    data = dict(mutable_data)

    batch_no = f"{data['farmer_code']}-{datetime.now().strftime('%Y%m%d%H%M%S')}"


    season = datetime.now().year

    data['created_at'] = datetime.now().date()

    data['batch_no'] = batch_no
    data['season'] = season


    try:
        transaction = Transactions.objects.create(**data)
        return Response({"message": "Transaction data successfully processed.", "batch_no": batch_no, "season": season,"success":True}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({"error": f"Error processing transaction data: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class TransactionsListView(APIView):
    def get(self, request):
        transactions = Transactions.objects.all()
        serializer = TransactionsSerializer(transactions, many=True)
        return Response(serializer.data)
    
# get financial report
    
@api_view(['POST'])
def get_financial_report(request):
    chosen_date_str = request.data.get('date', '')

    # Set the default date to today if no date is provided
    if not chosen_date_str:
        chosen_date = date.today()
    else:
        try:
            chosen_date = datetime.strptime(chosen_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response({'error': 'Invalid date format. Please provide a valid date in the format YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

    transactions = Transactions.objects.filter(purchase_date=chosen_date).order_by('-purchase_date')
    serializer = TransactionsSerializer(transactions, many=True)

    return Response(serializer.data)

# Get Direct Purchase Report

@api_view(['POST'])
def get_dpr(request):
    start_date_str = request.data.get('start_date', '')
    end_date_str = request.data.get('end_date', '')

    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    except ValueError:
        return Response({'error': 'Invalid date format. Please provide valid dates in the format YYYY-MM-DD.'}, status=status.HTTP_400_BAD_REQUEST)

    transactions = Transactions.objects.filter(purchase_date__range=[start_date, end_date]).order_by('-purchase_date')
    serializer = TransactionsSerializer(transactions, many=True)

    return Response(serializer.data)
