%define bname qalculate

Summary:	A very versatile desktop calculator
Name:		qalculate-gtk
Version:	0.9.7
Release:	7
License:	GPLv2+
Group:		Office
Url:		http://qalculate.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/qalculate/%{name}-%{version}.tar.bz2
Patch1:		qalculate-gtk-0.9.6-fix-str-fmt.patch
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	rarian
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(libgnome-2.0)
BuildRequires:	pkgconfig(libqalculate) >= %{version}
Requires(pre):	rarian
Requires:	gnuplot
Requires:	wget

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
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/* 

##CAE rm symlink so both gtk and kde frontend are installable
rm -f %{buildroot}%{_bindir}/qalculate

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/glade/*.glade
%{_iconsdir}/hicolor/*/apps/%{name}.png

