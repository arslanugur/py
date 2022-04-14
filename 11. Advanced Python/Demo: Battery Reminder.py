import psutil                     # Library
from plyer import notification    # Library
import time

battery = psutil.sensors_battery()
while True:
  percent = battery.percent
  notification.notify(
    title="Battery Percentage",
    message="%"+ str(percent)+ "battery left.",
    timeout=10
  )
  time.sleep(60*60)
  continue
#


