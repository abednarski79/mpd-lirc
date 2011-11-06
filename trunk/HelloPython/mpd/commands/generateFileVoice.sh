# find /tmp/music/ -name "*.mp3" -exec generateFileVoice.sh '{}' \;
mp3info -p "%a, %l, %t \n" "$1" 
file_wav=`mp3info -p "%F.wav" "$1"`
mp3info -p "%a, %l, %t" "$1" | text2wave -o "$file_wav"

