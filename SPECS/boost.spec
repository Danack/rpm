# $Id$
Name:           boost
Version:        1.47.0
Release:        1
Summary:        The Boost C++ headers and shared development libraries

Group:          System Environment/Libraries
License:        Boost
URL:            http://www.boost.org/
Source0:        boost_1_47_0.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  bzip2-devel, python-devel, python-libs
Requires: bzip2, python-libs
%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

%prep
%setup -q -n boost_1_47_0

%build
BOOST_ROOT=`pwd`
export BOOST_ROOT
./bootstrap.sh --prefix=$RPM_BUILD_ROOT/usr/local --with-toolset=gcc --with-icu

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/local
./b2 install

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,0644)
/usr/local/lib/libboost_*
/usr/local/include/boost/*

%changelog
* Tue Jul 12 2011 Mike Willbanks <mike@digitalstruct.com> - 1.47.1
- Build 1.47.1 for boost 1.47.0
* Thu May  5 2011 Mike Willbanks <mike@digitalstruct.com> - 1.46.1
- Initial build
