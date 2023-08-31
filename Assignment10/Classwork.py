def main():
   print("In dictionaries()") 
   
#    phoneBook =[{Mike: "555-1111",
#                 Katie: "555-2222",
#                 JoAnne: "555-3333"}]
   
#    print(type(phoneBook))
   Blacksburg_Forecast = [ 
                    { 'humidity' :  20, 'temperature' : 78, 'wind' :  7},
                    { 'humidity' :  50, 'temperature' : 61, 'wind' : 10},
                    { 'humidity' : 100, 'temperature' : 81, 'wind' :  5},
                    { 'humidity' :  90, 'temperature' : 62, 'wind' : 15},
                    { 'humidity' :  30, 'temperature' : 84, 'wind' : 19},
                    { 'humidity' :   0, 'temperature' : 66, 'wind' : 28},
                    { 'humidity' :   0, 'temperature' : 87, 'wind' : 12},
                    { 'humidity' :   0, 'temperature' : 68, 'wind' : 14},
                    { 'humidity' :   0, 'temperature' : 86, 'wind' :  4},
                    { 'humidity' :  60, 'temperature' : 68, 'wind' :  0}                    
                    ]
   print(type(Blacksburg_Forecast))
   print(type(Blacksburg_Forecast[0]))
   
   print("Wind Speed")
   for forecast in Blacksburg_Forecast:
        wind_speed = forecast["wind"]
        humidity = forecast["humidity"]
        temperature = forecast["temperature"]
        print(wind_speed, humidity, temperature)  
    
   aggregate = 0
   for forecast in Blacksburg_Forecast:
        aggregate += forecast["temperature"]
        print()
    
if __name__ == "__main__":
    main()