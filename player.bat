set URL=https://youtu.be/LXsxxXKellI

echo %URL%

youtube-dl -f best %URL% -o - | ffplay -noborder -window_title pynamic_player -loop 0 -x %1 -y %2 -