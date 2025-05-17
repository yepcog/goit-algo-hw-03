from datetime import datetime, date, timedelta

def get_days_from_today(date):
    try:
        try_date = datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        error_message = f"time data '{date}' does not match format '%Y-%m-%d'"
        return error_message
    else:
        today_date = datetime.today().date()
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        diff = (given_date - today_date).days
        return diff

print(get_days_from_today("2025-09-17"))