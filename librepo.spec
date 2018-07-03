#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : librepo
Version  : 1.8.1
Release  : 10
URL      : https://github.com/rpm-software-management/librepo/archive/1.8.1.tar.gz
Source0  : https://github.com/rpm-software-management/librepo/archive/1.8.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: librepo-python3
Requires: librepo-lib
Requires: librepo-python
BuildRequires : attr-dev
BuildRequires : check-dev
BuildRequires : cmake
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : gpgme-dev
BuildRequires : libassuan-dev
BuildRequires : libgpg-error-dev
BuildRequires : pkgconfig(expat)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : python3-dev
BuildRequires : zlib-dev

%description
# librepo
librepo - A library providing C and Python (libcURL like) API for downloading
linux repository metadata and packages

%package dev
Summary: dev components for the librepo package.
Group: Development
Requires: librepo-lib
Provides: librepo-devel

%description dev
dev components for the librepo package.


%package lib
Summary: lib components for the librepo package.
Group: Libraries

%description lib
lib components for the librepo package.


%package python
Summary: python components for the librepo package.
Group: Default
Requires: librepo-python3

%description python
python components for the librepo package.


%package python3
Summary: python3 components for the librepo package.
Group: Default
Requires: python3-core

%description python3
python3 components for the librepo package.


%prep
%setup -q -n librepo-1.8.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507584249
mkdir clr-build
pushd clr-build
cmake .. -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/usr -DBUILD_SHARED_LIBS:BOOL=ON -DLIB_INSTALL_DIR:PATH=/usr/lib64 -DCMAKE_AR=/usr/bin/gcc-ar -DLIB_SUFFIX=64 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DPYTHON_DESIRED=3 -DWITH_TESTS=OFF
make VERBOSE=1  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1507584249
rm -rf %{buildroot}
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
