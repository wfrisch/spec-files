#
# spec file for package ghc-reflection
#
# Copyright (c) 2020 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%global pkg_name reflection
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        2.1.6
Release:        0
Summary:        Reifies arbitrary terms into types that can be reflected back into terms
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-template-haskell-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-QuickCheck-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-hspec-devel
%endif

%description
This package addresses the /configuration problem/ which is propagating
configurations that are available at run-time, allowing multiple configurations
to coexist without resorting to mutable global variables or
'System.IO.Unsafe.unsafePerformIO'.

That package is an implementation of the ideas presented in the paper
"Functional Pearl: Implicit Configurations" by Oleg Kiselyov and Chung-chieh
Shan (<http://okmij.org/ftp/Haskell/tr-15-04.pdf original paper>).
However, the API has been streamlined to improve performance.

Austin Seipp's tutorial
<https://www.schoolofhaskell.com/user/thoughtpolice/using-reflection Reflecting
values to types and back> provides a summary of the approach taken by this
library, along with more motivating examples.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%check
%cabal_test

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc CHANGELOG.markdown README.markdown examples

%changelog
