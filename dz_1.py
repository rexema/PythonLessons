duration = int(input("Введите продолжительность: "))
minute = duration // 60
second = duration % 60

if duration < 60:
    print(duration, "сек")
elif 60 <= duration < 3600:
    print(minute, "мин", second, "сек")
elif 3600 <= duration < 86400:
    hour = duration // 3600
    minute = (duration % 3600) // 60
    print(hour, "час", minute, "мин", second, "сек")
elif duration >= 86400:
    day = duration // 86400
    hour = (duration / 86400 - day) * 24
    minute = (hour - int(hour)) * 60
    second = (minute - int(minute)) * 60
    print(day, "дн", int(hour), "час", int(minute), "мин", int(second), "сек")
