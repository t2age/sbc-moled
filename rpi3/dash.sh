
echo 1 >/sys/class/leds/led0/brightness
./3unit.sh
echo 0 >/sys/class/leds/led0/brightness
./1unit.sh
