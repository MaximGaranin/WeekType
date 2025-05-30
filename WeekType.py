from datetime import datetime, date

def get_week_type(base_date_str=None): 
    try:
        base_date = datetime.strptime(base_date_str, "%d.%m.%Y").date() if base_date_str else date.today()
    except ValueError:
        return "Ошибка: неверный формат даты. Используйте ДД.ММ.ГГГГ"
    
    reference_date = datetime.strptime("24.03.2025", "%d.%m.%Y").date()
    
    delta_weeks = (base_date - reference_date).days // 7
    
    return "Числитель" if delta_weeks % 2 == 0 else "Знаменатель"

if __name__ == "__main__":
    user_date = input("Введите дату или оставьте пустым для проверки сегодняшнего дня: ").strip()
    
    print(f"Дата {user_date if user_date else date.today().strftime('%d.%m.%Y')} - {get_week_type(user_date)}")