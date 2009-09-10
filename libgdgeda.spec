%define fname gdgeda
%define name lib%{fname}
%define version 2.0.15
%define release %mkrel 8

%define major 6
%define libname %mklibname %fname %major

Summary: 	Graphical libraries for the gEDA project
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
Source:		%{name}-%{version}.tar.bz2
Url:		http://www.geda.seul.org
License:	LGPL 
Group: 		Sciences/Other
BuildRoot:    	%{_tmppath}/%{name}-buildroot
BuildRequires:  zlib >= 1.1
BuildRequires:  libpng >= 1.0

%description
Libgdgeda is a hack on libgd, which is a graphics library.  It allows your
code to quickly draw images complete with lines, arcs, text, multiple
colors, cut and paste from other images, and flood fills, and write out
the result as a .PNG file.

%package -n %libname
Summary:        Graphical libraries for the gEDA project
Group:          Sciences/Other
Obsoletes:	libgdgeda
Provides: 	libgdgeda = %version-%release

%description -n %libname
Libgdgeda is a hack on libgd, which is a graphics library.  It allows your
code to quickly draw images complete with lines, arcs, text, multiple
colors, cut and paste from other images, and flood fills, and write out
the result as a .PNG file.

%package -n %libname-devel
Summary:	Graphical development libraries for the gEDA project
Group:		Development/C
Obsoletes: libgdgeda-devel
Provides: libgdgeda-devel = %version-%release
Requires: %libname = %version

%description -n %libname-devel
This package contains libgdgeda header files that are needed for
development.
Libgdgeda is a hack on libgd, which is a graphics library. It allows your
code to quickly draw images complete with lines, arcs, text, multiple
colors, cut and paste from other images, and flood fills, and write out
the result as a .PNG file.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
%configure
%make

%install
%makeinstall
./libtool --finish $RPM_BUILD_ROOT/%{_libdir}

%multiarch_binaries %{buildroot}%{_bindir}/libgdgeda-config

%if %mdkversion < 200900
%post -n %libname -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libname -p /sbin/ldconfig
%endif

%clean
rm -Rf $RPM_BUILD_ROOT

%files -n %libname
%defattr(-,root,root)
%doc COPYING README.1ST README.TXT
%{_libdir}/libgdgeda.so.%major
%{_libdir}/libgdgeda.so.%{major}.0.0

%files -n %libname-devel
%defattr(-,root,root)
%_bindir/*
%{_libdir}/pkgconfig/%{name}.pc
%multiarch %{multiarch_bindir}/*-config
%{_libdir}/libgdgeda.so
%{_libdir}/libgdgeda.a
%{_libdir}/libgdgeda.la
%dir %{_includedir}/gdgeda
%{_includedir}/gdgeda/*


