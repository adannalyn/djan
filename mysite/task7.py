from djan.models import Product

#  I. Insert a new record into the Product Model
Product1=Product(productname="school items", price=20)
#  ii. Get all the records in the Product table 
Product.objects.all()
#  iii. Filter products by their name 
Product.objects.filter(productname="school items")
#  iv. Get a single record from the product table 
Product_Record = Product.objects.get(productname="school items")
Product_Record
#  v. Change a product price
Product1.price=200
x = Product1
x.price