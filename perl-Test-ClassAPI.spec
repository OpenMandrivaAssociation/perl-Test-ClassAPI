%define real_name Test-ClassAPI

Summary:	Test::ClassAPI - Provides basic first-pass API testing for large class trees
Name:		perl-%{real_name}
Version:	1.06
Release: %mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Test/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(Class::Inspector) >= 1.06
BuildRequires:	perl(Config::Tiny) >= 2.0
Buildrequires:  perl(Params::Util)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
For many APIs with large numbers of classes, it can be very useful to be
able to do a quick once-over to make sure that classes, methods, and
inheritance is correct, before doing more comprehensive testing. This
module aims to provide such a capability.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Test/ClassAPI.pm
%{_mandir}/*/*

