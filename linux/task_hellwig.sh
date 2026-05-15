#!/bin/bash

WORKDIR=/opt/060326-ptm/hellwig

mkdir -p $WORKDIR

touch $WORKDIR/{1..10}_$(date +%d.%m.%y)
