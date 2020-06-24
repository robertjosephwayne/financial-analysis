# Liquidity Ratios


# Current Ratio = Current Assets / Current Liabilities
def current_ratio(current_assets, current_liabilities):
    """
    Calculates the current ratio.

    Current Ratio = Current Assets / Current Liabilities

    Measures a company's ability to pay off short-term liabilities with current assets.


    """
    return current_assets / current_liabilities


def acid_test_ratio(current_assets, current_liabilities, inventory):
    """
    Acid-test Ratio = (Current Assets – Inventory) / Current Liabilities

    Measures a company's ability to pay off short-term liabilities with quick assets.
    """
    return (current_assets - inventory) / current_liabilities


def cash_ratio(cash_and_equivalents, current_liabilities):
    """
    Cash Ratio = Cash and Cash Equivalents / Current Liabilities

    Measures a company’s ability to pay off short-term liabilities with cash and cash equivalents.
    """
    return cash_and_equivalents / current_liabilities


def operating_cash_flow_ratio(operating_cash_flow, current_liabilities):
    """
    Operating Cash Flow Ratio = Operating Cash Flow / Current Liabilities

    Measures the number of times a company can pay off current liabilities with the
    cash generated in a given period.
    """
    return operating_cash_flow / current_liabilities


# Leverage Financial Ratios
# Measure the amount of capital that comes from debt.


def debt_ratio(total_liabilities, total_assets):
    """
    Debt Ratio = Total Liabilities / Total Assets

    Measures the relative amount of a company’s assets that are provided from debt.
    """
    return total_liabilities / total_assets


def debt_to_equity_ratio(total_liabilities, total_equity):
    """
    Debt to Equity Ratio = Total Liabilities / Total Shareholders' Equity

    Calculates the weight of total debt and financial liabilities against shareholders’ equity.
    """
    return total_liabilities / total_equity


def interest_coverage_ratio(operating_income, interest_expense):
    """
    Interest Coverage Ratio = Operating Income / Interest Expense

    Measures how easily a company can pay its interest expenses.
    """
    return operating_income / interest_expense


def debt_service_coverage_ratio(operating_income, debt_service):
    """
    Debt Service Coverage Ratio = Operating Income / Total Debt Service

    Measures how easily a company can pay its debt obligations.
    """
    return operating_income / debt_service


# Efficiency Ratios
# Measure how well a company is utilizing its assets and resources.


def asset_turnover_ratio(net_sales, total_assets):
    """
    Asset Turnover Ratio = Net Sales / Total Assets

    Measures a company’s ability to generate sales from assets.
    """
    return net_sales / total_assets


def inventory_turnover_ratio(cogs, average_inventory):
    """
    Inventory Turnover Ratio = Cost of Goods Sold / Average Inventory

    Measures how many times a company’s inventory is sold and replaced over a given period.
    """
    return cogs / average_inventory


def ar_turnover_ratio(net_credit_sales, average_ar):
    """
    Accounts Receivable Turnover Ratio = Net Credit Sales / Average Accounts Receivable

    Measures how many times a company can turn receivables into cash over a given period.
    """
    return net_credit_sales / average_ar


def dsi_ratio(inventory_turnover_ratio, period=365):
    """
    Days Sales in Inventory Ratio (DSI) = 365 days / Inventory Turnover Ratio

    Measures the average number of days that a company holds on to inventory before selling it to
    customers.
    """
    return period / inventory_turnover_ratio


# Profitability Ratios
# Measure a company’s ability to generate income


def gross_margin(gross_profit, net_sales):
    """
    Gross Margin Ratio = Gross Profit / Net Sales

    Measures how much profit a company makes after paying its cost of goods sold.
    """
    return gross_profit / net_sales


def operating_margin(operating_income, net_sales):
    """
    Operating Margin Ratio = Operating Income / Net sales

    Measures how much profit a company makes after paying its operating expenses.
    """
    return operating_income / net_sales


def roa(net_income, total_assets):
    """
    Return on Assets Ratio = Net Income / Total Assets

    Measures how efficiently a company is using its assets to generate profit.
    """
    return net_income / total_assets


def roe(net_income, total_equity):
    """
    Return on Equity Ratio = Net Income / Total Shareholders' Equity

    Measures how efficiently a company is using its equity to generate profit.
    """
    return net_income / total_equity


# Market Value Ratios

# Used to evaluate the share price of a company’s stock.


def book_value_per_share(total_equity, shares_outstanding):
    """
    Book Value per Share Ratio = Total Shareholders' Equity / Total Shares Outstanding

    Calculates the per-share value of a company based on equity available to shareholders.
    """
    return total_equity / shares_outstanding


def dividend_yield(dividend_per_share, market_price):
    """
    Dividend Yield Ratio = Dividend per Share / Market Price per Share

    Measures the amount of dividends attributed to shareholders relative
    to the market value per share.
    """
    return dividend_per_share / market_price


def eps(net_income, preferred_dividends, shares_outstanding):
    """
    Earnings per Share Ratio (EPS) = (Net Income - Preferred Dividends) / Total Shares Outstanding

    Measures the amount of net income earned for each share outstanding.
    """
    return (net_income - preferred_dividends) / shares_outstanding


def pe(market_price, eps):
    """
    Price-Earnings Ratio = Market Price per Share / Earnings per Share

    Compares a company’s share price to its earnings per share.
    """
    return market_price / eps
