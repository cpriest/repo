#!/bin/env zsh

#for dir in `realpath $(dirname **/*.rpm | sort | uniq | perl -pe 's/$/\/../') | sort | uniq`; {
for dir in `ls -1d **/*.rpm(:h:h:A) | sort -u`; {
	echo "Building $dir...";
	cd $dir;
	createrepo . | perl -pe 's/^/\t/g';
}

echo "Signing RPM Packages, enter gpg passwordi...";
rpm --addsign **/*.rpm
