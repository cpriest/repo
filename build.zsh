#!/bin/env zsh

echo "Signing RPM Packages, enter gpg password...";
rpmsign --addsign **/*.rpm |& grep -v 'WARNING: unsafe ownership on configuration'

for dir in `ls -1d **/*.rpm(:h:h:A) | sort -u`; {
	echo "Building $dir...";
	( 
		cd $dir;
		if [[ "$dir" == "/opt/repo/repo/CentOS" ]] {
			ls -1 noarch/**.rpm > noarch.pkgs
			createrepo --deltas -i noarch.pkgs . | perl -pe 's/^/\t/g';
			rm -f noarch.pkgs;
		} else {
			createrepo --deltas . | perl -pe 's/^/\t/g';
		}
	)
}
echo;
echo "Adding ./CentOS to git and comitting a build release";
git add --all CentOS
git commit -m 'Build of repo';
git push;
