#
# spec file for package envoy-proxy
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


%define _dwz_low_mem_die_limit  20000000
%define _dwz_max_die_limit     100000000

%define src_install_dir /usr/src/%{name}

Name:           envoy-proxy
Version:        1.14.4
Release:        0
Summary:        L7 proxy and communication bus
License:        Apache-2.0
URL:            https://www.envoyproxy.io/
Source0:        %{name}-%{version}.tar.gz
# AUTOGENERATED BY obs-service-bazel_repositories
# vendor.tar.gz contains the following dependencies:
# - https://github.com/Cyan4973/xxHash/archive/v0.7.3.tar.gz
# - https://github.com/DataDog/dd-opentracing-cpp/archive/v1.1.3.tar.gz
# - https://github.com/LuaJIT/LuaJIT/archive/v2.1.0-beta3.tar.gz
# - https://github.com/Tencent/rapidjson/archive/dfbe1db9da455552f7a9ad5d2aea17dd9d832ac1.tar.gz
# - https://github.com/abseil/abseil-cpp/archive/06f0e767d13d4d68071c4fc51e25724e0fc8bc74.tar.gz
# - https://github.com/apache/kafka/archive/2.4.0.zip
# - https://github.com/bazelbuild/apple_support/releases/download/0.7.2/apple_support.0.7.2.tar.gz
# - https://github.com/bazelbuild/bazel-gazelle/releases/download/v0.19.1/bazel-gazelle-v0.19.1.tar.gz
# - https://github.com/bazelbuild/bazel-skylib/releases/download/0.9.0/bazel_skylib-0.9.0.tar.gz
# - https://github.com/bazelbuild/bazel-toolchains/releases/download/2.2.0/bazel-toolchains-2.2.0.tar.gz
# - https://github.com/bazelbuild/platforms/archive/9ded0f9c3144258dad27ad84628845bcd7ca6fe6.zip
# - https://github.com/bazelbuild/rules_apple/releases/download/0.19.0/rules_apple.0.19.0.tar.gz
# - https://github.com/bazelbuild/rules_cc/archive/818289e5613731ae410efb54218a4077fb9dbb03.tar.gz
# - https://github.com/bazelbuild/rules_foreign_cc/archive/7bc4be735b0560289f6b86ab6136ee25d20b65b7.tar.gz
# - https://github.com/bazelbuild/rules_go/releases/download/v0.23.3/rules_go-v0.23.3.tar.gz
# - https://github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip
# - https://github.com/bazelbuild/rules_proto/archive/2c0468366367d7ed97a1f702f9cd7155ab3f73c5.tar.gz
# - https://github.com/bazelbuild/rules_python/releases/download/0.0.1/rules_python-0.0.1.tar.gz
# - https://github.com/bazelbuild/rules_swift/releases/download/0.13.0/rules_swift.0.13.0.tar.gz
# - https://github.com/c-ares/c-ares/archive/d7e070e7283f822b1d2787903cce3615536c5610.tar.gz
# - https://github.com/census-instrumentation/opencensus-cpp/archive/04ed0211931f12b03c1a76b3907248ca4db7bc90.tar.gz
# - https://github.com/census-instrumentation/opencensus-proto/archive/be218fb6bd674af7519b1850cdf8410d8cbd48e8.tar.gz
# - https://github.com/circonus-labs/libcircllhist/archive/63a16dd6f2fc7bc841bb17ff92be8318df60e2e1.tar.gz
# - https://github.com/cncf/udpa/archive/e8cd3a4bb307e2c810cffff99f93e96e6d7fee85.tar.gz
# - https://github.com/envoyproxy/envoy-build-tools/archive/84ca08de00eedd0ba08e7d5551108d6f03f5d362.tar.gz
# - https://github.com/envoyproxy/protoc-gen-validate/archive/ab56c3dd1cf9b516b62c5087e1ec1471bd63631e.tar.gz
# - https://github.com/envoyproxy/sql-parser/archive/b14d010afd4313f2372a1cc96aa2327e674cc798.tar.gz
# - https://github.com/fmtlib/fmt/archive/6.0.0.tar.gz
# - https://github.com/gabime/spdlog/archive/v1.4.0.tar.gz
# - https://github.com/golang/protobuf/archive/v1.4.1.zip
# - https://github.com/golang/tools/archive/2bc93b1c0c88b2406b967fcd19a623d1ff9ea0cd.zip
# - https://github.com/google/cel-cpp/archive/80e1cca533190d537a780ad007e8db64164c582e.tar.gz
# - https://github.com/google/jwt_verify_lib/archive/40e2cc938f4bcd059a97dc6c73f59ecfa5a71bac.tar.gz
# - https://github.com/google/re2/archive/2020-03-03.tar.gz
# - https://github.com/googleapis/googleapis/archive/82944da21578a53b74e547774cf62ed31a05b841.tar.gz
# - https://github.com/gperftools/gperftools/archive/gperftools-2.7.90.tar.gz
# - https://github.com/grpc-ecosystem/grpc-httpjson-transcoding/archive/faf8af1e9788cd4385b94c8f85edab5ea5d4b2d6.tar.gz
# - https://github.com/grpc/grpc/archive/d8f4928fa779f6005a7fe55a176bdb373b0f910f.tar.gz
# - https://github.com/jbeder/yaml-cpp/archive/yaml-cpp-0.6.3.tar.gz
# - https://github.com/libevent/libevent/archive/0d7d85c2083f7a4c9efe01c061486f332b576d28.tar.gz
# - https://github.com/lightstep/lightstep-tracer-cpp/archive/3efe2372ee3d7c2138d6b26e542d757494a7938d.tar.gz
# - https://github.com/mirror/tclap/archive/tclap-1-2-1-release-final.tar.gz
# - https://github.com/moonjit/moonjit/archive/2.2.0.tar.gz
# - https://github.com/msgpack/msgpack-c/releases/download/cpp-3.2.1/msgpack-3.2.1.tar.gz
# - https://github.com/nodejs/http-parser/archive/v2.9.3.tar.gz
# - https://github.com/opentracing/opentracing-cpp/archive/v1.5.1.tar.gz
# - https://github.com/openzipkin/zipkin-api/archive/0.2.2.tar.gz
# - https://github.com/pallets/jinja/archive/2.10.3.tar.gz
# - https://github.com/pallets/markupsafe/archive/1.1.1.tar.gz
# - https://github.com/prometheus/client_model/archive/99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c.tar.gz
# - https://github.com/protocolbuffers/protobuf-go/archive/v1.22.0.zip
# - https://github.com/protocolbuffers/protobuf/releases/download/v3.10.1/protobuf-all-3.10.1.tar.gz
# - https://github.com/protocolbuffers/upb/archive/8a3ae1ef3e3e3f26b45dec735c5776737fc7247f.tar.gz
# - https://mirror.bazel.build/github.com/bazelbuild/platforms/archive/9ded0f9c3144258dad27ad84628845bcd7ca6fe6.zip
# - https://mirror.bazel.build/github.com/bazelbuild/rules_java/archive/7cf3cefd652008d0a64a419c34c13bdca6c8f178.zip
# - https://mirror.bazel.build/github.com/golang/protobuf/archive/v1.4.1.zip
# - https://mirror.bazel.build/github.com/golang/tools/archive/2bc93b1c0c88b2406b967fcd19a623d1ff9ea0cd.zip
# - https://mirror.bazel.build/github.com/protocolbuffers/protobuf-go/archive/v1.22.0.zip
Source1:        vendor.tar.gz
# END obs-service-bazel_repositories
Source100:      %{name}-rpmlintrc
Patch0:         0001-build-Use-Go-from-host.patch
Patch1:         0002-build-update-several-go-dependencies-11581.patch
Patch2:         0003-build-Add-explicit-requirement-on-rules_cc.patch
# AUTOGENERATED BY obs-service-bazel_repositories
Provides:       bundled(abseil-cpp) = 06f0e767d13d4d68071c4fc51e25724e0fc8bc74
Provides:       bundled(apple_support) = 0.7.2
Provides:       bundled(bazel-gazelle) = 0.19.1
Provides:       bundled(bazel-skylib) = 0.9.0
Provides:       bundled(bazel-toolchains) = 2.2.0
Provides:       bundled(c-ares) = d7e070e7283f822b1d2787903cce3615536c5610
Provides:       bundled(cel-cpp) = 80e1cca533190d537a780ad007e8db64164c582e
Provides:       bundled(client_model) = 99fa1f4be8e564e8a6b613da7fa6f46c9edafc6c
Provides:       bundled(dd-opentracing-cpp) = 1.1.3
Provides:       bundled(envoy-build-tools) = 84ca08de00eedd0ba08e7d5551108d6f03f5d362
Provides:       bundled(fmt) = 6.0.0
Provides:       bundled(googleapis) = 82944da21578a53b74e547774cf62ed31a05b841
Provides:       bundled(gperftools) = 2.7.90
Provides:       bundled(grpc) = d8f4928fa779f6005a7fe55a176bdb373b0f910f
Provides:       bundled(grpc-httpjson-transcoding) = faf8af1e9788cd4385b94c8f85edab5ea5d4b2d6
Provides:       bundled(http-parser) = 2.9.3
Provides:       bundled(jinja) = 2.10.3
Provides:       bundled(jwt_verify_lib) = 40e2cc938f4bcd059a97dc6c73f59ecfa5a71bac
Provides:       bundled(kafka) = 2.4.0
Provides:       bundled(libcircllhist) = 63a16dd6f2fc7bc841bb17ff92be8318df60e2e1
Provides:       bundled(libevent) = 0d7d85c2083f7a4c9efe01c061486f332b576d28
Provides:       bundled(lightstep-tracer-cpp) = 3efe2372ee3d7c2138d6b26e542d757494a7938d
Provides:       bundled(luajit) = 2.1.0
Provides:       bundled(markupsafe) = 1.1.1
Provides:       bundled(moonjit) = 2.2.0
Provides:       bundled(msgpack-c) = 3.2.1
Provides:       bundled(opencensus-cpp) = 04ed0211931f12b03c1a76b3907248ca4db7bc90
Provides:       bundled(opencensus-proto) = be218fb6bd674af7519b1850cdf8410d8cbd48e8
Provides:       bundled(opentracing-cpp) = 1.5.1
Provides:       bundled(platforms) = 9ded0f9c3144258dad27ad84628845bcd7ca6fe6
Provides:       bundled(protobuf) = 1.4.1
Provides:       bundled(protobuf) = 3.10.1
Provides:       bundled(protobuf-go) = 1.22.0
Provides:       bundled(protoc-gen-validate) = ab56c3dd1cf9b516b62c5087e1ec1471bd63631e
Provides:       bundled(rapidjson) = dfbe1db9da455552f7a9ad5d2aea17dd9d832ac1
Provides:       bundled(re2)
Provides:       bundled(rules_apple) = 0.19.0
Provides:       bundled(rules_cc) = 818289e5613731ae410efb54218a4077fb9dbb03
Provides:       bundled(rules_foreign_cc) = 7bc4be735b0560289f6b86ab6136ee25d20b65b7
Provides:       bundled(rules_go) = 0.23.3
Provides:       bundled(rules_java) = 7cf3cefd652008d0a64a419c34c13bdca6c8f178
Provides:       bundled(rules_proto) = 2c0468366367d7ed97a1f702f9cd7155ab3f73c5
Provides:       bundled(rules_python) = 0.0.1
Provides:       bundled(rules_swift) = 0.13.0
Provides:       bundled(spdlog) = 1.4.0
Provides:       bundled(sql-parser) = b14d010afd4313f2372a1cc96aa2327e674cc798
Provides:       bundled(tclap)
Provides:       bundled(tools) = 2bc93b1c0c88b2406b967fcd19a623d1ff9ea0cd
Provides:       bundled(udpa) = e8cd3a4bb307e2c810cffff99f93e96e6d7fee85
Provides:       bundled(upb) = 8a3ae1ef3e3e3f26b45dec735c5776737fc7247f
Provides:       bundled(xxhash) = 0.7.3
Provides:       bundled(yaml-cpp) = 0.6.3
Provides:       bundled(zipkin-api) = 0.2.2
# END obs-service-bazel_repositories
BuildRequires:  bazel
BuildRequires:  bazel-workspaces
BuildRequires:  boringssl-source
BuildRequires:  c-ares-devel
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  fmt-devel
BuildRequires:  gcc-c++
BuildRequires:  gcovr
BuildRequires:  git
BuildRequires:  golang-packaging
BuildRequires:  libcurl-devel
BuildRequires:  libnghttp2-devel
BuildRequires:  libtool
BuildRequires:  nghttp2-devel
BuildRequires:  ninja
BuildRequires:  python3
BuildRequires:  python3-Jinja2
BuildRequires:  python3-MarkupSafe
BuildRequires:  zlib-devel
BuildRequires:  golang(API) >= 1.12
BuildRequires:  pkgconfig(openssl)
ExcludeArch:    %ix86

