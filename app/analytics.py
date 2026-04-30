import pandas as pd

def load_data():
    return pd.read_csv("data/trades.csv")


def compute_pnl(df):
    return df["Gaurav"].sum(), df["Rishika"].sum()


def win_loss_days(df):
    win_days = (df["Total"] > 0).sum()
    loss_days = (df["Total"] < 0).sum()
    return win_days, loss_days


def best_trader(g, r):
    if g > r:
        return "Gaurav"
    elif r > g:
        return "Rishika"
    else:
        return "Tie"


def run_report():
    df = load_data()

    g, r = compute_pnl(df)
    win, loss = win_loss_days(df)
    winner = best_trader(g, r)

    print("\n📊 TRADING REPORT")
    print("----------------------")
    print("Gaurav P&L :", g)
    print("Rishika P&L:", r)
    print("Winning Days:", win)
    print("Losing Days :", loss)
    print("Best Trader :", winner)


if __name__ == "__main__":
    run_report()