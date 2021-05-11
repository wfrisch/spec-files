#
# spec file for package python-coveralls
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
%define skip_python2 1
Name:           python-coveralls
Version:        2.1.1
Release:        0
Summary:        Module for showing coverage stats online via coverallsio
License:        MIT
URL:            https://github.com/coveralls-clients/coveralls-python
Source:         https://github.com/coveralls-clients/coveralls-python/archive/%{version}.tar.gz
BuildRequires:  %{python_module PyYAML >= 3.10}
BuildRequires:  %{python_module coverage >= 4.1}
BuildRequires:  %{python_module docopt >= 0.6.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 1.0.0}
BuildRequires:  %{python_module responses}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module sh >= 1.08}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-coverage >= 3.6
Requires:       python-docopt >= 0.6.1
Requires:       python-requests >= 1.0.0
Recommends:     python-PyYAML >= 3.10
BuildArch:      noarch
%ifpython2
Recommends:     python-urllib3
%endif
Requires(post):   update-alternatives
Requires(postun):  update-alternatives
%python_subpackages

%description
Coveralls.io is a service to publish coverage stats online.
This package provides integration with coverage.py in Python projects.

The module makes custom report for data generated by the coverage.py
package and sends it to the json API of the coveralls.io service. All
Python files in the coverage analysis are posted to this service,
along with coverage stats, so do not upload what you do not intend
to. (For private projects, there is Coveralls Pro.)

%prep
%setup -q -n coveralls-python-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/coveralls
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG="en_US.UTF8"
%pytest

%post
%python_install_alternative coveralls

%postun
%python_uninstall_alternative coveralls

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%python_alternative %{_bindir}/coveralls
%{python_sitelib}/*

%changelog