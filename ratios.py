# Liquidity Ratios


# Current Ratio = Current Assets / Current Liabilities
def current_ratio(current_assets, current_liabilities):
    """Measures a company's ability to pay off short-term liabilities with current assets"""
    return current_assets / current_liabilities


# Acid-test Ratio = (Current Assets – Inventory) / Current Liabilities
def acid_test_ratio(current_assets, current_liabilities, inventory):
    """Measures a company's ability to pay off short-term liabilities with quick assets"""
    return (current_assets - inventory) / current_liabilities


# Cash Ratio = Cash and Cash Equivalents / Current Liabilities
def cash_ratio(cash_and_equivalents, current_liabilities):
    """Measures a company’s ability to pay off short-term liabilities
    with cash and cash equivalents"""
    return cash_and_equivalents / current_liabilities


# Operating Cash Flow Ratio = Operating Cash Flow / Current Liabilities
def operating_cash_flow_ratio(operating_cash_flow, current_liabilities):
    """Measures the number of times a company can pay off current
    liabilities with the cash generated in a given period"""
    return operating_cash_flow / current_liabilities


# Leverage Financial Ratios
# Measure the amount of capital that comes from debt.


# Debt Ratio = Total Liabilities / Total Assets
def debt_ratio(total_liabilities, total_assets):
    """Measures the relative amount of a company’s assets that are
    provided from debt"""
    return total_liabilities / total_assets


# Debt to Equity Ratio = Total Liabilities / Total Shareholder’s Equity
def debt_to_equity_ratio(total_liabilities, total_equity):
    """Calculates the weight of total debt and financial liabilities
    against shareholders’ equity"""
    return total_liabilities / total_equity


# Interest Coverage Ratio = Operating Income / Interest Expense
def interest_coverage_ratio(operating_income, interest_expense):
    """Measures how easily a company can pay its interest expenses"""
    return operating_income / interest_expense


# Debt Service Coverage Ratio = Operating Income / Total Debt Service
def debt_service_coverage_ratio(operating_income, debt_service):
    """Measures how easily a company can pay its debt obligations"""
    return operating_income / debt_service


# Efficiency Ratios
# Measure how well a company is utilizing its assets and resources.


# Asset Turnover Ratio = Net Sales / Total Assets
def asset_turnover_ratio(net_sales, total_assets):
    """Measures a company’s ability to generate sales from assets"""
    return net_sales / total_assets


# Inventory Turnover Ratio = Cost of Goods Sold / Average Inventory
def inventory_turnover_ratio(cogs, average_inventory):
    """Measures how many times a company’s inventory is sold and
    replaced over a given period"""
    return cogs / average_inventory


# Accounts Receivable Turnover Ratio = Net Credit Sales / Average Accounts Receivable
def ar_turnover_ratio(net_credit_sales, average_ar):
    """Measures how many times a company can turn receivables into cash over a given period"""
    return net_credit_sales / average_ar


# Days Sales in Inventory Ratio (DSI) = 365 days / Inventory Turnover Ratio
def dsi_ratio(cogs, average_inventory, period=365):
    """Measures the average number of days that a company holds on to
    inventory before selling it to customers"""
    return period / inventory_turnover_ratio(cogs, average_inventory)


# Profitability Ratios
# Measure a company’s ability to generate income


# Gross Margin Ratio = Gross Profit / Net Sales
def gross_margin(gross_profit, net_sales):
    """Measures how much profit a company makes after paying its cost of goods sold"""
    return gross_profit / net_sales


# Operating Margin Ratio = Operating income / Net sales
def operating_margin(operating_income, net_sales):
    """Measures how much profit a company makes after paying its operating expenses"""
    return operating_income / net_sales


# Return on Assets Ratio
# The return on assets ratio measures how efficiently a company is using its assets to generate profit:
# Return on assets ratio = Net income / Total assets
# The return on equity ratio measures how efficiently a company is using its equity to generate profit:


# Return on Equity Ratio
# Return on equity ratio = Net income / Shareholder’s equity

# Market Value Ratios

# Market value ratios are used to evaluate the share price of a company’s stock. Common market value ratios include the following:


# Book Value per Share Ratio
# The book value per share ratio calculates the per-share value of a company based on equity available to shareholders:
# Book value per share ratio = Shareholder’s equity / Total shares outstanding


# Dividend Yield Ratio
# The dividend yield ratio measures the amount of dividends attributed to shareholders relative to the market value per share:
# Dividend yield ratio = Dividend per share / Share price


# Earnings per Share Ratio
# The earnings per share ratio measures the amount of net income earned for each share outstanding:
# Earnings per share ratio = Net earnings / Total shares outstanding


# Price-Earnings Ratio
# The price-earnings ratio compares a company’s share price to its earnings per share:
# Price-earnings ratio = Share price / Earnings per share
