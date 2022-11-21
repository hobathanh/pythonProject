from .extension import db


class Customers(db.Model):
    CustomersID = db.Column(db.Integer, primary_key=True)
    CustomersName = db.Column(db.String(100), nullable=False)
    ContactName = db.Column(db.String(50))
    Address = db.Column(db.String(100))
    City = db.Column(db.String(50))
    PostalCode = db.Column(db.String(50))
    Country = db.Column(db.String(50))

    def __init__(self, CustomersName, ContactName, Address, City, PostalCode, Country ):
        self.CustomersName = CustomersName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country


class Products(db.Model):
    ProductID = db.Column(db.Integer, primary_key=True)
    ProductName = db.Column(db.String(50), nullable=False)
    SupplierID = db.Column(db.Integer, db.ForeignKey('suppliers.SupplierID'))
    CategoryID = db.Column(db.Integer, db.ForeignKey('categories.CategoryID'))
    Unit = db.Column(db.String(100))
    Price = db.Column(db.Integer)

    def __init__(self, ProductName, SupplierID, CategoryID, Unit, Price ):
        self.ProductName = ProductName
        self.SupplierID = SupplierID
        self.CategoryID = CategoryID
        self.Unit = Unit
        self.Price = Price


class Suppliers(db.Model):
    SupplierID = db.Column(db.Integer, primary_key=True)
    SupplierName = db.Column(db.String(100), nullable=False)
    ContactName = db.Column(db.String(50))
    Address = db.Column(db.String(100))
    City = db.Column(db.String(50))
    PostalCode = db.Column(db.String(50))
    Country = db.Column(db.String(50))
    Phone = db.Column(db.String(20))

    def __init__(self, SupplierName, ContactName, Address, City, PostalCode, Country, Phone ):
        self.SupplierName = SupplierName
        self.ContactName = ContactName
        self.Address = Address
        self.City = City
        self.PostalCode = PostalCode
        self.Country = Country
        self.Phone = Phone


class Categories(db.Model):
    CategoryID = db.Column(db.Integer, primary_key=True)
    CategoryName = db.Column(db.String(100), nullable=False)

    def __init__(self, CategoryName):
        self.CategoryName = CategoryName


class Orders(db.Model):
    OrderID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer, db.ForeignKey("customers.CustomersID"))
    EmployeeID = db.Column(db.Integer, db.ForeignKey("employees.EmployeeID"))
    OrderDate = db.Column(db.Date)
    ShipperID = db.Column(db.Integer, db.ForeignKey("shippers.ShipperID"))

    def __init__(self, CustomerID, EmployeeID, OrderDate, ShipperID):
        self.CustomerID = CustomerID
        self.EmployeeID = EmployeeID
        self.OrderDate = OrderDate
        self.ShipperID = ShipperID

class OrderDetails(db.Model):
    OrderDetailID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer, db.ForeignKey("orders.OrderID"))
    ProductID = db.Column(db.Integer, db.ForeignKey("products.ProductID"))
    Quantity = db.Column(db.Integer)

    def __init__(self, OrderID, ProductID, Quantity):
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.Quantity = Quantity



class Employees(db.Model):
    EmployeeID = db.Column(db.Integer, primary_key=True)
    LastName = db.Column(db.String(10), nullable=False)
    FirstName = db.Column(db.String(10),nullable= False)
    BirthDate = db.Column(db.Date)
    Photo = db.Column(db.String(50))
    Notes = db.Column(db.String(500))

    def __init__(self, LastName, FirstName, BirthDate, Photo, Notes):
        self.LastName = LastName
        self.FirstName = FirstName
        self.BirthDate = BirthDate
        self.Photo = Photo
        self.Notes = Notes


class Shippers(db.Model):
    ShipperID = db.Column(db.Integer, primary_key=True)
    ShipperName = db.Column(db.String(100), nullable=False)
    Phone = db.Column(db.String(20))

    def __init__(self, ShipperName, Phone):
        self.ShipperName = ShipperName
        self.Phone = Phone
