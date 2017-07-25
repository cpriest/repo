#!/bin/env zsh

for dir in `dirname **/*.rpm | sort | uniq`; {
	echo "Building $dir...";
	cd $dir;
	createrepo . | perl -pe 's/^/\t/g';
}
