#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Unicode
%define		pnam	Map
Summary:	Perl Unicode::Map module
Summary(pl.UTF-8):   Moduł Perla Unicode::Map
Name:		perl-Unicode-Map
Version:	0.112
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	edaa8fc5ddf0e5d805e274283dd0625d
URL:		http://search.cpan.org/dist/Unicode-Map/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Startup
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unicode::Map module converts strings from and to Unicode UCS2 format.

%description -l pl.UTF-8
Moduł Unicode::Map konwertuje łańcuchy znaków na format Unicode UCS2 i
odwrotnie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
