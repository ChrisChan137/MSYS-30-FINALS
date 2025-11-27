from collections import deque

CRM = {}
Customer_queue = deque()

class Customer():
  def __init__(self, ID, name, email, phone, rarity):
    self.ID = ID
    self.name = name
    self.email = email
    self.phone = phone
    self.rarity = rarity # 1: vip, 2: consistent customer, 3: new customer

  def info(self):
    print(f"AccountID: {str(self.ID)}\nName: {self.name}\nEmail Address: {self.email}\nPhone Number: {self.phone}")

  def update(self, param, value):
    if param == "name":
      self.name = value

    elif param == "email":
      self.email = value

    elif param == "phone":
      self.phone = value

    else:
      print("Invalid Parameter")

  def __repr__(self):
    return f"{self.ID} - {self.name}"


CRM[25001] = Customer(25001, "Jeffrey", "eggshapedjeff@gmail.com", "09837592930", 1)
CRM[25002] = Customer(25002, "Donald", "thebigcheese@gmail.com", "09649385948", 2)
CRM[25003] = Customer(25003, "Bill", "clintandsteel@gmail.com", "09183950356", 3)

def get_customers_sorted_by_name(): # Linear Sorting Algo
  return sorted(CRM.values(), key=lambda c: c.name.lower())

def enqueue_customer(Customer):
    if Customer.rarity == 1:
        Customer_queue.appendleft(Customer)
    elif Customer.rarity == 2:
      if Customer_queue and Customer_queue[0].rarity == 1:
          Customer_queue.appendleft(Customer)
      else:
          Customer_queue.appendleft(Customer)
    elif Customer.rarity == 3:
        Customer_queue.append(Customer)
    else:
        print("invalid rarity")

def dequeue_customer():
      if Customer_queue:
        return Customer_queue.popleft()
      else:
        print("Queue empty")
        return None

#-------------------------------------------------
CRM[25002].info()
CRM[25002].update("email", "homealone2guy@gmail.com")
CRM[25002].info()

print("\nAll customers (dis is unsorted):")
print("\n".join(str(x) for x in CRM.values()))


print("\nCustomers sorted by name:")
sorted_customers = get_customers_sorted_by_name()
for c in sorted_customers:
    print(c)

enqueue_customer(CRM[25001])
enqueue_customer(CRM[25002])
enqueue_customer(CRM[25003])

print(list(Customer_queue))