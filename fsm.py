from transitions.extensions import GraphMachine
import pymysql

class TocMachine(GraphMachine):
    
    # open database connection
    db = pymysql.connect("localhost","root","shelly7526","chatbot")
    cursor = db.cursor();
    #execute SQL query using execute() method
    cursor.execute("SELECT VERSION()")
    count =0
    
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
    
    def is_going_to_user(self, update):
        text = update.message.text
        return text.lower() != 'hi chunfu'
    
    def is_going_to_start(self, update):
        text = update.message.text
        return text.lower() == 'hi chunfu'
    
    def is_going_to_set(self, update):
        text = update.message.text
        return text.lower() == 'set'
    
    def is_going_to_setMoney(self, update):
        total = update.message.text
        return total.isdigit()
    
    def is_going_to_record(self, update):
        text = update.message.text
        return text.lower() == 'record'
    
    def is_going_to_exin(self, update):
        exin = update.message.text
        if exin.isalpha():
            return True
        else:
            return False
    
    def is_going_to_category(self, update):
        cate = update.message.text
        if cate.isalpha():
            return True
        else:
            return False
    
    def is_going_to_money(self, update):
        cost = update.message.text
        return cost.isdigit()
    
    def is_going_to_date(self, update):
        date = update.message.text
        return date.isdigit()
    
    def is_going_to_check(self, update):
        text = update.message.text
        return text.lower() == 'check'
    
    def on_enter_user(self, update):
        update.message.reply_text("garbage")
    
    def on_enter_start(self, update):
        update.message.reply_text("Hi! I am a spending Tracker bot.I can help you to mange your money.")
        update.message.reply_text("You can ask me to :")
        update.message.reply_text("(1)set your budget - say set")
        update.message.reply_text("(2)record your expense and income - say record")
        update.message.reply_text("(3)check your account - say check")
    
    def on_enter_set(self, update):
        update.message.reply_text("SETING BUDGET!")
        update.message.reply_text("How much is your pocket money?")
    
    def on_enter_setMoney(self, update):
        update.message.reply_text("budget set already!")
        self.go_back(update)
    
    def on_enter_record(self, update):
        update.message.reply_text("RECORDING COSTING!")
        update.message.reply_text("expense or income")
    
    def on_enter_exin(self, update):
        update.message.reply_text("Got it!")
        update.message.reply_text("And What kind of things you buy(category)?")
    
    def on_enter_category(self, update):
        update.message.reply_text("How much??")
    
    def on_enter_money(self, update):
        update.message.reply_text("When did you buy??")
    
    def on_enter_date(self, update):
        update.message.reply_text("already save")
        self.go_back(update)
        
    def on_enter_check(self, update):
        update.message.reply_text("CHECK ACCOUNT")
    
    def on_exit_user(self, update):
        print('go go go ')
    
    def on_exit_start(self, update):
        print('Leaving start')

    
    def on_exit_set(self, update):
        print('Leaving seting')
    
    
    def on_exit_setMoney(self, update):
        print('Leaving setMoney')
    
    
    def on_exit_record(self, update):
        print('Leaving recording')
    
    
    def on_exit_exin(self, update):
        print('Leaving exin')
    
    
    def on_exit_category(self, update):
        print('Leaving category')
    
    
    def on_exit_money(self, update):
        print('Leaving money')
    
    
    def on_exit_date(self, update):
        print('Leaving date')
    
    
    def on_exit_check(self, update):
        print('Leaving checking')

    db.close()
