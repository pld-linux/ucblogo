Name:		ucblogo
Version:	5.1
Release:	1
Summary:	Berkeley Logo interpreter
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://anarres.cs.berkeley.edu/pub/ucblogo/%{name}-%{version}.tar.gz
Patch0:		%{name}-signals.patch
Patch1:		%{name}-make.patch
Patch2:		%{name}-FHS.patch
# Patch2 NFY
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Berkeley Logo interpreter for Unix and X. Features *not* found in
Berkeley Logo include robotics, music, GUIs, animation, parallelism,
and multimedia. For those, buy a commercial version.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
autoconf
%configure --with-x
%{__make} "CFLAGS=%{rpmcflags}"

%install
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
#rm -rf $RPM_BUILD_ROOT
