%define modname	XML-Writer
%define modver	0.612

Summary:	Module for writing XML documents
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	15
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)

%description
XML::Writer is a simple Perl module for writing XML documents:	it
takes care of constructing markup and escaping data correctly, and by
default, it also performs a significant amount of well-formedness
checking on the output, to make certain (for example) that start and
end tags match, that there is exactly one document element, and that
there are not duplicate attribute names.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*

