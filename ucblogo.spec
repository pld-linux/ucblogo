Summary:	Berkeley LOGO interpreter
Summary(pl):	Interpreter Berkeley LOGO
Name:		ucblogo
Version:	5.3
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	ftp://anarres.cs.berkeley.edu/pub/ucblogo/%{name}-%{version}.tar.gz
# Source0-md5:	d10fb7ef5d36c38d54cfe5f2f3f7b5d6
Patch0:		%{name}-signals.patch
Patch1:		%{name}-make.patch
BuildRequires:	autoconf
BuildRequires:	XFree86-devel
BuildRequires:	ncurses-devel
BuildRequires:	emacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Berkeley Logo interpreter for Unix and X. Features *not* found in
Berkeley Logo include robotics, music, GUIs, animation, parallelism,
and multimedia. For those, buy a commercial version.

%description -l pl
Interpreter Berkeley Logo dla Unika i X. Mo¿liwo¶ci, których nie ma
Berkeley Logo to m.in. robotyka, muzyka, GUI, animacje, równoleg³o¶æ,
multimedia. Dla nich kup komercyjn± wersjê.

%package examples
Summary:	Example LOGO programs for the Berkeley LOGO interpreter
Summary(pl):	Przyk³ady programów w LOGO dla interpretera Berkeley LOGO
Group:		Development/Languages
Requires:	%{name}

%description examples
This package contains example LOGO programs, eg solitaire, poker, plot
and many others.

%description examples -l pl
Ten pakiet zawiera przyk³adowe programy w LOGO, m.in. pasjans, poker,
plot i wiele innych.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__autoconf}
%configure --with-x
%{__make} "CFLAGS=%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/logo
install csls/* $RPM_BUILD_ROOT%{_examplesdir}/logo

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_infodir}/*
%dir %{_datadir}/logo
%{_datadir}/logo/*
%doc README

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/logo
%{_examplesdir}/logo/*
