# $Id$
Name:           libevent
Version:        1.4.14b
Release:        1
Summary:        Abstract asynchronous event notification library

Group:          System Environment/Libraries
License:        BSD
URL:            http://monkey.org/~provos/libevent/
Source0:        http://monkey.org/~provos/libevent-%{version}-stable.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-stable-%{release}-root-%(%{__id_u} -n)

%description
The libevent API provides a mechanism to execute a callback function
when a specific event occurs on a file descriptor or after a timeout
has been reached. libevent is meant to replace the asynchronous event
loop found in event driven network servers. An application just needs
to call event_dispatch() and can then add or remove events dynamically
without having to change the event loop.

%package devel
Summary: Header files, libraries and development documentation for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs using %{name},
you will need to install %{name}-devel.


%prep
%setup -q -n %{name}-%{version}-stable

%build
%configure \
    --disable-dependency-tracking --enable-shared
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0755)
%doc README
%{_libdir}/libevent-*.so.*
%{_libdir}/libevent_core-*.so.*
%{_libdir}/libevent_extra-*.so.*

%files devel
%defattr(-,root,root,0755)
%doc sample/*.c
%{_includedir}/event.h
%{_includedir}/evdns.h
%{_includedir}/evhttp.h
%{_includedir}/evrpc.h
%{_includedir}/evutil.h
%{_includedir}/event-config.h
%{_libdir}/libevent*

%{_bindir}/event_rpcgen.py

%{_mandir}/man3/*

%changelog
* Wed Jul 13 2011 Mike Willbanks <mike@digitalstruct.com> - 1.4.14b
- Updated for version 1.4.14b-stable
