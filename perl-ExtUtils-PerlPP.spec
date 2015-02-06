%define upstream_name	 ExtUtils-PerlPP
%define upstream_version 0.03

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	4

Summary:	%{upstream_name} module for perl
License:	GPL
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
%{upstream_name} module for perl

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/ExtUtils
%{_mandir}/*/*


%changelog
* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 407051
- rebuild using %%perl_convert_version

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.03-11mdv2009.0
+ Revision: 256861
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 0.03-9mdv2008.1
+ Revision: 135841
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 0.03-9mdv2007.0
+ Revision: 108539
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-ExtUtils-PerlPP

* Wed Feb 25 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.03-8mdk
- rebuild
- own dir
- remove packager tag, if you don't maitain it, you'll loose your name from spec !)

