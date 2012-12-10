%define fname gdgeda

%define major 6
%define libname %mklibname %{fname} %{major}
%define develname %mklibname -d %{fname}

Summary:	Graphical libraries for the gEDA project
Name:		lib%{fname}
Version:	2.0.15
Release:	10
Group:		Sciences/Other
License:	LGPL 
Url:		http://www.geda.seul.org
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	pkgconfig(zlib)
BuildRequires:  pkgconfig(libpng)

%description
Libgdgeda is a hack on libgd, which is a graphics library.  It allows your
code to quickly draw images complete with lines, arcs, text, multiple
colors, cut and paste from other images, and flood fills, and write out
the result as a .PNG file.

%package -n %{libname}
Summary:	Graphical libraries for the gEDA project
Group:		Sciences/Other

%description -n %{libname}
Libgdgeda is a hack on libgd, which is a graphics library.  It allows your
code to quickly draw images complete with lines, arcs, text, multiple
colors, cut and paste from other images, and flood fills, and write out
the result as a .PNG file.

%package -n %{develname}
Summary:	Graphical development libraries for the gEDA project
Group:		Development/C
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
This package contains libgdgeda header files that are needed for
development.
Libgdgeda is a hack on libgd, which is a graphics library. It allows your
code to quickly draw images complete with lines, arcs, text, multiple
colors, cut and paste from other images, and flood fills, and write out
the result as a .PNG file.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/libgdgeda-config

%files -n %{libname}
%{_libdir}/libgdgeda.so.%{major}*

%files -n %{develname}
%{_bindir}/libgdgeda-config
%{_libdir}/pkgconfig/%{name}.pc
%{multiarch_bindir}/libgdgeda-config
%{_libdir}/libgdgeda.so
%{_libdir}/libgdgeda.a
%{_includedir}/gdgeda

