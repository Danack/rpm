Name:	    GeoIP
Version:    1.4.8
Summary:    GeoIP is a C library finds the location of an IP address.
Release:    1
Group:	    System Environment/Libraries
URL:	    http://www.maxmind.com/app/c
Vendor:	    MaxMind LLC
Source0:    http://www.maxmind.com/download/geoip/api/c/GeoIP-%{version}.tar.gz
License:    GPL
BuildRoot:  %{_tmppath}/%{name}-%{version}-root

%description
GeoIP is a C library that enables the user to find geographical and
network information of an IP address.
Included is a free GeoLite Country database
that is updated at the beginning of every month.
To download the latest free GeoLite Country database, go to:
http://www.maxmind.com/app/geoip_country

There is also a free city-level geolocation database, GeoLite City,
available from:
http://www.maxmind.com/app/geolitecity

%package devel
Summary: GeoIP headers, libraries
Group: Development/Libraries
Requires: %name = %{version}

%description devel
This package contain the devel files for GeoIP.

%prep
%setup -q

%build
%configure \
    --enable-shared
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
%makeinstall
# Fixup permissions on shared libraries so that findreqs will work right.
chmod 755 $RPM_BUILD_ROOT/%{_libdir}/*
wget http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz
gunzip GeoLiteCity.dat.gz
mv GeoLiteCity.dat $RPM_BUILD_ROOT/%{_datadir}/GeoIP/GeoIPCity.dat

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%attr(0755,root,root) %{_libdir}/*.so.*.*
%{_bindir}/*
%{_sysconfdir}/*
%dir %{_datadir}/GeoIP
%{_datadir}/GeoIP/*
%{_libdir}/*.so
%{_libdir}/*.so.*
%{_mandir}/*/*

%files devel
%{_includedir}/*
%{_libdir}/*.a
%{_libdir}/*.la

%changelog
* Wed Jul 13 2011 Mike Willbanks <mike@digitalstruct.com>
- Initial RPM Build 1.4.8
