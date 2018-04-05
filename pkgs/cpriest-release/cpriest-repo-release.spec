Name:		cpriest-repo-release
Summary:	Installs the repository reference for my repository
Version:	1.0
Release:	2
License:	MIT
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
This installs Clint Priests' public repo, use entirely at your own risk.

As of 2018-04-05 this consists of packages built for CentOS 6 & 7 on CentOS 7.3 using Fedora source RPMs, nothing special.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/etc/yum.repos.d/
mkdir -p %{buildroot}/etc/pki/rpm-gpg/
cp cpriest.repo %{buildroot}/etc/yum.repos.d/cpriest.repo
cp RPM-GPG-KEY-cpriest-repo %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-cpriest-repo

%files
%config(noreplace) /etc/yum.repos.d/cpriest.repo
%config(noreplace) /etc/pki/rpm-gpg/RPM-GPG-KEY-cpriest-repo

%changelog
 * Thu Apr 05 2018 - Clint Priest <github-repo@rxv.me> 1.0.2
 - Built as noarch without .el7
 * Sat Jul 29 2017 - Clint Priest <github-repo@rxv.me> 1.0
 - Initial build of release rpm
