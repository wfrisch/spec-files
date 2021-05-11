#
# spec file for package ghc-indexed-traversable
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


%global pkg_name indexed-traversable
Name:           ghc-%{pkg_name}
Version:        0.1.1
Release:        0
Summary:        FunctorWithIndex, FoldableWithIndex, TraversableWithIndex
License:        BSD-2-Clause
URL:            https://hackage.haskell.org/package/%{pkg_name}
Source0:        https://hackage.haskell.org/package/%{pkg_name}-%{version}/%{pkg_name}-%{version}.tar.gz
BuildRequires:  ghc-Cabal-devel
BuildRequires:  ghc-array-devel
BuildRequires:  ghc-containers-devel
BuildRequires:  ghc-rpm-macros
BuildRequires:  ghc-transformers-devel
ExcludeArch:    %{ix86}

%description
This package provides three useful generalizations:

' class Functor f => FunctorWithIndex i f | f -> i where imap :: (i -> a -> b)
-> f a -> f b '

' class Foldable f => FoldableWithIndex i f | f -> i where ifoldMap :: Monoid m
=> (i -> a -> m) -> f a -> m '

' class (FunctorWithIndex i t, FoldableWithIndex i t, Traversable t) =>
TraversableWithIndex i t | t -> i where itraverse :: Applicative f => (i -> a
-> f b) -> t a -> f (t b) '

This package contains instances for types in GHC boot libraries. For some
additional instances see
[indexed-traversable-instances](https://hackage.haskell.org/package/indexed-traversable-instances).

The [keys](https://hackage.haskell.org/package/keys) package provides similar
functionality, but uses (associated) 'TypeFamilies' instead of
'FunctionalDependencies'.

%package devel
Summary:        Haskell %{pkg_name} library development files
Requires:       %{name} = %{version}-%{release}
Requires:       ghc-compiler = %{ghc_version}
Requires(post): ghc-compiler = %{ghc_version}
Requires(postun): ghc-compiler = %{ghc_version}

%description devel
This package provides the Haskell %{pkg_name} library development
files.

%prep
%autosetup -n %{pkg_name}-%{version}

%build
%ghc_lib_build

%install
%ghc_lib_install

%post devel
%ghc_pkg_recache

%postun devel
%ghc_pkg_recache

%files -f %{name}.files
%license LICENSE

%files devel -f %{name}-devel.files
%doc Changelog.md

%changelog
