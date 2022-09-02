halcmd -s show pin | grep "==" > pin.out
halcmd -s show sig | grep -v "^$" > sig.out
python graphviz.py > gv.in
dot -Tpng gv.in > gv.png
