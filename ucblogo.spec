Summary:	Berkeley LOGO interpreter
Summary(pl.UTF-8):	Interpreter Berkeley LOGO
Name:		ucblogo
Version:	6.2.4
Release:	1
License:	GPL v2+
Group:		Development/Languages
Source0:	https://github.com/jrincayc/ucblogo-code/releases/download/version_%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d7fb4d409be5349199e0ce377902f233
URL:		http://www.cs.berkeley.edu/~bh/logo.html
BuildRequires:	ncurses-devel
BuildRequires:	wxGTK3-unicode-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Berkeley Logo interpreter for Unix and X. Features *not* found in
Berkeley Logo include robotics, music, GUIs, animation, parallelism,
and multimedia. For those, buy a commercial version.

%description -l pl.UTF-8
Interpreter Berkeley Logo dla Unika i X. Możliwości, których nie ma
Berkeley Logo to m.in. robotyka, muzyka, GUI, animacje, równoległość,
multimedia. Dla nich kup komercyjną wersję.

%package examples
Summary:	Example LOGO programs for the Berkeley LOGO interpreter
Summary(pl.UTF-8):	Przykłady programów w LOGO dla interpretera Berkeley LOGO
Group:		Development/Languages
Requires:	%{name}

%description examples
This package contains example LOGO programs, eg solitaire, poker, plot
and many others.

%description examples -l pl.UTF-8
Ten pakiet zawiera przykładowe programy w LOGO, m.in. pasjans, poker,
plot i wiele innych.

%prep
%setup -q

%build
%configure \
	--enable-x11 \
	--with-wx-configh=%{_bindir}/wx-gtk3-unicode-config

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -p csls/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/ucblogo

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README.md TODO changes.txt newtermnotes plm usermanual
%doc docs/ucblogo.pdf
%attr(755,root,root) %{_bindir}/ucblogo
%{_infodir}/ucblogo.info*
%{_datadir}/ucblogo
%{_desktopdir}/ucblogo.desktop
%{_iconsdir}/hicolor/*x*/apps/ucblogo.png
%{_mandir}/man1/ucblogo.1*
%{_pixmapsdir}/ucblogo.xpm

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
