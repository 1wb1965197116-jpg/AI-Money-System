# payments.py
import stripe
import os

stripe.api_key = os.getenv("STRIPE_API_KEY")

def create_checkout_session(amount: int, currency="usd") -> str:
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data":{
                "currency": currency,
                "product_data": {"name": "AI App"},
                "unit_amount": amount
            },
            "quantity": 1
        }],
        mode="payment",
        success_url="https://your-app.com/success",
        cancel_url="https://your-app.com/cancel"
    )
    return session.url
