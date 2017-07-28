#!/bin/env zsh

for dir in `realpath $(dirname **/*.rpm | sort | uniq | perl -pe 's/$/\/../') | sort | uniq`; {
	echo "Building $dir...";
	cd $dir;
	createrepo . | perl -pe 's/^/\t/g';
}

echo "Signing RPM Packages, enter gpg passwordi...";
rpm --addsign **/*.rpm
