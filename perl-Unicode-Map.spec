Summary: 	Perl Unicode-Map module
Summary(pl):	Modu³ Perla Unicode-Map
Name: 		perl-Unicode-Map
Version: 	0.105
Release: 	4
Copyright: 	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source: 	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Unicode/Unicode-Map-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
Requires:	perl-Startup
BuildRoot:      /tmp/%{name}-%{version}-root

%description
Unicode-Map module converts strings from and to Unicode UCS2 format.

%description -l pl
Modu³ Unicode-Map konwertuje ³añcuchy znaków na format Unicode UCS2
i odwrotnie.

%prep
%setup -q -n Unicode-Map-%{version}

%build
perl Makefile.PL
make CFLAGS="$RPM_OPT_FLAGS"

%clean 
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{perl_sitearch}/auto/Unicode/Map/*.so

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Unicode/Map/
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man[13]/* \
	README Changes

%files 
%defattr(644,root,root,755)
%doc {README,Changes}.gz
%attr(755,root,root) %{_bindir}/*

%{perl_sitearch}/Unicode/Map
%{perl_sitearch}/Unicode/Map.pm

%dir %{perl_sitearch}/auto/Unicode/Map
%{perl_sitearch}/auto/Unicode/Map/Map.bs
%{perl_sitearch}/auto/Unicode/Map/.packlist
%attr(755,root,root) %{perl_sitearch}/auto/Unicode/Map/Map.so

%{_mandir}/man[13]/*
