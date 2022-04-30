class SalesPerson:
    def __init__(self, employee_id, name):
        self.id = employee_id
        self.name = name
        self.sales = []

    def get_id(self):
        return int(self.id)

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sale):
        self.sales.append(sale)

    def total_sales(self):
        total = 0
        for sale in self.sales:
            total += sale
        return total

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        total = self.total_sales()
        if total >= quota:
            return True
        return False

    def compare_to(self, other):
        if self.total_sales() > other.total_sales():
            return 1
        elif self.total_sales() == other.total_sales():
            return 0
        else:
            return -1

    def __str__(self):
        return '{}-{}: {}'.format(self.id, self.name, self.total_sales())
