from datetime import datetime


def format_time(iso_time_str):
    try:
        # Omvandla ISO-formatet till datetime-objekt och formatera endast tid
        time_obj = datetime.fromisoformat(iso_time_str.replace('Z', '+00:00'))
        return time_obj.strftime('%H:%M')
    except ValueError as e:
        print(f"Fel vid omvandling av tid '{iso_time_str}': {e}")
        return 'Ogiltig tid'
