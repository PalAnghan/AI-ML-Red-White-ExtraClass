class Product:

    def __init__(self, product_id, name, price):

        self.product_id = product_id
        self.name = name
        self.__price = price

    # get method

    def get_price(self):
        return self.__price

    # set method

    def set_price(self):

        user_id = int(input("Enter your product id: "))

        if user_id == self.product_id:

            print("Your id matched successfully!")

            new_price = float(input("Enter new price: "))

            if new_price > 0:
                self.__price = new_price
                print("Price Updated Successfully!")
            else:
                print("Invalid Price")
        else:
            print("Product ID not matched!")

    def display(self):
        print("\n======== Product Details =======")
        print("Product Id :", self.product_id)
        print("Product Name :", self.name)
        print("Product Price : ₹", self.__price)


# Child class

class Mobile(Product):

    def __init__(self, product_id, name, price, brand, ram, storage):
        super().__init__(product_id, name, price)

        self.brand = brand
        self.ram = ram
        self.storage = storage

    def display(self):

        super().display()

        print("Product Brand :", self.brand)
        print("Product RAM :", self.ram, "GB")
        print("Product Storage :", self.storage, "GB")

    def buy(self):
        print("\nOrder Placed Successfully!")
        print("Thank You for Shopping with Us.")


# Main Program

mobile = Mobile(101, "iPhone 17", 85000, "Apple", 16, 256)
laptop = Mobile(11, "G-15", 75000, "Dell", 16, 512)

while True:

    print("\n========== E-Commerce Menu =========")

    print("1. View Product")
    print("2. Check Price")
    print("3. Update Price")
    print("4. Buy Product")
    print("5. Exit")

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter numbers only!")
        continue

    if choice == 1:

        mobile.display()
        laptop.display()

    elif choice == 2:

        print("Mobile Current Price : ₹", mobile.get_price())
        print("Laptop Current Price : ₹", laptop.get_price())

    elif choice == 3:

        product_id = int(input("Enter Product ID: "))

        if product_id == mobile.product_id:
            mobile.set_price()

        elif product_id == laptop.product_id:
            laptop.set_price()

        else:
            print("Product Not Found!")

    elif choice == 4:

        product_id = int(input("Enter Product ID: "))

        if product_id == mobile.product_id:
            mobile.buy()

        elif product_id == laptop.product_id:
            laptop.buy()

        else:
            print("Product Not Found!")

    elif choice == 5:

        print("Thank You!")
        break

    else:

        print("Invalid Choice")
