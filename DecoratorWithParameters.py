import time

def retry(call_count = 3, start_sleep_time = 1, factor = 2, border_sleep_time = 10):
  def decorator(function):
    def wrapper(*args, **kwargs):
      retries = 0
      t = start_sleep_time
      print(f'Начало работы.')
      while retries < call_count and t <= border_sleep_time:
        time.sleep(t)
        retries += 1
        value = function(*args, **kwargs)
        print(f'Запуск № {retries}. Ожидание: {t} секунд. Результат декорируемой функции = {value}') 
        t *= (factor**retries)
        t = border_sleep_time if t >= border_sleep_time else t
      print(f'Конец работы.')
    return wrapper
  return decorator
    
@retry(3, 1, 2, 100)
def hello(name):
  return (f"Hello, {name}!")
