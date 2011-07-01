%define api_version	3.0
%define lib_major 0
%define oname gtksourceview
%define libname	%mklibname %{oname}- %{api_version} %{lib_major}
%define libnamedev %mklibname -d %{oname}- %{api_version}

Summary:	Source code viewing library
Name:		gtksourceview3
Version: 3.0.5
Release:	%mkrel 1
License:	GPLv2+
Group:		Editors
URL:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.xz
Buildroot:	%{_tmppath}/%{oname}-%{version}
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:  libxml2-devel >= 2.6.0
BuildRequires:  gtk-doc
BuildRequires:  gobject-introspection-devel
BuildRequires:  intltool

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libname}
Summary:	Source code viewing library
Group:		Editors
Requires:	%{name} >= %{version}-%{release}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libnamedev}
Summary:        Libraries and include files for GtkSourceView
Group:          Development/GNOME and GTK+
Requires:       %{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	lib%{oname}-%{api_version}-devel = %{version}-%{release}

%description -n %{libnamedev}
GtkSourceView development files 


%prep
%setup -q -n %oname-%version

%build

%configure2_5x

%make

%install
rm -rf %{buildroot}

%makeinstall_std

%{find_lang} %{oname}-%{api_version}

%clean
rm -rf %{buildroot}

%files -f %{oname}-%{api_version}.lang
%defattr(-,root,root)
%doc AUTHORS NEWS README
%{_datadir}/gtksourceview-%{api_version}

%files -n %{libname} 
%defattr(-,root,root)
%{_libdir}/libgtksourceview-%{api_version}.so.%{lib_major}*
%{_libdir}/girepository-1.0/GtkSource-%{api_version}.typelib

%files -n %{libnamedev}
%defattr(-,root,root)
%doc %{_datadir}/gtk-doc/html/gtksourceview-%api_version
%{_libdir}/*.so
%attr(644,root,root) %{_libdir}/*.la
%{_includedir}/*
%{_libdir}/pkgconfig/*
%_datadir/gir-1.0/GtkSource-%{api_version}.gir
