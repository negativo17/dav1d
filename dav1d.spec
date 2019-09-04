Name:           dav1d
Version:        0.4.0
Release:        1%{?dist}
Summary:        AV1 cross-platform Decoder

License:        BSD
URL:            https://code.videolan.org/videolan/dav1d
Source0:        %url/-/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  nasm
BuildRequires:  doxygen
BuildRequires:  meson >= 0.47.0

%description
dav1d is a new AV1 cross-platform Decoder, open-source, and focused on speed
and correctness.

%package -n libdav1d
Summary:        Library files for dav1d

%description -n libdav1d
Library files for dav1d, the AV1 cross-platform Decoder.

%package -n libdav1d-devel
Summary:        Development files for dav1d
Requires:       libdav1d%{?_isa} = %{version}-%{release}

%description -n libdav1d-devel
Development files for dav1d, the AV1 cross-platform Decoder.

%prep
%autosetup -n %{name}-%{version}

%build
%meson --buildtype=release

%meson_build
%meson_build doc/html

%install
%meson_install

%check
%meson_test

%files
%license COPYING doc/PATENTS
%doc CONTRIBUTING.md NEWS README.md
%{_bindir}/dav1d

%files -n libdav1d
%license COPYING doc/PATENTS
%{_libdir}/libdav1d.so.2*

%files -n libdav1d-devel
%doc %{_host_alias}/doc/html
%{_includedir}/%{name}
%{_libdir}/libdav1d.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Fri Aug 09 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.4.0-1
- Release 0.4.0 (#1708919)

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Apr 29 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.0-1
- Release 0.3.0 (#1701494)

* Sun Apr 21 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.2.2-1
- Release 0.2.2 (#1701494)

* Tue Apr 16 2019 Adam Williamson <awilliam@redhat.com> - 0.2.1-3
- Rebuild with Meson fix for #1699099

* Tue Mar 26 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.2.1-2
- Rebuild with -Db_ndebug=true

* Tue Mar 12 2019 Robert-André Mauchin - 0.2.1-1
- Release 0.2.1

* Tue Mar 05 2019 Robert-André Mauchin - 0.2.0-1
- Release 0.2.0

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Dec 11 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-1
- Initial build
