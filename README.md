# TESSR (The Extremely Small Security Robot)

TESSR is a simple, fully 3D printable, Raspberry Pi based robot designed to replace traditional CCTV: TESSR can move automatically supervise an area and alert users to suspicious activity (It can also be controlled manually from a mobile phone).

## Getting Started

### Requirements

Tools
* 3D Printer
* Soldering iron
* 9V Battery Charger

Hardware
* Raspberry Pi Zero with unsoldered headers
* SD card for Ras Pi (Raspbian strongly recommended)
* Raspberry Pi Camera
* Pi Borg Zero Borg (Standard or complete)
* Two 6V DC Motors (5V also works fine)
* HC-SR04 Ultrasound Distance Sensor
* Resistors (Various)
* M2 Bolts and nuts
* 1/2 inch ball bearing
* 9V Rechargeable battery

Software
* Python 3
* TESSR Code
* Blue Dot Python module

### Assembly

STL Files are included if you wish to print your own case, if not you can easily make your own out of whatever you want: early prototypes of TESSR were made out of cardboard. Detailed assembly instructions on the way.

### Install requirements

Download Python 3. 

```
$sudo apt-get install python3
```

Download Blue Dot module.

```
$sudo apt install python3-dbus
$sudo pip3 install bluedot
```

# Installation

Download TESSR code

```
Add download instructions when live!
```

## Contributing

Open to any and all improvements both to hardware and software. Raise an issue if you'd like to see a feature added or made a pull request through Git Hub if you'd like to contribute. Total cost of hardware not including tools is around £50, no changes will be made to hardware which increase this price.

## Authors

* **Hugh Evans** - *Initial work* - (https://github.com/HughEvans01)

See also list of [contributors](https://github/com/HughEvans01/TESSR/contributors) who participated in this project.

## License

This project is Unlicensed.

## Acknowledgements

* Find ZeroBorg thread
