#
# spec file for package ghc-foldl
#
# Copyright (c) 2021 SUSE LLC
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


%global pkg_name foldl
%bcond_with tests
Name:           ghc-%{pkg_name}
Version:        1.4.11
Release:        0
Summary:        Composable, streaming, and efficient left folds
License:        BSD-3-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-bytestring-devel
BuildRequires:  ghc-comonad-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-contravariant-devel
BuildRequires:  ghc-hashable-devel
BuildRequires:  ghc-mwc-random-devel
BuildRequires:  ghc-primitive-devel
BuildRequires:  ghc-profunctors-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-semigroupoids-devel
BuildRequires:  ghc-text-devel
BuildRequires:  ghc-transformers-devel
BuildRequires:  ghc-unordered-containers-devel
BuildRequires:  ghc-vector-devel
ExcludeArch:    %{ix86}
%if %{with tests}
BuildRequires:  ghc-doctest-devel
%endif

%description
This library provides strict left folds that stream in constant memory, and you
can combine folds using 'Applicative' style to derive new folds.
Derived folds still traverse the container just once and are often as efficient
as hand-written folds.

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
%doc CHANGELOG.md README.md

%changelog
