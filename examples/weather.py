from pysis import SIS
from pysis.core.sis_datetime import convertToDateTime

if __name__ == "__main__":
    s = SIS(token="891fea6456f40f6369b824fb0a8ddcf0d983096f")
        
    print("\nWeather Accounts \n---------------------------")
    data = s.weather.getAccounts()
    for x in data:
        print(str(x.id) + ' : ' + x.email + ' : ' + x.last_call_time)
        
    print("\nWeather Accounts (with id) \n---------------------------")
    x = s.weather.getAccounts(1)
    print(str(x.id) + ' : ' + x.email + ' : ' + x.last_call_time)
    
    print("\nWeather Locations \n---------------------------")
    data = s.weather.getLocations()
    for x in data:
        print(str(x.id) + ' : ' + x.city + ' : ' + x.search_key)
        
    print("\nWeather Locations (with id) \n---------------------------")
    x = s.weather.getLocations(1)
    print(str(x.id) + ' : ' + x.city + ' : ' + x.search_key)
    
    print("\nWeather Types \n---------------------------")
    data = s.weather.getTypes()
    for x in data:
        print(x.type + ' : ' + x.title + ' : ' + x.description)
        
    print("\nWeather Types (with type) \n---------------------------")
    x = s.weather.getTypes("actuals")
    print(x.type + ' : ' + x.title + ' : ' + x.description)
    
    print("\nWeather Actual Highs \n---------------------------")
    data = s.weather.getActualHighs(1, "20141025", "20141030")
    for x in data:
        print(x.date + ' : ' + str(x.high))
        
    print("\nWeather Actual Temps \n---------------------------")
    data = s.weather.getActualTemps(1, "20150201", None, "20150203", 15)
    for x in data:
        date = convertToDateTime(x.date).strftime("%Y.%m.%d:%H")
        print(date + ' : ' + str(x.value))
    
    print("\nWeather Forecasts Daily \n---------------------------")
    data = s.weather.getForecastDaily(1)
    for day in data:
        print(day.forecast_high)
    
    
    print("\nWeather Forecasts Hourly \n---------------------------")
    data = s.weather.getForecastHourly(1)
    for x in data:
        date = convertToDateTime(x.date).strftime("%Y.%m.%d:%H")
        print(date + ' : ' + str(x.value))
    
    
    
    
