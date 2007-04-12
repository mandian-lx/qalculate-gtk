%define bname   qalculate
%define name    qalculate-gtk
%define version 0.9.4
%define release %mkrel 3

Name:       %{name}
Summary:    A very versatile desktop calculator
Version:    %{version}
Release:    %{release}
Source:     http://prdownloads.sourceforge.net/qalculate/%{name}-%{version}.tar.bz2
URL:        http://qalculate.sourceforge.net/
License:    GPL
Group:      Office
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  libqalculate-devel >= %{version} 
BuildRequires:  libglade2.0-devel
BuildRequires:  gtk+2-devel
BuildRequires:  cln-devel
BuildRequires:  readline-devel
BuildRequires:  ncurses-devel
BuildRequires:  ImageMagick
BuildRequires:  perl(XML::Parser)
BuildRequires:  scrollkeeper
BuildRequires:  intltool
BuildRequires:  desktop-file-utils
Requires(pre): scrollkeeper
Requires:   gnuplot
Requires:   wget
Obsoletes:     qalculate
Provides:       qalculate

%description
Qalculate! is a modern multi-purpose desktop calculator for GNU/Linux. It is
small and simple to use but with much power and versatility underneath.
Features include customizable functions, units, arbitrary precision, plotting,
and a graphical interface that uses a one-line fault-tolerant expression entry 
(although it supports optional traditional buttons). 
This package provides the GTK frontend.

 
%prep
%setup -q 
 
%build
libtoolize --copy --force 
aclocal-1.9
autoconf-2.5x
automake-1.9
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std 

#menu
mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}): \
command="%{name}" \
icon="%{name}.png" \
needs="x11" \
title="Qalculate!" \
longtitle="Versatile desktop calculator" \
section="Office/Accessories" \
xdg="true"
EOF

#icons 
convert -size 48x48 data/%{bname}.png $RPM_BUILD_ROOT/%{_liconsdir}/%{name}.png 
convert -size 32x32 data/%{bname}.png $RPM_BUILD_ROOT/%{_iconsdir}/%{name}.png 
convert -size 16x16 data/%{bname}.png $RPM_BUILD_ROOT/%{_miconsdir}/%{name}.png

desktop-file-install --vendor="" \
--remove-category="Application" \
--add-category="GTK" \
--add-category="Calculator" \
--add-category="X-MandrivaLinux-Office;Utility" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/* 

##CAE rm symlink so both gtk and kde frontend are installable
rm -f $RPM_BUILD_ROOT%{_bindir}/qalculate

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q; fi 

%postun
%clean_menus
if [ -x %{_bindir}/scrollkeeper-update ]; then %{_bindir}/scrollkeeper-update -q; fi

 
%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*
%dir %{_datadir}/gnome/help/%{name}
%{_datadir}/gnome/help/%{name}/C/*
%{_datadir}/omf/%{name}
%{_datadir}/pixmaps/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade/*.glade
%{_menudir}/%{name}
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

 



