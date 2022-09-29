import requests
from test_app.google import service, spreadsheet_id
from test_app import sess, sched
from test_app.database.models import OrderData


def periodic_task():
    # получаем курс на сегодня
    data_usd = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    usd_val = round(data_usd['Valute']['USD']['Value'], 2)
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
    for i in range(1, len(data)):
        if sess.query(OrderData).filter(OrderData.id == data[i][0]).first():
            if sess.query(OrderData).filter(OrderData.order == data[i][1], OrderData.price == data[i][2]).first():
                continue
            else:                    
                price_rus = int(data[i][2]) * usd_val
                entry_id = data[i].pop(0)
                data[i].insert(2, str(float(f'{price_rus:.2f}')))
                sess.query(OrderData).filter(OrderData.id == entry_id).update({m_update[k]: v for k, v in enumerate(data[i])})
                sess.commit()
        else:
            price_rus = int(data[i][2]) * usd_val
            data[i].insert(3, str(float(f'{price_rus:.2f}')))
            sess.add(OrderData(**{mapping[k]: v for k, v in enumerate(data[i])}))
            sess.commit()
