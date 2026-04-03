import yfinance as yf
from textblob import TextBlob


def fetch_nvda_data():
    data = yf.download("NVDA", period="3mo", interval="1d")
    return data


def simple_sentiment(text: str) -> float:
    return TextBlob(text).sentiment.polarity


def compute_conviction(price_trend: float, sentiment: float):
    score = (price_trend * 0.6) + (sentiment * 0.4)
    scaled = round((score + 1) * 5, 2)  # scale to 0–10

    if scaled >= 6.5:
        decision = "BUY"
    elif scaled <= 3.5:
        decision = "SELL"
    else:
        decision = "HOLD"

    return scaled, decision


def run_nvda_pipeline():
    data = fetch_nvda_data()

    close = data["Close"]
    price_trend = (close.iloc[-1] - close.iloc[0]) / close.iloc[0]

    headline = "NVIDIA continues strong AI growth and demand"
    sentiment = simple_sentiment(headline)

    conviction, decision = compute_conviction(price_trend, sentiment)

    return {
        "ticker": "NVDA",
        "price_trend": float(price_trend),
        "sentiment": sentiment,
        "conviction_score": conviction,
        "decision": decision,
    }


if __name__ == "__main__":
    print(run_nvda_pipeline())
