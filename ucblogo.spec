Name:		ucblogo
Version:	5.1
Release:	1
Summary:	Berkeley LOGO interpreter
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://anarres.cs.berkeley.edu/pub/ucblogo/%{name}-%{version}.tar.gz
Patch0:		%{name}-signals.patch
Patch1:		%{name}-makefile.patch
Buildrequires:	autoconf
Buildrequires:	XFree86-devel
Buildrequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Berkeley Logo interpreter for Unix and X. Features *not* found in
Berkeley Logo include robotics, music, GUIs, animation, parallelism,
and multimedia. For those, buy a commercial version.

%package examples
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Summary:	Example LOGO programs for the Berkeley LOGO interpreter
Requires:	%{name}

%description examples
This package contains example LOGO programs, eg solitaire, poker, plot
and many others.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
autoconf
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

%files examples
%defattr(644,root,root,755)
%dir %{_examplesdir}/logo
%{_examplesdir}/logo/*
