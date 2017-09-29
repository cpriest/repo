#!/bin/env zsh

ORIG_WD=$PWD;
cd ${1:-$PWD};

[[ "$ORIG_WD" = "$PWD" ]] &&
	ORIG_WD=".";

REPODIR="/opt/repo/repo";

NAME="`basename $PWD`";

[[ -e ./$NAME.spec ]] || {
	echo "Expecting file $ORIG_WD/$NAME.spec to exist, you may pass a directory name as the first argument to use instead of $ORIG_WD.";
	exit 1;
}

VERSION=`pcregrep -o1 '^Version:\s+([\d\.]+)$' $NAME.spec`;
ARCH=`pcregrep -o1 '^BuildArch:\s+(.+)$' $NAME.spec`;

VER_NAME="$NAME-$VERSION";

indent() {
	perl -pe 's/^/\t/g';
}

echo -e "\e[31;1mCreating tar archive of \e[33;1m./files/\e[31;1m into $VER_NAME\e[m";
{
	cp -r ./files $VER_NAME; 
	tar -cvzf ~/rpmbuild/SOURCES/$VER_NAME.tar.gz $VER_NAME || exit 1;
	rm -rf $VER_NAME;
} |& indent;

echo;

cp $NAME.spec ~/rpmbuild/SPECS/

echo -e "\e[31;1mBuilding the repository...\e[m";
rpmbuild -ba ~/rpmbuild/SPECS/$NAME.spec |& indent;

echo;
echo -e "\e[31;1mLinting the spec file...\e[m";
rpmlint -i ~/rpmbuild/SPECS/$NAME.spec |& indent;
echo;
echo;
echo -e "\e[31;1mCopying the RPM file into place...\e[m";
mkdir -p $REPODIR/CentOS/7/$ARCH/
cp -v ~/rpmbuild/RPMS/$ARCH/$NAME*.rpm $REPODIR/CentOS/7/$ARCH/ |& indent;
