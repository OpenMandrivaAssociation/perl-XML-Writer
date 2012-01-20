%define upstream_name 	 XML-Writer
%define upstream_version 0.612

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:	Module for writing XML documents
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(XML::Parser)

BuildArch:	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}
# temporary dep due to the perl-5.14 bump
BuildRequires:  perl-List-MoreUtils >= 0.320.0-4

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
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/XML/Writer*
%{_mandir}/*/*
