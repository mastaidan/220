from sales_person import SalesPerson


class SalesForce:
    def __init__(self):
        self.sales_people = []

    def add_data(self, filename):
        data = open(filename, "r").readlines()
        for line in data:
            line = line.split(",")
            line[2] = line[2].rstrip("\n").lstrip()
            sales = line[2].split()
            person = SalesPerson(line[0], line[1].rstrip())
            for sale in sales:
                person.enter_sale(sale)
            self.sales_people.append(person)

    def quota_report(self, quota):
        report = []
        for person in self.sales_people:
            report.append([person.get_id(), person.get_name(), person.total_sales(), person.met_quota(quota)])
        return report

    def top_seller(self):
        top_seller = [False]
        for person in self.sales_people:
            if person.total_sales() > top_seller[0]:
                top_seller[0] = person
            elif person.total_sales() == top_seller[0]:
                top_seller.append(person)
        return top_seller

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if employee_id == person.get_id():
                return person.get_name()
        return

    def get_sale_frequencies(self):
        sale_freq = {}
        for person in self.sales_people:
            for sale in person.sales:
                sale_freq[sale] = sale_freq.get(sale, 0) + 1
        return sale_freq

