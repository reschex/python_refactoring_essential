from dataclasses import dataclass
import requests


@dataclass(frozen=True)
class Order:
    orderId: int
    shippingType: str
    weightKg: float
    distanceKm: float
    fragile: bool


class GenericOrderGetter:
    @staticmethod
    def get_order(order_id):
        pass


class GetOrderFromUrl(GenericOrderGetter):
    @staticmethod
    def get_order(order_id):
        url = f"https://codemanship.co.uk/api/orders.php?orderId={order_id}"

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        order = Order(
            orderId=data["orderId"],
            shippingType=data["shippingType"],
            weightKg=data["weightKg"],
            distanceKm=data["distanceKm"],
            fragile=data["fragile"]
        )

        return order


class TestOrderGetter(GenericOrderGetter):
    @staticmethod
    def get_order(order_id):

        match order_id:
            case 1001:
                return Order(orderId=1001, shippingType="STANDARD", weightKg=5, distanceKm=120, fragile=False)
            case 1002:
                return Order(orderId=1002, shippingType="EXPRESS", weightKg=8.5, distanceKm=300, fragile=True)
            case 1003:
                return Order(orderId=1003, shippingType="OVERNIGHT", weightKg=2, distanceKm=50, fragile=False)


class ShippingCalculator:

    def __init__(self, order_getter=None):
        if not order_getter:
            order_getter = GetOrderFromUrl
        self.order_getter = order_getter

    def calculate_shipping(self, order_id: int) -> float:

        try:
            order = self.order_getter.get_order(order_id)

            if order.shippingType == "STANDARD":
                return order.weightKg * 0.5

            elif order.shippingType == "EXPRESS":
                return order.weightKg * 0.8 + order.distanceKm * 0.1

            elif order.shippingType == "OVERNIGHT":
                return order.weightKg * 1.2 + 25

            else:
                raise RuntimeError(f"Unknown shipping type: {order.shippingType}")

        except Exception as e:
            print(e)
            return -1.0


