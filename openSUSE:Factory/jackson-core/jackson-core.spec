#
# spec file for package jackson-core
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


Name:           jackson-core
Version:        2.10.5
Release:        0
Summary:        Core part of Jackson
License:        Apache-2.0
Group:          Development/Libraries/Java
URL:            https://github.com/FasterXML/jackson-core/
Source0:        https://github.com/FasterXML/jackson-core/archive/%{name}-%{version}.tar.gz
Source1:        %{name}-build.xml
BuildRequires:  ant
BuildRequires:  fdupes
BuildRequires:  java-devel >= 1.6
BuildRequires:  javapackages-local
BuildArch:      noarch

%description
Core part of Jackson that defines Streaming API as well
as basic shared abstractions.

%package javadoc
Summary:        Javadoc for %{name}
Group:          Development/Libraries/Java

%description javadoc
This package contains API documentation for %{name}.

%prep
%setup -q -n %{name}-%{name}-%{version}
cp %{SOURCE1} build.xml
mkdir -p lib

# Remove section unnecessary for ant build
%pom_remove_parent
%pom_xpath_remove pom:project/pom:build

cp -p src/main/resources/META-INF/LICENSE .
cp -p src/main/resources/META-INF/NOTICE .
sed -i 's/\r//' LICENSE NOTICE

%build
%{ant} -Dtest.skip=true package javadoc

%install
install -dm 0755 %{buildroot}%{_javadir}
install -pm 0644 target/%{name}-%{version}.jar %{buildroot}%{_javadir}/%{name}.jar

install -dm 0755 %{buildroot}%{_mavenpomdir}
install -pm 0644 pom.xml %{buildroot}%{_mavenpomdir}/%{name}.pom
%add_maven_depmap %{name}.pom %{name}.jar

install -dm 0755 %{buildroot}%{_javadocdir}
cp -r target/site/apidocs %{buildroot}%{_javadocdir}/%{name}
%fdupes -s %{buildroot}%{_javadocdir}

%files -f .mfiles
%doc README.md release-notes/*
%license LICENSE

%files javadoc
%{_javadocdir}/%{name}
%license LICENSE

%changelog
