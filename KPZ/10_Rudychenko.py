import pandas as pd
import matplotlib.pyplot as plt
import random

class Client:
    def __init__(self):
        self.data = []
        self.account_info = {"balance": 10000}

    def get_data(self):
        return self.data

    def get_account(self):
        return self.account_info


class Model:
    def __init__(self, client, model_type="ARIMA"):
        self.client = client
        self.model_type = model_type

    def train(self):
        print("Тренуємо модель:", self.model_type)

    def predict(self, data):
        return random.choice(["BUY", "SELL", "HOLD"])


class Indicators:
    @staticmethod
    def calculate_rsi(data, period=14):
        return random.uniform(30, 70)

    @staticmethod
    def calculate_macd(data):
        return random.uniform(-1, 1)


class Trade:
    def __init__(self, entry_price, stop_loss, take_profit):
        self.entry_price = entry_price
        self.exit_price = None
        self.stop_loss = stop_loss
        self.take_profit = take_profit
        self.pnL = 0

    def calculate_pnL(self):
        if self.exit_price:
            self.pnL = self.exit_price - self.entry_price
        return self.pnL


class Backtester:
    def __init__(self, tp=10, sl=5, data_len=100):
        self.client = Client()
        self.amount = 10000
        self.take_profit_length = tp
        self.stop_loss_length = sl
        self.data_len = data_len
        self.model = Model(client=self.client, model_type="BACKTESTING")
        self.trades = []
        self.take_profits_number = 0
        self.stop_loss_number = 0
        self.balance = self.amount
        print("Створено ARIMA модель для бектестингу")

    def run_backtest(self):
        data = self.client.get_data()
        for index, candle in enumerate(data[100:]):
            if index < 100:
                continue

            rsi_value = Indicators.calculate_rsi(data[index-14:index])
            macd_value = Indicators.calculate_macd(data[index-26:index])
            signal = self.model.predict(data)

            if signal == "BUY" and self.balance >= 100:
                entry_price = data[index]["close"]
                stop_loss = entry_price - self.stop_loss_length
                take_profit = entry_price + self.take_profit_length
                trade = Trade(entry_price, stop_loss, take_profit)
                self.trades.append(trade)
                self.balance -= 100

            for trade in self.trades:
                if data[index]["low"] < trade.stop_loss < data[index]["high"]:
                    trade.exit_price = trade.stop_loss
                    self.stop_loss_number += 1
                    self.balance += trade.calculate_pnL()
                elif data[index]["low"] < trade.take_profit < data[index]["high"]:
                    trade.exit_price = trade.take_profit
                    self.take_profits_number += 1
                    self.balance += trade.calculate_pnL()

    def generate_stats(self):
        trades_count = len(self.trades)
        win_rate = (self.take_profits_number / trades_count) * 100 if trades_count > 0 else 0
        profit_factor = self.balance / self.amount
        pnl = self.balance - self.amount
        print(f"Статистика бектестингу:")
        print(f"Кількість угод: {trades_count}")
        print(f"Win Rate: {win_rate}%")
        print(f"Профіт фактор: {profit_factor}")
        print(f"PnL: {pnl}")
        print(f"Загальний прибуток: {pnl}")
        print(f"Абсолютний прибуток: {pnl}")
        
        balance_history = [self.amount]
        for trade in self.trades:
            balance_history.append(balance_history[-1] + trade.calculate_pnL())
        plt.plot(balance_history)
        plt.xlabel('Кількість угод')
        plt.ylabel('Баланс')
        plt.title('Зміна балансу під час бектестингу')
        plt.show()


backtester = Backtester(tp=10, sl=5)
backtester.run_backtest()
backtester.generate_stats()
