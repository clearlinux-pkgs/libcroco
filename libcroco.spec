#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
Name     : libcroco
Version  : 0.6.13
Release  : 25
URL      : https://download.gnome.org/sources/libcroco/0.6/libcroco-0.6.13.tar.xz
Source0  : https://download.gnome.org/sources/libcroco/0.6/libcroco-0.6.13.tar.xz
Summary  : a CSS2 Parsing and manipulation Library in C.
Group    : Development/Tools
License  : LGPL-2.0
Requires: libcroco-bin = %{version}-%{release}
Requires: libcroco-lib = %{version}-%{release}
Requires: libcroco-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : buildreq-gnome
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxml2-dev32
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32libxml-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libxml-2.0)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: cve-2017-8834.nopatch
Patch2: cve-2017-8871.nopatch
Patch3: CVE-2020-12825.patch

%description
libcroco is a standalone css2 parsing library.
It provides a low level event driven SAC like api
and a css object model like api.

%package bin
Summary: bin components for the libcroco package.
Group: Binaries
Requires: libcroco-license = %{version}-%{release}

%description bin
bin components for the libcroco package.


%package dev
Summary: dev components for the libcroco package.
Group: Development
Requires: libcroco-lib = %{version}-%{release}
Requires: libcroco-bin = %{version}-%{release}
Provides: libcroco-devel = %{version}-%{release}
Requires: libcroco = %{version}-%{release}

%description dev
dev components for the libcroco package.


%package dev32
Summary: dev32 components for the libcroco package.
Group: Default
Requires: libcroco-lib32 = %{version}-%{release}
Requires: libcroco-bin = %{version}-%{release}
Requires: libcroco-dev = %{version}-%{release}

%description dev32
dev32 components for the libcroco package.


%package doc
Summary: doc components for the libcroco package.
Group: Documentation

%description doc
doc components for the libcroco package.


%package lib
Summary: lib components for the libcroco package.
Group: Libraries
Requires: libcroco-license = %{version}-%{release}

%description lib
lib components for the libcroco package.


%package lib32
Summary: lib32 components for the libcroco package.
Group: Default
Requires: libcroco-license = %{version}-%{release}

%description lib32
lib32 components for the libcroco package.


%package license
Summary: license components for the libcroco package.
Group: Default

%description license
license components for the libcroco package.


%prep
%setup -q -n libcroco-0.6.13
cd %{_builddir}/libcroco-0.6.13
%patch3 -p1
pushd ..
cp -a libcroco-0.6.13 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1680036989
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -O3 -Os -fdata-sections -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -ffunction-sections -flto=auto -fno-semantic-interposition -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1680036989
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libcroco
cp %{_builddir}/libcroco-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libcroco/5fb362ef1680e635fe5fb212b55eef4db9ead48f || :
cp %{_builddir}/libcroco-%{version}/COPYING.LIB %{buildroot}/usr/share/package-licenses/libcroco/5fb362ef1680e635fe5fb212b55eef4db9ead48f || :
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/croco-0.6-config
/usr/bin/csslint-0.6

%files dev
%defattr(-,root,root,-)
/usr/include/libcroco-0.6/libcroco/cr-additional-sel.h
/usr/include/libcroco-0.6/libcroco/cr-attr-sel.h
/usr/include/libcroco-0.6/libcroco/cr-cascade.h
/usr/include/libcroco-0.6/libcroco/cr-declaration.h
/usr/include/libcroco-0.6/libcroco/cr-doc-handler.h
/usr/include/libcroco-0.6/libcroco/cr-enc-handler.h
/usr/include/libcroco-0.6/libcroco/cr-fonts.h
/usr/include/libcroco-0.6/libcroco/cr-input.h
/usr/include/libcroco-0.6/libcroco/cr-num.h
/usr/include/libcroco-0.6/libcroco/cr-om-parser.h
/usr/include/libcroco-0.6/libcroco/cr-parser.h
/usr/include/libcroco-0.6/libcroco/cr-parsing-location.h
/usr/include/libcroco-0.6/libcroco/cr-prop-list.h
/usr/include/libcroco-0.6/libcroco/cr-pseudo.h
/usr/include/libcroco-0.6/libcroco/cr-rgb.h
/usr/include/libcroco-0.6/libcroco/cr-sel-eng.h
/usr/include/libcroco-0.6/libcroco/cr-selector.h
/usr/include/libcroco-0.6/libcroco/cr-simple-sel.h
/usr/include/libcroco-0.6/libcroco/cr-statement.h
/usr/include/libcroco-0.6/libcroco/cr-string.h
/usr/include/libcroco-0.6/libcroco/cr-style.h
/usr/include/libcroco-0.6/libcroco/cr-stylesheet.h
/usr/include/libcroco-0.6/libcroco/cr-term.h
/usr/include/libcroco-0.6/libcroco/cr-tknzr.h
/usr/include/libcroco-0.6/libcroco/cr-token.h
/usr/include/libcroco-0.6/libcroco/cr-utils.h
/usr/include/libcroco-0.6/libcroco/libcroco-config.h
/usr/include/libcroco-0.6/libcroco/libcroco.h
/usr/lib64/libcroco-0.6.so
/usr/lib64/pkgconfig/libcroco-0.6.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libcroco-0.6.so
/usr/lib32/pkgconfig/32libcroco-0.6.pc
/usr/lib32/pkgconfig/libcroco-0.6.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/gtk-doc/html/libcroco/ch01.html
/usr/share/gtk-doc/html/libcroco/home.png
/usr/share/gtk-doc/html/libcroco/index.html
/usr/share/gtk-doc/html/libcroco/left-insensitive.png
/usr/share/gtk-doc/html/libcroco/left.png
/usr/share/gtk-doc/html/libcroco/libcroco-cr-additional-sel.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-attr-sel.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-cascade.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-declaration.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-doc-handler.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-enc-handler.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-fonts.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-input.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-num.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-om-parser.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-parser.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-parsing-location.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-prop-list.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-pseudo.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-rgb.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-sel-eng.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-selector.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-simple-sel.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-statement.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-string.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-style.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-stylesheet.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-term.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-tknzr.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-token.html
/usr/share/gtk-doc/html/libcroco/libcroco-cr-utils.html
/usr/share/gtk-doc/html/libcroco/libcroco-libcroco-config.html
/usr/share/gtk-doc/html/libcroco/libcroco.devhelp2
/usr/share/gtk-doc/html/libcroco/right-insensitive.png
/usr/share/gtk-doc/html/libcroco/right.png
/usr/share/gtk-doc/html/libcroco/style.css
/usr/share/gtk-doc/html/libcroco/up-insensitive.png
/usr/share/gtk-doc/html/libcroco/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/libcroco-0.6.so.3
/usr/lib64/libcroco-0.6.so.3.0.1

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libcroco-0.6.so.3
/usr/lib32/libcroco-0.6.so.3.0.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libcroco/5fb362ef1680e635fe5fb212b55eef4db9ead48f
