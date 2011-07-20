Summary: Gearman Server and C Library
Name: gearmand
Version: 0.23
Release: 1
License: BSD
Group: System Environment/Libraries
BuildRequires: gcc-c++
Requires: libevent >= 1.4.14
Requires: boost >= 1.46
URL: http://www.gearman.org/

Packager: Brian Aker <brian@tangent.org>

Source: http://launchpad.net/gearmand/trunk/%{version}/+download/gearmand-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gearman provides a generic framework to farm out work to other machines, dispatching function calls to machines that are better suited to do work, to do work in parallel, to load balance processing, or to call functions between languages.

%prep
%setup -q

%configure \
    --enable-shared --disable-libmemcached

%build
%{__make} %{_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""
mkdir -p %{buildroot}/etc/init.d
mkdir -p %{buildroot}/etc/sysconfig
cp /usr/src/redhat/SOURCES/init.d/gearmand %{buildroot}/etc/init.d/gearmand
cp /usr/src/redhat/SOURCES/sysconfig/gearmand %{buildroot}/etc/sysconfig/gearmand

%clean
%{__rm} -rf %{buildroot}

%files
/etc/init.d/gearmand
/etc/sysconfig/gearmand
%{_bindir}/*
%{_sbindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*

%pre
mkdir -p /var/run/gearmand/
mkdir -p /opt/gearmand/

%post
echo "/usr/local/lib" > /etc/ld.so.conf.d/gearmand.conf
chkconfig --add gearmand
chkconfig --level 2345 gearmand on
getent group gearmand >/dev/null || groupadd -r gearmand
getent passwd gearmand >/dev/null || useradd -r -g gearmand -s /bin/bash -c "Gearmand Application User" gearmand
/sbin/ldconfig


%changelog
* Tue Jul 12 2011 Mike Willbanks <mike@digitalstruct.com> - 0.23-1
- updated gearmand and library to 0.23
