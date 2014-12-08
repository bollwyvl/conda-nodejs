#!/bin/sh

for d in bin include lib; do
    [ ! -e $PREFIX/$d ] && mkdir -p $PREFIX/$d
    cp -r $SRC_DIR/$d/* $PREFIX/$d
done
