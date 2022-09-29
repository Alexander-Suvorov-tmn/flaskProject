from . import ma


class DataTestSchema(ma.Schema):
    class Meta:
        fields = ("id", "order", "price", "price_rus", "delivery_time")


data_test_schema = DataTestSchema()
tests_schema = DataTestSchema(many=True)