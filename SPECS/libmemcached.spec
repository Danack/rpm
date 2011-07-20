Name:      libmemcached
Summary:   memcached C library and command line tools
Version:   0.50
Release:   1
License:   BSD
Group:     System Environment/Libraries
URL:       http://launchpad.net/libmemcached
Source0:   http://download.tangent.org/libmemcached-%{version}.tar.gz
BuildRequires: memcached
Requires:  libevent >= 1.4.14
# For test suite

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


%description
libmemcached is a C client library to the memcached server
(http://danga.com/memcached). It has been designed to be light on memory
usage, and provide full access to server side methods.

%package devel
Summary: Header files and development libraries for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
This package contains the header files and development libraries
for %{name}. If you like to develop programs using %{name}, 
you will need to install %{name}-devel.


%prep
%setup -q

%{__mkdir} examples
%{__cp} tests/*.{c,cpp,h} examples/


%build
%configure \
    --enable-shared
%{__make} %{_smp_mflags}


%install
%{__rm} -rf %{buildroot}
%{__make} install  DESTDIR="%{buildroot}" AM_INSTALL_PROGRAM_FLAGS=""


%check
# test suite cannot run in mock (same port use for memcache server on all arch)
# 1 test seems to fail.. 
#%{__make} test


%clean
%{__rm} -rf %{buildroot}


%post -p /sbin/ldconfig


%postun -p /sbin/ldconfig
 

%files
%defattr (-,root,root,-) 
%doc AUTHORS COPYING NEWS README THANKS TODO
%{_bindir}/mem*
%{_libdir}/*.so.*
%{_mandir}/man1/*

%files devel
%defattr (-,root,root,-) 
%doc examples
%{_includedir}/libmemcached/*
%{_includedir}/libhashkit/*
%{_libdir}/*.so
%{_libdir}/*.la
%{_libdir}/pkgconfig/libmemcached.pc
%{_mandir}/man3/*

%changelog
* Wed Jul 13 2011 Mike Willbanks <mike@digitalstruct.com> - 0.50-1
- Updated for libmemcached 0.50
