import os
import math
import time
import signal
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import subprocess
import psutil

DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=None)
font = ImageFont.load_default()

disp.begin()
disp.clear()
disp.display()

image = Image.new('1', (disp.width, disp.height))
draw = ImageDraw.Draw(image)
data = {}

def stop(sig, frame):
    draw.rectangle((0, 0, disp.width - 1, disp.height - 1), outline=1, fill=0)
    disp.display()

def remap(value, fromMin, fromMax, toMin, toMax):
    return (((value - fromMin) * (toMax - toMin)) / (fromMax - fromMin)) + toMin

def getMetrics():
    data['hostname'] = subprocess.check_output("hostname", shell = True)
    data['ip'] = subprocess.check_output("hostname -I | cut -d\' \' -f1", shell = True)
    data['disk'] = int(os.popen("df / | awk '{ print $5 }' | tail -n 1").readline().replace("%\n",""))
    data['temp'] = int(math.floor(float(os.popen("vcgencmd measure_temp | cut -c6-").readline().replace("'C\n",""))))
    data['cpu'] = int(math.floor(psutil.cpu_percent()))
    data['clock'] = int(subprocess.check_output("cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq", shell = True)) / 1000
    data['id'] = os.popen("hostname").readline().replace("\n","")
    total = int(os.popen("free -h | grep 'Mem' | cut -c15-23").readline().strip().replace("M",""))
    available = int(os.popen("free -h | grep 'Mem' | cut -c70-").readline().strip().replace("M",""))
    data['memory'] = int(math.floor((available * 100) / total))

if __name__ == '__main__':
    while True:
        getMetrics()
        draw.rectangle((0, 0, disp.width - 1, disp.height - 1), outline=1, fill=0)
        valCpu = remap(data['cpu'], 0, 100, 0, 125)
        valTemp = remap(data['temp'], 30, 90, 0, 125)
        draw.rectangle((2, 2, valCpu, 15), outline=0, fill=1)
        draw.rectangle((2, 16, valTemp, 29), outline=0, fill=1)
        draw.text((4, 17), str(data['temp']) + "*C " + str(data['clock']) + "Mhz",  font=font, fill=0)
        if data['cpu'] > 20:
            draw.text((4, 4), str(data['cpu']) + "%",  font=font, fill=0)
        disp.image(image)
        disp.display()
        time.sleep(.1)
