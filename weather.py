from pyowm import OWM

API_KEY = "5b1bf16894d3ed0b8580d0974da9edc7"
owm = OWM(API_KEY)

mgr = owm.airpollution_manager()

observation = mgr.weather_at_coords(37.5683, 126.9778)
print(observation)

# print(w.detailed_status)
# print(w.wind())
# print(w.humidity)
# print(w.temperature('celsius'))
# print(w.rain)
# print(w.heat_index)
# print(w.clouds)
# print(w)