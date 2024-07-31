print("welcome to the restaurant\nHere is the menu")
menu={
    'pizza':100,
    'pasta':80,
    'maggi':50,
    'coffee':90,
    'salad':120
}
for i,j in menu.items():
    print(f"{i}:{j}")
sums=0
order=input("enter your first iteam you want to order\n")
print(f"your order {order} added")
sums=sums+menu[order]
while True:
    re=input("do you want to add something Yes/No")
    if(re=='yes'):
        order=input("enter your order\n")
        print(f"your order {order} added")
        sums=sums+menu[order]
    else:
        break
print(f"your total bill is{sums}")    
print("program finish")