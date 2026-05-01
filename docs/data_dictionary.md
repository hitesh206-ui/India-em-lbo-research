# Data Dictionary

## india_buyout_deals.csv

| Column | Description |
|---|---|
| deal_id | Unique deal identifier |
| announcement_date | Date deal was announced |
| target_name | Target company name |
| country | Target country |
| sector | Target sector |
| sponsor | Private equity sponsor or investor |
| deal_type | Buyout, control investment, minority PE, take-private, platform acquisition |
| enterprise_value_usd_mn | Enterprise value in USD million |
| ebitda_usd_mn | EBITDA in USD million |
| ev_ebitda_multiple | Entry EV/EBITDA multiple |
| debt_amount_usd_mn | Debt used in transaction |
| equity_amount_usd_mn | Sponsor equity contribution |
| debt_ebitda | Debt / EBITDA |
| debt_instrument_type | INR term loan, NCD, CCD, private credit, offshore debt, other |
| interest_rate | Estimated or disclosed borrowing cost |
| exit_route | IPO, strategic sale, secondary sale, continuation vehicle, pending |
| source_url | Public source link |
| notes | Analyst notes |

## regulatory_timeline.csv

| Column | Description |
|---|---|
| date | Date of regulatory event |
| jurisdiction | Country or legal jurisdiction |
| regulation | Law, circular, rule, or court decision |
| category | Companies Act, RBI, SEBI, tax, insolvency, foreign investment |
| effect_on_lbo | Expected impact on LBO feasibility |
| severity_score | 1 low to 5 high |
| source_url | Public source link |
