import requests
from datetime import datetime
import smtplib
import time

# YOU CAN SET YOUR OWN LATITUDE
MY_LAT = 51.507351
# YOU CAN SET YOUR OWN LONGITUDE
MY_LONG = -0.127758

# INSERT YOUR EMAIL
my_email = ""
# INSERT YOUR PASSWORD (YOU MAY NEED TO GO THROUGH ADDITIONAL SECURITY STEPS TO GET THROUGH YOUR EMAIL'S FIREWALL
my_pass = ""


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT + 5 <= iss_latitude <= MY_LAT - 5 and MY_LONG + 5 <= iss_longitude <= MY_LONG - 5:
        return True


def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if sunset >= time_now.hour <= sunrise:
        return True
# If the ISS is close to my current position


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_pass)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:ISS\n\nLOOK UP!!"
            )