%description
Envoy is an L7 proxy and communication bus designed for large modern service
oriented architectures.

%package source
Summary:        Source code of bazel-rules-cc

%description source
Envoy is an L7 proxy and communication bus designed for large modern service
oriented architectures.

This package contains source code of Envoy.

%prep
%autosetup -p1

# Prevent bundling curl, nghttp2 and zlib, don't use foreign_cc on them.
sed -i \
    -e "s|@envoy//bazel/foreign_cc:curl|@com_github_curl//:curl|" \
    -e 's|patches = \["@envoy//bazel/foreign_cc:nghttp2.patch"\]|# patches = \["@envoy//bazel/foreign_cc:nghttp2.patch"\]|g' \
    -e "s|@envoy//bazel/foreign_cc:nghttp2|@com_github_nghttp2_nghttp2//:all|" \
    -e "s|@envoy//bazel/foreign_cc:zlib|@zlib//:zlib|" \
    bazel/repositories.bzl

# Remove the script which requires /usr/bin/bash.exe and is meant to work only
# on Windows.
rm ci/windows_ci_steps.sh

# AUTOGENERATED BY obs-service-bazel_repositories
%setup -q -T -D -a 1
# END obs-service-bazel_repositories

%build
git config --global user.email you@example.com
git config --global user.name "Your Name"
git init
git add .
GIT_AUTHOR_DATE=2000-01-01T01:01:01 GIT_COMMITTER_DATE=2000-01-01T01:01:01 \
git commit -m "Dummy commit just to satisfy bazel" &> /dev/null

