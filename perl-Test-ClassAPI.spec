%define upstream_name    Test-ClassAPI
%define upstream_version 1.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Test::ClassAPI - Provides basic first-pass API testing for large class trees
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl(Class::Inspector) >= 1.06
BuildRequires:	perl(Config::Tiny) >= 2.0
BuildRequires:	perl(Params::Util)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
For many APIs with large numbers of classes, it can be very useful to be
able to do a quick once-over to make sure that classes, methods, and
inheritance is correct, before doing more comprehensive testing. This
module aims to provide such a capability.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Test/ClassAPI.pm
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-4mdv2012.0
+ Revision: 765674
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.60.0-2
+ Revision: 676775
- rebuild

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 1.60.0-1mdv2010.0
+ Revision: 405546
- rebuild using %%perl_convert_version

* Wed Jul 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.06-1mdv2010.0
+ Revision: 396224
- update to new version 1.06

* Fri Jul 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.05-1mdv2009.0
+ Revision: 233663
- update to new version 1.05

* Fri Dec 21 2007 Olivier Blin <blino@mandriva.org> 1.04-1mdv2008.1
+ Revision: 136360
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu May 03 2007 Olivier Thauvin <nanardon@mandriva.org> 1.04-1mdv2008.0
+ Revision: 22121
- 1.04


* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 1.02-2mdk
- Fix SPEC according to Perl Policy
	- BuildRequires
	- Source URL
- use mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.02-1mdk
- initial Mandriva package

