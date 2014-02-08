%define upstream_name 	 XML-Writer
%define upstream_version 0.612

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	8

Summary:	Module for writing XML documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)

BuildArch:	noarch

%description
XML::Writer is a simple Perl module for writing XML documents: it
takes care of constructing markup and escaping data correctly, and by
default, it also performs a significant amount of well-formedness
checking on the output, to make certain (for example) that start and
end tags match, that there is exactly one document element, and that
there are not duplicate attribute names.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README Changes
%{perl_vendorlib}/XML/Writer*
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.612.0-5mdv2012.0
+ Revision: 765857
- rebuilt for perl-5.14.2
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 0.612.0-3
+ Revision: 763289
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.612.0-2
+ Revision: 667461
- mass rebuild

* Tue Aug 17 2010 Jérôme Quelin <jquelin@mandriva.org> 0.612.0-1mdv2011.0
+ Revision: 570747
- update to 0.612

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.611.0-1mdv2011.0
+ Revision: 539089
- update to 0.611

* Mon Mar 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.610.0-1mdv2010.1
+ Revision: 528763
- update to 0.610

* Tue Mar 23 2010 Jérôme Quelin <jquelin@mandriva.org> 0.607.0-1mdv2010.1
+ Revision: 526820
- update to 0.607

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.606-2mdv2010.0
+ Revision: 426601
- rebuild

* Mon Dec 08 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.606-1mdv2009.1
+ Revision: 311965
- update to new version 0.606

* Tue Dec 02 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.605-1mdv2009.1
+ Revision: 309328
- update to new version 0.605

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.604-2mdv2009.0
+ Revision: 224675
- rebuild

* Tue Feb 26 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.604-1mdv2008.1
+ Revision: 175317
- update to new version 0.604

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - simplify buildrequires

* Sun Jul 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.603-1mdv2008.0
+ Revision: 46720
- update to new version 0.603


* Mon Dec 11 2006 Olivier Thauvin <nanardon@mandriva.org> 0.602-1mdv2007.0
+ Revision: 94582
- 0.602
- Import perl-XML-Writer

* Sat Jul 02 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.600-1mdk
- 0.600

* Fri May 27 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.545-1mdk
- 0.545

* Tue Apr 26 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.531-1mdk
- 0.531

* Wed Feb 09 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.530-1mdk
- 0.530
- make tests

* Tue Nov 09 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.520-1mdk
- 0.520

* Thu May 27 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.510-1mdk
- 0.510

* Tue Apr 13 2004 Stefan van der Eijk <stefan@eijk.nu> 0.500-1mdk
- 0.500

* Sun Jan 11 2004 Stefan van der Eijk <stefan@eijk.nu> 0.4.1-1mdk
- 0.4.1

