
def sensorStub():
    return {
        'temperatureInC': 50,
        'precipitation': 70, 
        'humidity': 26,
        'windSpeedKMPH': 52
    }


def sensorStubHighPrecipitation():
    return {
        'temperatureInC': 30,  
        'precipitation': 80,   
        'humidity': 90,        
        'windSpeedKMPH': 40    
    }

def sensorStubPartlyCloudy():
    return {
        'temperatureInC': 30,  
        'precipitation': 40,   
        'humidity': 70,
        'windSpeedKMPH': 30
    }


def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day" 

    if (readings['temperatureInC'] > 25): 
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"

    return weather


def testRainy():

    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)


def testHighPrecipitation():
    weather = report(sensorStubHighPrecipitation) 
    print(f"testHighPrecipitation -> {weather}")

    assert("Sunny Day" not in weather) 

if __name__ == '__main__':
    testRainy()
    testHighPrecipitation() 
    print("All is well (maybe!)"); 
