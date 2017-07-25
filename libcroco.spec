#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libcroco
Version  : 0.6.12
Release  : 10
URL      : https://download.gnome.org/sources/libcroco/0.6/libcroco-0.6.12.tar.xz
Source0  : https://download.gnome.org/sources/libcroco/0.6/libcroco-0.6.12.tar.xz
Summary  : a CSS2 Parsing and manipulation Library in C.
Group    : Development/Tools
License  : LGPL-2.0
Requires: libcroco-bin
Requires: libcroco-lib
Requires: libcroco-doc
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
BuildRequires : pkgconfig(32glib-2.0)
BuildRequires : pkgconfig(32libxml-2.0)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(libxml-2.0)
Patch1: cve-2017-7960.patch
Patch2: cve-2017-7961.patch

%description
libcroco is a standalone css2 parsing library.
It provides a low level event driven SAC like api
and a css object model like api.

%package bin
Summary: bin components for the libcroco package.
Group: Binaries

%description bin
bin components for the libcroco package.


%package dev
Summary: dev components for the libcroco package.
Group: Development
Requires: libcroco-lib
Requires: libcroco-bin
Provides: libcroco-devel

%description dev
dev components for the libcroco package.


%package dev32
Summary: dev32 components for the libcroco package.
Group: Default
Requires: libcroco-lib32
Requires: libcroco-bin
Requires: libcroco-dev

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

%description lib
lib components for the libcroco package.


%package lib32
Summary: lib32 components for the libcroco package.
Group: Default

%description lib32
lib32 components for the libcroco package.


%prep
%setup -q -n libcroco-0.6.12
%patch1 -p1
%patch2 -p1
pushd ..
cp -a libcroco-0.6.12 build32
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1500994989
export CFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export FCFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export FFLAGS="$CFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
export CXXFLAGS="$CXXFLAGS -Os -fdata-sections -ffunction-sections -fno-semantic-interposition -fstack-protector-strong "
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
export LDFLAGS="$LDFLAGS -m32"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1500994989
rm -rf %{buildroot}
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
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
%defattr(-,root,root,-)
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
