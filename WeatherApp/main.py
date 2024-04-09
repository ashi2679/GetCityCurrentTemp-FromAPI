import requests
import subprocess
city = input("Enter the name of City: ", )
url = f"https://api.weatherapi.com/v1/current.json?key=9cf290280e394d6386f173444240904&q={city}"
r = requests.get(url).json()
data = f"Current Temprature in Celcius of {r["location"]["name"]} city is {r["current"]["temp_c"]})"
print(data)
command = (f'echo {data} | PowerShell -Command "Add-Type -AssemblyName System.Speech; '
                    f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak([Console]::In.ReadToEnd())"')
subprocess.run(command, shell=True)