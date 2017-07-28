Name:		cpriest-repo-release
Summary:	Installs the repository reference for my repository
Version:	1.0
Release:	1%{?dist}
License:	MIT
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch

%description
This installs Clint Priests' public repo, use entirely at your own risk.

As of 2017-07-28 this consists of packages built on CentOS 7.3 using Fedora source RPMs, nothing special.

%prep
%setup -q

%install
mkdir -p %{buildroot}/etc/yum.repos.d/
mkdir -p %{buildroot}/etc/pki/rpm-gpg/
cp cpriest.repo %{buildroot}/etc/yum.repos.d/cpriest.repo
cp RPM-GPG-KEY-cpriest-repo %{buildroot}/etc/pki/rpm-gpg/RPM-GPG-KEY-cpriest-repo

%files
%config(noreplace) /etc/yum.repos.d/cpriest.repo
%config(noreplace) /etc/pki/rpm-gpg/RPM-GPG-KEY-cpriest-repo

%changelog
 * Sat Jul 29 2017 - Clint Priest <github-repo@rxv.me> 1.0
 - Initial build of release rpm
