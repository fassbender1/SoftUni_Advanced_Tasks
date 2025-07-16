from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers: list[Customer] = []
        self.trainers: list[Trainer] = []
        self.equipment: list[Equipment] = []
        self.plans: list[ExercisePlan] = []
        self.subscriptions: list[Subscription] = []

    def add_customer(self, customer: Customer):
        if customer not in self.customers:
            self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer not in self.trainers:
            self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment not in self.equipment:
            self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan not in self.plans:
            self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription not in self.subscriptions:
            self.subscriptions.append(subscription)

    def subscription_info(self, subscription_id: int):
        subscription = next((sub for sub in self.subscriptions if sub.id == subscription_id), None)
        customer = next((cust for cust in self.customers if cust.id == subscription.customer_id), None)
        trainer = next((tr for tr in self.trainers if tr.id == subscription.trainer_id), None)
        plan = next((pl for pl in self.plans if pl.id == subscription.exercise_id), None)
        equipment = next((eq for eq in self.equipment if eq.id == plan.equipment_id), None)

        return f"\n".join([subscription.__repr__(),
                           customer.__repr__(),
                           trainer.__repr__(),
                           equipment.__repr__(),
                           plan.__repr__()])
