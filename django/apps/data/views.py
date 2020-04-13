from django.shortcuts import render

# Create your views here.
def data_view(request):
    '''
    query_loan_allocation_models = LoanAllocationModel.objects.all()
    print('here')
    print(query_loan_allocation_models)
    context = {
        'query_loan_allocation_models' : query_loan_allocation_models
    }
    return render(request, 'data.html', context)
    '''
    return render(request, 'data.html', {})