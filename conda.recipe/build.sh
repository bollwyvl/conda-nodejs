#!/bin/sh

[ ! -e $PREFIX/bin ] && mkdir -p $PREFIX/bin
[ ! -e $PREFIX/lib ] && mkdir -p $PREFIX/lib

mv -f $SRC_DIR/bin/node $PREFIX/bin
mv -f $SRC_DIR/lib/* $PREFIX/lib
