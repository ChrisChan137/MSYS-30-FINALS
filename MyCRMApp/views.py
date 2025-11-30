from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Account, Customer
from collections import deque

CRM = {}
Customer_queue = deque()

def login_user(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pword')

        try:
            account = Account.objects.get(user_name=username)

            if password == account.pass_word:
                request.session['username'] = account.user_name
                return redirect('view_customers')
            else:
                messages.error(request, 'Invalid Login. Wrong password.')
                return redirect('login_user')

        except Account.DoesNotExist:
            messages.error(request, 'Invalid Login. Account does not exist.')
            return redirect('login_user')

    else:
        return render(request, 'MyCRMApp/login_user.html')


def signup_user(request):
    if request.method == "POST":
        username = request.POST.get('uname')
        password = request.POST.get('pword')

        if Account.objects.filter(user_name=username).exists():
            messages.error(request, 'Account already exists. Please select another username.')
            return redirect('signup_user')

        Account.objects.create(user_name=username, pass_word=password)
        messages.success(request, 'Account created successfully.')
        return redirect('login_user')
    else:
        return render(request, 'MyCRMApp/signup_user.html')

def delete_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    account.delete()
    return redirect('login_user')

def manage_account(request, pk):
    account = get_object_or_404(Account, pk=pk)
    return render(request, 'MyCRMApp/manage_account.html', {'account': account})


def change_password(request, pk):
    if request.method == "POST":
        cpassword = request.POST.get('pword')
        npassword1 = request.POST.get('npword1')
        npassword2 = request.POST.get('npword2')

        account = get_object_or_404(Account, pk=pk)

        if account.pass_word != cpassword:
            messages.error(request, 'Password is incorrect, please input the correct password.')
            return redirect('change_password', pk=account.pk)

        if npassword1 != npassword2:
            messages.error(request, "The re-entered password does not match. Please make sure they are the same.")
            return redirect('change_password', pk=account.pk)

        Account.objects.filter(pk=pk).update(pass_word=npassword1)
        return redirect('manage_account', pk=account.pk)

    else:
        account = get_object_or_404(Account, pk=pk)
        return render(request, 'MyCRMApp/change_password.html', {'account': account})


# customer stuff
def view_customers(request):
    customers = Customer.objects.all()

    # get the logged in user's account
    username = request.session.get('username')   # we will store this in login
    account = Account.objects.filter(user_name=username).first()

    return render(request, 'MyCRMApp/view_customers.html', {
        'customers': customers,
        'account': account,
    })


def customer_detail(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    return render(request, 'MyCRMApp/view_detail.html', {
        'customer': customer
    })

def add_customers(request):
    if request.method == "POST":
        customer_id = request.POST.get('customer_id')
        name = request.POST.get('name')
        phone_no = request.POST.get('phone_no')
        address = request.POST.get('address')
        customer_type = request.POST.get('customer_type')
        satisfaction = request.POST.get('satisfaction') or 0

        Customer.objects.create(
            customer_id=customer_id,
            name=name,
            phone_no=phone_no,
            address=address,
            customer_type=customer_type,
            satisfaction=satisfaction,
        )

        messages.success(request, "Customer added successfully.")
        return redirect('view_customers')   # ← inside the IF block

    # ← this line is OUTSIDE the IF (same indent as `if request.method`)
    return render(request, 'MyCRMApp/add_customer.html')

def delete_customers(request, pk):
    Customer.objects.filter(pk=pk).delete()
    return redirect('view_customers')

def get_customers_sorted_by_name(): # Linear Sorting Algo
  return sorted(CRM.values(), key=lambda c: c.name.lower())

def enqueue_customer(Customer):
    if Customer.type == 1:
        Customer_queue.appendleft(Customer)
    elif Customer.type == 2:
      if Customer_queue and Customer_queue[0].rarity == 1:
          Customer_queue.appendleft(Customer)
      else:
          Customer_queue.appendleft(Customer)
    elif Customer.type == 3:
        Customer_queue.append(Customer)
    else:
        print("invalid rarity")

def dequeue_customer():
      if Customer_queue:
        return Customer_queue.popleft()
      else:
        print("Queue empty")
        return None




