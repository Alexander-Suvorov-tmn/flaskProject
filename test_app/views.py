from test_app import sess
from flask_restful import Resource

from test_app.database.models import OrderData



class TestDataView(Resource):
    """
    Отдаем данные на страницу приложения
    """
    def get(self):
        info = sess.query(OrderData).all()
        from test_app.schems import tests_schema
        result = tests_schema.dumps(info)

        return result
