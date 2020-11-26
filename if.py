# weather = input("How is the weather today?")
# if weather == "rain" or weather == "snow":
#     print("Take your umbrella.")
# elif weather == "Dust":
#     print("Take your mask")
# else:
#     print("Today is no prepare anything")


temp = int(input("How's the temperature today?"))
if 30 <= temp:
    print("so hot. don't go outside, stay home")
elif 10 <= temp and temp < 30:
    print("today is good weather, let's0 go out!")
elif 0 <= temp < 10:
    print("Please pack your coat, weather is so cold")
else:
    print("Don't go out, amazing cold")