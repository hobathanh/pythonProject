from .extension import ma


class CustomerSchema(ma.Schema):
    class Meta:
        fields = ('CustomersID', 'CustomersName', 'ContactName', 'Address', 'City','PostalCode','Country')


class ProductSchema(ma.Schema):
    class Meta:
        fields = ('ProductID', 'ProductName', 'SupplierID', 'CategoryID', 'Unit','Price')


class SupplierSchema(ma.Schema):
    class Meta:
        fields = ('SupplierID', 'SupplierName', 'ContactName', 'Address', 'City','PostalCode','Country','Phone')


class CategorySchema(ma.Schema):
    class Meta:
        fields = ('CategoryID', 'CategoryName', 'Description')


class OrderSchema(ma.Schema):
    class Meta:
        fields = ('OrderID', 'CustomerID', 'EmployeeID', 'OrderDate', 'ShipperID')


class OrderDetailSchema(ma.Schema):
    class Meta:
        fields = ('OrderDetailID', 'OrderID', 'ProductID', 'Quantity')


class EmployeeSchema(ma.Schema):
    class Meta:
        fields = ('EmployeeID', 'LastName', 'FirstName', 'BirthDate','Photo', 'Notes')



class ShipperSchema(ma.Schema):
    class Meta:
        fields = ('ShipperID', 'ShipperName', 'Phone')

