%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	Map
Summary:	Perl Unicode::Map module
Summary(pl):	Modu³ Perla Unicode::Map
Name:		perl-Unicode-Map
Version:	0.112
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	edaa8fc5ddf0e5d805e274283dd0625d
BuildRequires:	perl-devel >= 5.6
BuildRequires:	perl-Startup
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::Map module converts strings from and to Unicode UCS2 format.

%description -l pl
Modu³ Unicode::Map konwertuje ³añcuchy znaków na format Unicode UCS2 i
odwrotnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/*
%{perl_vendorarch}/Unicode/Map
%{perl_vendorarch}/Unicode/Map.pm
%dir %{perl_vendorarch}/auto/Unicode/Map
%{perl_vendorarch}/auto/Unicode/Map/Map.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Unicode/Map/Map.so
%{_mandir}/man[13]/*
