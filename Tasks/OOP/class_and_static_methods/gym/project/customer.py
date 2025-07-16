from project.id_mixin import IDMixin

class Customer(IDMixin):
    # id = 1
    def __init__(self, name: str, address: str, email: str):
        self.name = name
        self.address = address
        self.email = email
        # self.id = Customer.id
        self.id = self.get_next_id()
        # Customer.id += 1
        self.increment_id()

    # @staticmethod
    # def get_next_id():
    #     return Customer.id

    # @classmethod
    # def get_next_id(cls):
    #     return cls.id
    #
    # @classmethod
    # def increment_id(cls):
    #     cls.id += 1

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"