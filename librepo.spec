#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : librepo
Version  : 1.9.2
Release  : 17
URL      : https://github.com/rpm-software-management/librepo/archive/1.9.2.tar.gz
Source0  : https://github.com/rpm-software-management/librepo/archive/1.9.2.tar.gz
Summary  : Repodata downloading library
Group    : Development/Tools
License  : LGPL-2.1 LGPL-2.1+
Requires: librepo-lib = %{version}-%{release}
Requires: librepo-license = %{version}-%{release}
Requires: librepo-python = %{version}-%{release}
Requires: librepo-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : check-dev
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : gpgme-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : python3-dev
BuildRequires : zlib-dev

%description
A library providing C and Python (libcURL like) API to downloading repository
metadata.

%package abi
Summary: abi components for the librepo package.
Group: Default

%description abi
abi components for the librepo package.


%package dev
Summary: dev components for the librepo package.
Group: Development
Requires: librepo-lib = %{version}-%{release}
Provides: librepo-devel = %{version}-%{release}

%description dev
dev components for the librepo package.


%package lib
Summary: lib components for the librepo package.
Group: Libraries
Requires: librepo-license = %{version}-%{release}

%description lib
lib components for the librepo package.


%package license
Summary: license components for the librepo package.
Group: Default

%description license
license components for the librepo package.


%package python
Summary: python components for the librepo package.
Group: Default
Requires: librepo-python3 = %{version}-%{release}

%description python
python components for the librepo package.


%package python3
Summary: python3 components for the librepo package.
Group: Default
Requires: python3-core

%description python3
python3 components for the librepo package.


%prep
%setup -q -n librepo-1.9.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1542316150
mkdir -p clr-build
pushd clr-build
%cmake .. -DPYTHON_DESIRED=3 -DWITH_TESTS=OFF
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1542316150
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/librepo
cp COPYING %{buildroot}/usr/share/package-licenses/librepo/COPYING
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files abi
%defattr(-,root,root,-)
/usr/share/abi/librepo.so.0.abi

%files dev
%defattr(-,root,root,-)
/usr/include/librepo/checksum.h
/usr/include/librepo/downloader.h
/usr/include/librepo/downloader_internal.h
/usr/include/librepo/downloadtarget.h
/usr/include/librepo/fastestmirror.h
/usr/include/librepo/gpg.h
/usr/include/librepo/handle.h
/usr/include/librepo/librepo.h
/usr/include/librepo/metadata_downloader.h
/usr/include/librepo/metalink.h
/usr/include/librepo/mirrorlist.h
/usr/include/librepo/package_downloader.h
/usr/include/librepo/rcodes.h
/usr/include/librepo/repoconf.h
/usr/include/librepo/repomd.h
/usr/include/librepo/repoutil_yum.h
/usr/include/librepo/result.h
/usr/include/librepo/types.h
/usr/include/librepo/url_substitution.h
/usr/include/librepo/util.h
/usr/include/librepo/version.h
/usr/include/librepo/xmlparser.h
/usr/include/librepo/yum.h
/usr/lib64/librepo.so
/usr/lib64/pkgconfig/librepo.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/librepo.so.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/librepo/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
