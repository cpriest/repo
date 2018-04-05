#!/bin/env zsh

if [[ $# != 1 ]] {
	echo "This script takes exactly one argument which should be the version of cpriest-repo-release as in ./build.zsh 1.0";
	exit 1;
}

NAME="cpriest-repo-release";
VER_NAME="cpriest-repo-release-$1";
FILES=(cpriest.repo RPM-GPG-KEY-cpriest-repo);

echo -e "\e[31;1mCreating tar archive of $FILES into $VER_NAME\e[m";

{ 
	mkdir $VER_NAME || exit 1; 

	cp -t $VER_NAME $FILES || exit 1;

	tar -cvzf ~/rpmbuild/SOURCES/$VER_NAME.tar.gz $VER_NAME || exit 1;
	echo;
	ls -a --color ~/rpmbuild/SOURCES/$VER_NAME.tar.gz;

	rm -rf $VER_NAME;
} |& perl -pe 's/^/\t/g';

echo;

cp cpriest-repo-release.spec ~/rpmbuild/SPECS/

echo -e "\e[31;1mBuilding the repository...\e[m";

rpmbuild -ba ~/rpmbuild/SPECS/cpriest-repo-release.spec |& perl -pe 's/^/\t/g';

echo;
echo -e "\e[31;1mLinting the spec file...\e[m";
rpmlint -i ~/rpmbuild/SPECS/cpriest-repo-release.spec |& perl -pe 's/^/\t/g';
echo;
echo;
echo -e "\e[31;1mMoving the RPM file into place...\e[m";
mkdir -p ../../CentOS/noarch/
mv -v ~/rpmbuild/RPMS/noarch/cpriest-repo-release*.rpm ../../CentOS/noarch/ |& perl -pe 's/^/\t/g' |& perl -pe "s/['‘’]//g";
