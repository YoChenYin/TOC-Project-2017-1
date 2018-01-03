import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '450682559:AAH6O0asktmSgXh-I-aDaQ5RNGZQ9pABWtU'
WEBHOOK_URL = 'https://83b987c1.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'start',
        'set',
        'setMoney',
        'record',
        'exin',
        'category',
        'money',
        'date',
        'check'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'user',
            'conditions': 'is_going_to_user'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'start',
            'conditions': 'is_going_to_start'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'set',
            'conditions': 'is_going_to_set'
        },
        {
            'trigger': 'advance',
            'source': 'set',
            'dest': 'setMoney',
            'conditions': 'is_going_to_setMoney'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'record',
            'conditions': 'is_going_to_record'
        },
        {
            'trigger': 'advance',
            'source': 'record',
            'dest': 'exin',
            'conditions': 'is_going_to_exin'
        },
        {
            'trigger': 'advance',
            'source': 'exin',
            'dest': 'category',
            'conditions': 'is_going_to_category'
        },
        {
            'trigger': 'advance',
            'source': 'category',
            'dest': 'money',
            'conditions': 'is_going_to_money'
        },
        {
            'trigger': 'advance',
            'source': 'money',
            'dest': 'date',
            'conditions': 'is_going_to_date'
        },
        {
            'trigger': 'advance',
            'source': 'start',
            'dest': 'check',
            'conditions': 'is_going_to_check'
        },
        {
            'trigger': 'go_back',
            'source': [
              'setMoney',
              'date'
            ],
          'dest': 'start'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
