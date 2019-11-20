
echo 'default-on' > /sys/class/leds/nanopi:blue:status/trigger
./3unit.sh
echo 'none' > /sys/class/leds/nanopi:blue:status/trigger
./1unit.sh
