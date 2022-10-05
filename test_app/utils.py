from pycbrf.toolbox import ExchangeRates, Banks
from test_app.google import service, spreadsheet_id
from test_app import sess, sched
from test_app.database.models import OrderData


def periodic_task():
    # получаем данные из таблицы
    values = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id,
        range='A1:D',
        majorDimension='ROWS'
    ).execute()
    # Создаем запись в БД  + добавляем стоимость в рублях
    data = values['values']
    mapping = ('id', 'order', 'price', 'price_rus', 'delivery_time')
    m_update = ('order', 'price', 'price_rus', 'delivery_time')
    db_data = OrderData.query.all()
    for i in range(1, len(data)):
        # проверяем есть ли такая запись по id
        a = (next((x for x in db_data if x.id == int(data[i][0])), None))
        if a != None:
            # смотрим запись по id менялась или нет
            d = (next((x for x in db_data if x.id == int(data[i][0]) and x.order == int(data[i][1] )and x.price == int(data[i][2])), None))
            if d != None:
                continue
            # усли запись изменилась - обновляем данные в БД
            else:
                # получаем курс на день отгрузки
                rates = ExchangeRates(str(a.delivery_time.date()))
                usd_val = float(rates['USD'].value)
                # делаем расчет и запись в Бд
                price_rus = int(data[i][2]) * usd_val
                entry_id = data[i].pop(0)
                data[i].insert(2, str(float(f'{price_rus:.2f}')))
                sess.query(OrderData).filter(OrderData.id == entry_id).update({m_update[k]: v for k, v in enumerate(data[i])})
                sess.commit()
        # если такой записи нет, создаем запись в БД
        else:            
            rates = ExchangeRates(str(a.delivery_time.date()))
            usd_val = float(rates['USD'].value)
            price_rus = int(data[i][2]) * usd_val
            data[i].insert(3, str(float(f'{price_rus:.2f}')))
            sess.add(OrderData(**{mapping[k]: v for k, v in enumerate(data[i])}))
            sess.commit()

