from datetime import datetime, timedelta

def format_conv_date (date):
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)
    start_of_week = today - timedelta(days=today.weekday())  #Mondayb of current day
    if date == today:
        return "Aujourd'hui"
    elif date == yesterday:
        return "Hier"
    elif start_of_week <= date < today:
        days_of_week = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
        return days_of_week[datetime.weekday()]
    else: 
        return datetime.strftime("%d %m %Y")