#
# spec file for package perl-ExtUtils-Config
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-ExtUtils-Config
Version:        0.008
Release:        0
%define cpan_name ExtUtils-Config
Summary:        A wrapper for perl's configuration
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/ExtUtils-Config/
Source:         http://www.cpan.org/authors/id/L/LE/LEONT/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Test::More) >= 0.88
%{perl_requires}

%description
ExtUtils::Config is an abstraction around the %Config hash. By itself it is
not a particularly interesting module by any measure, however it ties
together a family of modern toolchain modules.

%prep
%setup -q -n %{cpan_name}-%{version}

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
%doc Changes LICENSE README

%changelog
