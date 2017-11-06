%define bname qalculate

Summary:	A very versatile desktop calculator
Name:		%{bname}-gtk
Version:	2.1.0
Release:	1
License:	GPLv2+
Group:		Office
Url:		https://qalculate.github.io/
Source0:	https://github.com/Qalculate/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	rarian
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(libqalculate) >= %{version}
Requires(pre):	rarian
Requires:	gnuplot

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is small
and simple to use but with much power and versatility underneath

Features include customizable functions, units, arbitrary precision,
plotting, and a user-friendly interface (GTK+ and CLI).

This package provides the GTK+ frontend.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%doc doc/html
%{_bindir}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make

%install
%makeinstall_std

#icons 
for i in 16 32 64 48 64 128 256 512
do
	install -dm 755 %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps
	convert -size ${i}x${i} data/%{bname}.png %{buildroot}%{_iconsdir}/hicolor/${i}x${i}/apps/%{name}.png 
done

# desktop
desktop-file-install \
	--remove-category="Application" \
	--add-category="GTK" \
	--add-category="Calculator" \
	--set-icon="%{name}" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/* 

# locales
%find_lang %{name} --with-gnome

