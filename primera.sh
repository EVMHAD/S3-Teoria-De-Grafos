# esto es para linux
python3 primera.py
cat graph.json | python3 -m json.tool
gifsicle graph.gif --no-loopcount --colors 256 > tmp.gif # seriously no looping
gifview -a tmp.gif # http://manpages.ubuntu.com/manpages/bionic/man1/gifview.1.html
