%include	/usr/lib/rpm/macros.perl
%define	pdir	Unicode
%define	pnam	Map
Summary:	Perl Unicode-Map module
Summary(pl):	Modu³ Perla Unicode-Map
Name:		perl-Unicode-Map
Version:	0.110
Release:	5
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Startup
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode-Map module converts strings from and to Unicode UCS2 format.

%description -l pl
Modu³ Unicode-Map konwertuje ³añcuchy znaków na format Unicode UCS2 i
odwrotnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{perl_sitearch}/Unicode/Map
%{perl_sitearch}/Unicode/Map.pm
%dir %{perl_sitearch}/auto/Unicode/Map
%{perl_sitearch}/auto/Unicode/Map/Map.bs
%attr(755,root,root) %{perl_sitearch}/auto/Unicode/Map/Map.so
%{_mandir}/man[13]/*
