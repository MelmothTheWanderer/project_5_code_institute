from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):

    """ A view that renders teh bag contentes page """

    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Get the quantity from the form
    quantity = int(request.POST.get('quantity'))
    # Send them back to the page that they were on once the submission is finished. This is why we put the hidden input that contained the url that the shopper was on: 
    redirect_url = request.POST.get('redirect_url')
    # Sessions are memory that the browser uses to make certain data persistent, until the shopper decides to close their browser, and this is useful so that we can store the contents of their shopping bag while the go from page to page shopping.
    # Here we are checking to see if a variable bag exists, and if it doesn't , then making it equal to an empty dictionary. I think that the second parameter is similar to putting a default value or something like that.
    bag = request.session.get('bag', {

    })

    # Now that we have that place to stuff the contents of the bag, lets go about defining what we want to put in there: 

    # Start by seeing if the item is already in the bag: 
    if item_id in list(bag.keys()):
        #if so then increase it's quantity accordingly:
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity
    #Finally, just chuck this into the session that we created: 
    request.session['bag'] = bag
    # Finally FINALLY we redirect the user back to the url that they came from using the imported redirect method: 
    return redirect(redirect_url)