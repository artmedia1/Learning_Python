#2) Let's say your company has a product with this lot number: "037-00901-00027".
#037 is the country code. 00901 is the product code. 00027 is the batch number.
#Create a program to print:
#Country code: _ _ _
#Product code: _ _ _ _ _
#Batch number: _ _ _ _ _



lot_number = "037-00901-00027"

x = lot_number.split("-")

country_code = x[0]
product_code = x[1]
batch_number = x[2]

print("Country code: " + country_code, "Product code: " + product_code, "Batch Number: " + batch_number, sep='\n')
