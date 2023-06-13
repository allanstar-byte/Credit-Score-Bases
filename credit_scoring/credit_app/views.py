# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from .models import CreditScoreModel

def predict_credit_score(request):
    if request.method == 'POST':
        # Get the input data from the request
        data = request.POST
        
        # Create a CreditScoreModel instance and set the input data
        model = CreditScoreModel()
        model.feature1 = data.get('feature1')
        model.feature2 = data.get('feature2')
        # Set other features as needed

        # Call the predict_credit_score() method to get the credit score prediction
        credit_score = model.predict_credit_score()

        # Return the prediction as a JSON response
        return JsonResponse({'credit_score': credit_score})

    return render(request, 'predict.html')
