#
# spec file for package rubygem-prawn-core
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-prawn-core
Version:        0.8.4
Release:        0
%define mod_name prawn-core
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  %{ruby}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  %{rubygem rdoc > 3.10}
Url:            http://prawn.majesticseacreature.com
Source:         https://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A fast and nimble PDF generator for Ruby
License:        Ruby or GPL-2.0-or-later
Group:          Development/Languages/Ruby

%description
Prawn is a fast, tiny, and nimble PDF generator for Ruby.

%prep

%build

%install
%gem_install \
  --doc-files="COPYING LICENSE README" \
  -f
# MANUAL
%fdupes %{buildroot}/%{gem_base}
# /MANUAL


%gem_packages

%changelog
