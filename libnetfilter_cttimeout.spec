Name:           libnetfilter_cttimeout
Version:        1.0.0
Release:        6%{?dist}
Summary:        Timeout policy tuning for Netfilter/conntrack
Group:          System Environment/Libraries
License:        GPLv2+
URL:            http://netfilter.org
Source0:        http://netfilter.org/projects/%{name}/files/%{name}-%{version}.tar.bz2

BuildRequires:  libmnl-devel >= 1.0.0, pkgconfig, kernel-headers

%description
This infrastructure allows you to define fine-grain timeout
policies per flow. Basically, from user-space, you can create
timeout policy objects via nfct_timeout_alloc(), set the
policy attributes, via nfct_timeout_*_attr_set(), and then
build the ctnetlink message to communicate this new timeout
policy to the kernel.

%package        devel
Summary:        Timeout policy tuning for Netfilter/conntrack
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       libmnl-devel >= 1.0.0
Requires:       kernel-headers

%description    devel
This infrastructure allows you to define fine-grain timeout
policies per flow. Basically, from user-space, you can create
timeout policy objects via nfct_timeout_alloc(), set the
policy attributes, via nfct_timeout_*_attr_set(), and then
build the ctnetlink message to communicate this new timeout
policy to the kernel.

%prep
%setup -q

%build
%configure --disable-static

make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc COPYING README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_includedir}/libnetfilter_cttimeout
%{_includedir}/libnetfilter_cttimeout/*.h

%changelog
* Fri Jun 19 2015 Paul Wouters <pwouters@redhat.com> - 1.0.0-6
- Resolves: rhbz#1233221 Add libnetfilter_cttimeout package to RHEL-7
