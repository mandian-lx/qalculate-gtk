%define bname qalculate

Summary:	A very versatile desktop calculator
Name:		qalculate-gtk
Version:	0.9.8
Release:	10
License:	GPLv2+
Group:		Office
Url:		https://qalculate.github.io/
Source0:        https://github.com/Qalculate/%{name}/archive/v%{version}.tar.gz
Patch0:		qalculate-gtk-0.9.8-fix-str-fmt.patch
BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	rarian
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(cln)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libqalculate) >= %{version}
Requires(pre):	rarian
Requires:	gnuplot
Requires:	wget

%description
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is small
and simple to use but with much power and versatility underneath
Features include customizable functions, units, arbitrary precision,
plotting, and a user-friendly interface (GTK+ and CLI).

This package provides the GTK+ frontend.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/*
%{_datadir}/pixmaps/*.png
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/ui
%{_datadir}/%{name}/ui/*.ui
%{_iconsdir}/hicolor/*/apps/%{name}.png

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p1 -b .str

%build
autoreconf -fiv
%configure
%make

%install
%make_install

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

%find_lang %{name} --with-gnome

