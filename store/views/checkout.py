from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings

from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View

from store.models.product import Product
from store.models.orders import Order
from store.models.productkeys import Productkeys
from django.db.models import Q

class CheckOut(View):
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        #print(address, phone, customer, cart, products)

        emailfrom = settings.EMAIL_HOST_USER
        subject ='Thank you for placing order'
        message ='Here is your Product: '

        productlist=[]
        #Productkeys.objects.all().update (used=False)
        for product in products:
            message1 = ' '
            message2 = ' '
            message1=message1+product.name+' - '
            quantity = int(cart.get(str(product.id)))
            #print(message1)
            #print(product.id)
            #print(quantity)
            #print(Productkeys.objects.filter(products__id=product.id)[:quantity])
            objectproductkeys=Productkeys.objects.filter(products__id=product.id )
            #objectproductkeys=Productkeys.objects.filter(Q(products__id=product.id) & Q(Productkeys.objects.filter(used=False)))[:quantity]
            #objectproductkeys=Productkeys.objects.filter(products__id=product.id).exclude(Productkeys.objects.filter(used=True))[:quantity]

            quantitycount=0

            for objectproductkey in objectproductkeys:
                if(objectproductkey.used==False):

                    objectproductkey.used=True
                    objectproductkey.save()
                    quantitycount=quantitycount+1

                    if len(objectproductkeys)!=1:
                        message2=message2+str(objectproductkey.productkey)+' ; '
                    else :
                        message2 = message2 + str(objectproductkey.productkey)
                    if(quantitycount==quantity):
                        break

                    #print(message2)
                #if len(products)!=1:
                   # message2=message2+' , '

            #print(message1+message2)
            productlist.append(message1+message2)
        print(productlist)












        recipentemail=Customer.objects.filter(id=customer)[0].email
        #print(Customer.objects.filter(id=customer)[0].email)
        finalmessage = ' '
        for itemsx in productlist:
            finalmessage = finalmessage+itemsx+', '
        recipent = [recipentemail, ]
        send_mail(subject,message+finalmessage, emailfrom, recipent)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')