bazel build \
    -c dbg \
    --color=no \
    --copt="-fsigned-char" \
    --cxxopt="-fsigned-char" \
    --copt="-Wno-error=old-style-cast" \
    --cxxopt="-Wno-error=old-style-cast" \
    --copt="-Wno-unused-parameter" \
    --cxxopt="-Wno-unused-parameter" \
    --copt="-Wno-implicit-fallthrough" \
    --cxxopt="-Wno-implicit-fallthrough"\
    --copt="-Wno-return-type" \
    --cxxopt="-Wno-return-type" \
    --curses=no \
    --host_force_python=PY3 \
    --repository_cache=BAZEL_CACHE \
    --strip=never \
    --override_repository="boringssl=/usr/src/boringssl/" \
    --override_repository="com_github_curl=/usr/share/bazel-workspaces/curl" \
    --override_repository="com_github_nghttp2_nghttp2=/usr/share/bazel-workspaces/nghttp2" \
    --override_repository="zlib=/usr/share/bazel-workspaces/zlib" \
    --verbose_failures \
%ifarch ppc64le
    --local_cpu_resources=HOST_CPUS*.5 \
%endif
    //source/exe:envoy
bazel shutdown

%install
install -D -m0755 bazel-bin/source/exe/envoy-static %{buildroot}%{_bindir}/envoy-proxy

# Install sources
rm -rf .git bazel-*
mkdir -p %{buildroot}%{src_install_dir}
cp -r * %{buildroot}%{src_install_dir}
fdupes %{buildroot}%{src_install_dir}

%files
%license LICENSE
%doc README.md
%{_bindir}/envoy-proxy

%files source
%{src_install_dir}

%changelog
