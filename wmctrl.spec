#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : wmctrl
Version  : 1.07
Release  : 2
URL      : http://tripie.sweb.cz/utils/wmctrl/dist/wmctrl-1.07.tar.gz
Source0  : http://tripie.sweb.cz/utils/wmctrl/dist/wmctrl-1.07.tar.gz
Summary  : Control your EWMH compliant window manager from command line
Group    : Development/Tools
License  : GPL-2.0
Requires: wmctrl-bin = %{version}-%{release}
Requires: wmctrl-license = %{version}-%{release}
Requires: wmctrl-man = %{version}-%{release}
BuildRequires : glib-dev
BuildRequires : libXmu-dev
BuildRequires : pkgconfig(x11)

%description
wmctrl
A command line tool to interact with an EWMH/NetWM compatible X Window Manager.

%package bin
Summary: bin components for the wmctrl package.
Group: Binaries
Requires: wmctrl-license = %{version}-%{release}

%description bin
bin components for the wmctrl package.


%package license
Summary: license components for the wmctrl package.
Group: Default

%description license
license components for the wmctrl package.


%package man
Summary: man components for the wmctrl package.
Group: Default

%description man
man components for the wmctrl package.


%prep
%setup -q -n wmctrl-1.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1561307592
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1561307592
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/wmctrl
cp COPYING %{buildroot}/usr/share/package-licenses/wmctrl/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/wmctrl

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/wmctrl/COPYING

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/wmctrl.1
