from phi.agent import Agent
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq
from dotenv import load_dotenv
from phi.tools.duckduckgo import DuckDuckGo
import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


load_dotenv()


web_agent = Agent(
    name="Web Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources", "Ensure recent data"],
    show_tool_calls=True,
    markdown=True,
)

finance_agent = Agent(
    name="Finance Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True,
                         company_info=True, company_news=True)],
    instructions=["Use tables to display data", "Explain reasoning clearly"],
    show_tool_calls=True,
    markdown=True,
)

agent_team = Agent(
    team=[web_agent, finance_agent],
    instructions=["Always include sources", "Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)


# Track and visualize stock performance
def track_and_visualize_stocks(stock_symbols, period="1y", interval="1d"):
    """
    Tracks the performance of specified stocks and plots historical trends.

    Args:
        stock_symbols (list): List of stock symbols to track (e.g., ["RELIANCE.NS", "TCS.NS"]).
        period (str): Time period for historical data (e.g., "1y", "6mo").
        interval (str): Data interval (e.g., "1d", "1wk").
    """
    print(f"Fetching data for stocks: {', '.join(stock_symbols)}")
    stock_data = {}

    # Fetch historical data using yfinance
    for stock in stock_symbols:
        try:
            ticker = yf.Ticker(stock)
            data = ticker.history(period=period, interval=interval)
            if not data.empty:
                stock_data[stock] = data
                print(f"Successfully fetched data for {stock}.")
            else:
                print(f"No data found for {stock}.")
        except Exception as e:
            print(f"Error fetching data for {stock}: {e}")

    # Plot historical trends
    if stock_data:
        plt.figure(figsize=(10, 6))
        for stock, data in stock_data.items():
            plt.plot(data.index, data["Close"], label=stock)

        plt.title("Stock Performance Over Time")
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.legend()
        plt.grid()
        plt.show()
    else:
        print("No valid data to display.")


finance_agent.print_response(
    "Summarize the top 6 best stocks to buy in India for 2025, including percentage growth predictions.")
track_and_visualize_stocks(stock_symbols=[
                           "RELIANCE.NS", "INFY.NS", "INDHOTEL.NS"], period="2y", interval="1d")
