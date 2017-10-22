Summary:        Advanced Linux download manager
Name:           prozilla
Version:        2.0.4
Release:        18%{?dist}

License:        GPLv2+
Group:          Applications/Internet
Source0:        http://prozilla.genesys.ro/downloads/prozilla/tarballs/%{name}-%{version}.tar.bz2
Patch0:         prozilla1.patch
URL:            http://prozilla.genesys.ro/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ncurses-devel, gettext


%description
ProZilla is a download accellerator program written for Linux to speed
up the normal file download process. It often gives speed increases of
around 200% to 300%. It supports both FTP and HTTP protocols, and the
theory behind it is very simple.

The program opens multiple connections to a server, and each of the
connections downloads a part of the file, thus defeating existing
internet congestion prevention methods which slow down a single
connection based download.

ProZilla also supports file download resuming, and ftpsearch for
fastest ping times.



%package devel
Summary: Development libraries and headers for prozilla
Group: Development/Libraries
Requires: %{name} = %{version}


%description devel
The developmental files that must be installed in order to compile
applications which use prozilla.

%prep
%setup -q

# fix for makeinstall macro
sed -i -e \
     s'|gnulocaledir = $(prefix)/share/locale|gnulocaledir = ${RPM_BUILD_ROOT}$(prefix)/share/locale|' \
     po/Makefile.in.in

sed -i -e \
     s'|gnulocaledir = $(prefix)/share/locale|gnulocaledir = ${RPM_BUILD_ROOT}$(prefix)/share/locale|' \
     libprozilla/po/Makefile.in.in

%patch0 -p1
%configure

%build
CFLAGS="$RPM_OPT_FLAGS"
export CFLAGS

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=${RPM_BUILD_ROOT} INSTALL="install -p" install


rm -f ${RPM_BUILD_ROOT}%{_libdir}/libprozilla.la
rm -f ${RPM_BUILD_ROOT}%{_libdir}/libprozilla.a



rm -f ${RPM_BUILD_ROOT}%{_datadir}/locale/locale.alias ||:


%find_lang proz

%clean
rm -rf ${RPM_BUILD_ROOT}


%files -f proz.lang
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING CREDITS* NEWS README TODO
%doc libprozilla/docs/HACKING docs/FAQ
%{_bindir}/proz
%{_mandir}/man1/proz*
# from libprozilla
%{_datadir}/locale/it/LC_MESSAGES/.mo
%{_datadir}/locale/nl/LC_MESSAGES/.mo
%{_datadir}/locale/pt_BR/LC_MESSAGES/.mo
%{_datadir}/locale/ro/LC_MESSAGES/.mo


%files devel
%defattr(-,root,root,-)
%{_includedir}/prozilla/



%changelog
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Aug 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 2.0.4-9
- fix license tag

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.0.4-8
- Autorebuild for GCC 4.3

* Mon Jan 01 2007 ChitleshGoorah <chitlesh [AT fedoraproject DOT org] - 2.0.4-7
- Fixed for x86_64

* Sat Dec 09 2006 ChitleshGoorah <chitlesh [AT fedoraproject DOT org] - 2.0.4-3
- added gettext to BR
- added timestamps to make install
- fixed locales
- added RPM_OPT_FLAGS to %%make

* Tue Oct 10 2006 Kushal Das <kushaldas@gmail.com> - 2.0.4-2
- spec file fixed

* Fri Oct 06 2006 Kushal Das <kushaldas@gmail.com> - 2.0.4-1
- New Release

* Mon Aug 27 2006 Michael J. Knox <michael[AT]knox.net.nz> - 1.3.7.4-4
- Rebuild for FC6

* Wed May 02 2006 Michael J. Knox <michael[AT]knox.net.nz> - 1.3.7.4-3
- rebuild

* Fri Jan 20 2006 Hans de Goede <j.w.r.degoede@hhs.nl>
- Fix CAN-2005-2961 / bugzilla 169791

* Fri Sep 09 2005 Ralf Corsepius <rc040203@freenet.de>
- %%{_bindir}/proz.

* Thu Aug 25 2005 Warren Togami <wtogami@redhat.com> - 0:1.3.7.4-1
- 1.3.7.4 Security (#166789)

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net>
- rebuilt

* Wed Feb  2 2005 Dams <anvil[AT]livna.org> - 0:1.3.7.3-1
- Updated to 1.3.7.3
- Misc cleanups

* Tue Apr  1 2003 Dams <anvil[AT]livna.org> 0:1.3.6-0.fdr.1
- Modified Spec according to fedora template/guidelines.
- Added BuildRequires tag.

* Mon Aug 17 2001 Ralph Slooten <axllent@axllent.cjb.net>
- Prozilla 1.3.6 Released

* Sat Mar 31 2001 Ralph Slooten <axllent@axllent.cjb.net>
- Prozilla 1.3.4 Released
- Improvements in Prozilla (fixes)
- Download screen now shows actual rate and average rate

* Tue Mar 06 2001 Kalum / Grendel<kalum@lintux.cx>
- Prozilla 1.3.3.2 released
- Added several backup ftpsearch servers to fall back, if the main one
  fails
- Added prozilla.spec and modified the Makefile.am, to make rpms if
  necessary.

* Sun Mar 04 2001 Ralph Slooten <axllent@axllent.cjb.net>
- Prozilla 1.3.3.1 released
- ncurses display fixed to show no blank spaces

* Fri Mar 02 2001 Ralph Slooten <axllent@axllent.cjb.net>
- Development ProZilla 1.3.3 released
- Fixed ftp search URL
- Fixed Makefile.in problem fixed
- Spec file changed to suite /etc dir
- Spec file updated using definitions

* Sun Feb 18 2001 Ralph Slooten <axllent@axllent.cjb.net>
- ProZilla version 1.3.2 released
- Global preferences files added in /ect file
- Spec file changed to suite config file needs
- Makefile.in changed to suite RPM's needs... Needs to be fixed!

* Tue Feb 6 2001 Ralph Slooten <axllent@axllent.cjb.net>
- ProZilla version 1.3.1 released
- New FTP search function implemented into Prozilla
- proz manpage symlinked to prozilla man page
- gproz falls out due to drastic changes in Prozilla
- CHANGES file dropped due to existing Changelog
- Rpm spec file changes to suite Prozilla

* Fri Jan 25 2001 Ralph Slooten <axllent@axllent.cjb.net>
- Tweaked up the RPM spec file

* Mon Jan 22 2001 Ralph Slooten <axllent@axllent.cjb.net>
- man proz added, instead of just prozilla
- Server tweaking and changes (Read CHANGES)

* Wed Jan 3 2001 Calum Selkirk <cselkirk@sophix.uklinux.net>
- added RPM_BUILD_ROOT and install to that dir
- added RPM_OPT_FLAGS
- changed Source0: to use %%version
