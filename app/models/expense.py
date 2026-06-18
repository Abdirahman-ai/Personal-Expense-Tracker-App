""""
 Expense class
"""""
class Expense:

    def __init__(self, id, title, category, amount, date, payment_method):
        self.id = id
        self.title = title
        self.category = category
        self.amount = amount
        self.date = date
        self.payment_method = payment_method

    # TODO: getters and setters if needed

    # TODO: toSting method
    def __str__(self):
        return (
            f"ID: {self.id} | "
            f"{self.title} | "
            f"{self.category} | "
            f"${self.amount:.2f} | "
            f"{self.date} | "
            f"{self.payment_method}"
        )

    def __repr__(self):
        return self.__str__()