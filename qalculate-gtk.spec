%define bname qalculate

Summary:	A very versatile desktop calculator
Name:		qalculate-gtk
Version:	0.9.7
Release:	%mkrel 4
License:	GPLv2+
Group:		Office
URL:		http://qalculate.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/qalculate/%{name}-%{version}.tar.bz2
Patch1:		qalculate-gtk-0.9.6-fix-str-fmt.patch
BuildRequires:	libqalculate-devel >= %{version}
BuildRequires:	libglade2.0-devel
BuildRequires:	gtk+2-devel
BuildRequires:	imagemagick
BuildRequires:	scrollkeeper
BuildRequires:	perl(XML::Parser)
BuildRequires:	desktop-file-utils
BuildRequires:	libgnome2-devel
Requires(pre):	scrollkeeper
Requires:	gnuplot
Requires:	wget
Obsoletes:	qalculate < %{version}
Provides:	qalculate = %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting,
and a graphical interface that uses a one-line fault-tolerant expression entry 
(although it supports optional traditional buttons). 
This package provides the GTK frontend.

%prep
%setup -q
%patch1 -p0

%build

%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 

#menu
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48}/apps

#icons 
convert -size 48x48 data/%{bname}.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png 
convert -size 32x32 data/%{bname}.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png 
convert -size 16x16 data/%{bname}.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

#(tpg) drop icon extension
sed -i -e 's/^Icon=%{bname}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applications/*

desktop-file-install \
	--remove-category="Application" \
	--add-category="GTK" \
	--add-category="Calculator" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/* 

##CAE rm symlink so both gtk and kde frontend are installable
rm -f %{buildroot}%{_bindir}/qalculate

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade/*.glade
%{_iconsdir}/hicolor/*/apps/%{name}.png


%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.7-4mdv2011.0
+ Revision: 669366
- mass rebuild

* Sat Dec 04 2010 Funda Wang <fwang@mandriva.org> 0.9.7-3mdv2011.0
+ Revision: 608594
- update file list

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuild

* Tue Jan 26 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.7-1mdv2010.1
+ Revision: 496826
- update to new version 0.9.7
- drop patch0, fixed upstream

* Sun Sep 27 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-3mdv2010.0
+ Revision: 449912
- rebuild for new cln

* Sat Mar 21 2009 Funda Wang <fwang@mandriva.org> 0.9.6-2mdv2009.1
+ Revision: 359928
- fix str fmt

* Thu Jun 12 2008 Pixel <pixel@mandriva.com> 0.9.6-2mdv2009.0
+ Revision: 218429
- rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-2mdv2008.1
+ Revision: 182217
- bump release tag

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-1mdv2008.1
+ Revision: 182198
- Patch0: fix building against latest cln-1.2
- add missing buildrequires on libgnome2-devel
- fix desktop file

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jun 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.9.6-1mdv2008.0
+ Revision: 43700
- drop old menu style
- drop X-MandrivaLinux
- fix file list
- adjust buildrequires
- move icons to fd.o compiliant directory
- spec file clean
- new version
- use macros


* Fri Oct 27 2006 Nicolas LÃ©cureuil <neoclust@mandriva.org> 0.9.4-3mdv2007.0
+ Revision: 73122
- import qalculate-gtk-0.9.4-3mdv2007.1

* Sat Aug 05 2006 Charles A Edwards <eslrahc@mandriva.org> 0.9.4-2mdv2007.0
- rebuild for latest dbus

* Wed Jun 28 2006 Charles A Edwards <eslrahc@mandriva.org> 0.9.4-1mdv2007.0
- name change for spec and pkg
- 0.9.4
- update filelist
- xdg

* Fri Dec 02 2005 Thierry Vignaud <tvignaud@mandriva.com> 0.7.2-2mdk
- rebuild for new cln
- patch 0: fix compiling with g++-4

* Tue Feb 01 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.7.2-1mdk
- 0.7.2

* Sat Jan 22 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 0.7.1-4mdk
- rebuild for new readline

* Thu Jan 06 2005 Frederic Crozat <fcrozat@mandrakesoft.com> 0.7.1-3mdk 
- Rebuild with latest howl

* Thu Dec 02 2004 Abel Cheung <deaddog@mandrake.org> 0.7.1-2mdk
- Fix BuildRequires
- Run scrollkeeper during post/postun

* Mon Nov 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.1-1mdk
- 0.7.1

* Wed Oct 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.7.0-1mdk
- 0.7.0

* Thu Jul 22 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6.2-1mdk
- 0.6.2

* Sat Jul 10 2004 Austin Acton <austin@mandrake.org> 0.6.1-1mdk
- 0.6.1
- configure 2.5

* Sat Jun 26 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.6-1mdk
- 0.6

* Wed Feb 18 2004 Austin Acton <austin@mandrake.org> 0.4-1mdk
- 0.4

* Mon Oct 27 2003 Austin Acton <aacton@yorku.ca> 0.3.1-1mdk
- 0.3.1

