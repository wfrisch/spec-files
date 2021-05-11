#
# spec file for package python-ijson
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-ijson
Version:        3.0
Release:        0
Summary:        Iterative JSON parser with a standard Python iterator interface
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ICRAR/ijson
Source:         https://files.pythonhosted.org/packages/source/i/ijson/ijson-%{version}.tar.gz
# https://github.com/ICRAR/ijson/pull/26
Source1:        https://raw.githubusercontent.com/ICRAR/ijson/master/tests_asyncio.py
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-asyncio
BuildRequires:  pkgconfig(yajl)
%python_subpackages

%description
Iterative JSON parser with a standard Python iterator interface.

%prep
%setup -q -n ijson-%{version}
cp %{SOURCE1} .

%build
export CFLAGS="%{optflags}"
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
%python_exec tests.py

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitearch}/*

%changelog
