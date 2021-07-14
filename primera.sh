# esto es para linux
python3 primera.py
cat graph.json | python3 -m json.tool
gifsicle tmp.gif --no-loopcount --colors 256 > graph.gif # seriously no looping
rm tmp.gif
gifview -a graph.gif # http://manpages.ubuntu.com/manpages/bionic/man1/gifview.1.html
