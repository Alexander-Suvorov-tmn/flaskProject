from test_app import app, api, TestDataView
from test_app.utils import periodic_task
from test_app.telegram_bot import updater



if __name__ == '__main__':
    api.add_resource(TestDataView, '/')
    app.apscheduler.add_job(func=periodic_task, id='periodic_task', trigger='interval', seconds=10)
    updater.start_polling()
    updater.idle()
    app.run(debug=True)
