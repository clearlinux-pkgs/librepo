#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: f032afc
#
Name     : librepo
Version  : 1.15.1
Release  : 57
URL      : https://github.com/rpm-software-management/librepo/archive/1.15.1/librepo-1.15.1.tar.gz
Source0  : https://github.com/rpm-software-management/librepo/archive/1.15.1/librepo-1.15.1.tar.gz
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
BuildRequires : pkg-config
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(gio-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libcrypto)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : python3-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
A library providing C and Python (libcURL like) API to downloading repository
metadata.

%package dev
Summary: dev components for the librepo package.
Group: Development
Requires: librepo-lib = %{version}-%{release}
Provides: librepo-devel = %{version}-%{release}
Requires: librepo = %{version}-%{release}

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
%setup -q -n librepo-1.15.1
cd %{_builddir}/librepo-1.15.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1697586204
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake .. -DENABLE_TESTS=OFF \
-DENABLE_DOCS=OFF \
-DWITH_ZCHUNK=OFF \
-DENABLE_PYTHON=ON
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1697586204
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/librepo
cp %{_builddir}/librepo-%{version}/COPYING %{buildroot}/usr/share/package-licenses/librepo/01a6b4bf79aca9b556822601186afab86e8c4fbf || :
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

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/librepo/01a6b4bf79aca9b556822601186afab86e8c4fbf

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
