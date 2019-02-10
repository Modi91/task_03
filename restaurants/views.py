from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = { 
    'my_list':[{
    'restaurant_name': 'Modi',
    'food_type': 'Traditional Food'},

    {'restaurant_name': 'Italy',
    'food_type': 'Italian Food'},

    {'restaurant_name': 'Arabic',
    'food_type': 'Arabian Food'}
    ]
    

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    'my_object': {'restaurant_name': 'Modi',
                  'food_type': 'Traditional Food'
                  }
    }

    
    return render(request, 'detail.html', context)
