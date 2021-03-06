#
# spec file for package perl-XML-SAX-Writer
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-XML-SAX-Writer
Version:        0.57
Release:        0
%define cpan_name XML-SAX-Writer
Summary:        SAX2 XML Writer
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/XML-SAX-Writer/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERIGRIN/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(XML::Filter::BufferText) >= 1.00
BuildRequires:  perl(XML::NamespaceSupport) >= 1.00
BuildRequires:  perl(XML::SAX::Exception) >= 1.01
Requires:       perl(XML::Filter::BufferText) >= 1.00
Requires:       perl(XML::NamespaceSupport) >= 1.00
Requires:       perl(XML::SAX::Exception) >= 1.01
%{perl_requires}

%description
SAX2 XML Writer

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README README.md
%license LICENSE

%changelog
