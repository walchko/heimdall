# I2S Microphone Setup

- [Adafruit tutorial](https://learn.adafruit.com/adafruit-i2s-mems-microphone-breakout?view=all#raspberry-pi-wiring-and-test)

## Kernel Compiling

Here is the short/skinny of the Adafruit tutorial

```bash
sudo apt-get update
sudo apt-get install rpi-update
sudo rpi-update
```

```bash
sudo apt-get install git bc libncurses5-dev
```

```bash
sudo wget https://raw.githubusercontent.com/notro/rpi-source/master/rpi-source -O /usr/bin/rpi-source
sudo chmod +x /usr/bin/rpi-source
/usr/bin/rpi-source -q --tag-update
rpi-source --skip-gcc
```

```bash
sudo mount -t debugfs debugs /sys/kernel/debug
```
This may already be done - **mount: debugs is already mounted**  - in which case keep going

If you are using Pi 3 or Pi 2 - make sure the module name is `3f203000.i2s`

If you are using Pi Zero - the module name is `20203000.i2s`

```bash
$ sudo cat /sys/kernel/debug/asoc/platforms
3f203000.i2s
snd-soc-dumy
```
```bash
git clone https://github.com/PaulCreaser/rpi-i2s-audio
cd rpi-i2s-audio
```

```bash
make -C /lib/modules/$(uname -r )/build M=$(pwd) modules
sudo insmod my_loader.ko
```

Verified the module was loaded:

```bash
lsmod | grep my_loader
dmesg | tail
```

Note that on the Pi 2/3 you'll see `asoc-simple-card asoc-simple-card.0: snd-soc-dummy-dai <-> 3F203000.i2s mapping ok` 
on the last line and on Pi Zero you'll see `asoc-simple-card asoc-simple-card.0: snd-soc-dummy-dai <-> 20203000.i2s mapping ok`

## Test

`arecord -l` should give `snd_rpi_simple_card`

- Mono mic: `arecord -D plughw:1 -c1 -r 48000 -f S32_LE -t wav -V mono -v file.wav`
- Stereo mics: `arecord -D plughw:1 -c2 -r 48000 -f S32_LE -t wav -V stereo -v file_stereo.wav`

## Volume Control

`pico ~/.acoundrc`

```bash
#This section makes a reference to your I2S hardware, adjust the card name
# to what is shown in arecord -l after card x: before the name in []
#You may have to adjust channel count also but stick with default first
pcm.dmic_hw {
	type hw
	card sndrpisimplecar
	channels 2
	format S32_LE
}

#This is the software volume control, it links to the hardware above and after
# saving the .asoundrc file you can type alsamixer, press F6 to select
# your I2S mic then F4 to set the recording volume and arrow up and down
# to adjust the volume
# After adjusting the volume - go for 50 percent at first, you can do
# something like 
# arecord -D dmic_sv -c2 -r 48000 -f S32_LE -t wav -V mono -v myfile.wav
pcm.dmic_sv {
	type softvol
	slave.pcm dmic_hw
	control {
		name "Boost Capture Volume"
		card sndrpisimplecar
	}
	min_dB -3.0
	max_dB 30.0
}
```
