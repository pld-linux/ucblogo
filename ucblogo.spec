Summary:	Berkeley LOGO interpreter
Summary(pl.UTF-8):	Interpreter Berkeley LOGO
Name:		ucblogo
Version:	6.0
Release:	2
License:	GPL v2+
Group:		Development/Languages
Source0:	ftp://anarres.cs.berkeley.edu/pub/ucblogo/%{name}-%{version}.tar.gz
# Source0-md5:	36a56765b18136c817880c5381af196b
Patch0:		%{name}-signals.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-wx.patch
Patch3:		%{name}-lp64.patch
URL:		http://www.cs.berkeley.edu/~bh/logo.html
BuildRequires:	ncurses-devel
BuildRequires:	wxGTK2-unicode-devel
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%{__rm} -r csls/CVS

%build
# configure is manually hacked for wx support
export ac_cv_lib_termcap_tgetstr=no
export ac_cv_lib_termlib_tgetstr=no
%configure2_13 \
	--with-x \
	--wx-config_path=%{_bindir}/wx-gtk2-unicode-config \
	--wx-enable
%{__make} \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install csls/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_datadir}/logo/docs/usermanual.{ps,texi}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc README TODO changes.txt newtermnotes plm usermanual
%attr(755,root,root) %{_bindir}/logo
%{_infodir}/ucblogo.info*
%{_datadir}/logo

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
