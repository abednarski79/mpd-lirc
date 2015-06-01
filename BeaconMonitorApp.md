# Introduction #

Bluetooth low energy (aka. iBeacon) monitoring application

# Converting square image to android launcher icon #
```
 gm convert -size 144x144 1404678554_50.png -resize 144x144 -background white -compose Copy -gravity center -extent 144x144 144_144.png
 gm convert -size 96x96 1404678554_50.png -resize 96x96 -background white -compose Copy -gravity center -extent 96x96 96_96.png
 gm convert -size 72x72 1404678554_50.png -resize 72x72 -background white -compose Copy -gravity center -extent 72x72 72_72.png
 gm convert -size 48x48 1404678554_50.png -resize 48x48 -background white -compose Copy -gravity center -extent 48x48 48_48.png
```
```
cp 48_48.png drawable-mdpi/ic_launcher.png
cp 72_72.png drawable-hdpi/ic_launcher.png
cp 96_96.png drawable-xhdpi/ic_launcher.png
cp 144_144.png drawable-xxhdpi/ic_launcher.png
```