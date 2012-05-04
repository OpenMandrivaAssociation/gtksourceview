%define api	3.0
%define major 0
%define oname gtksourceview
%define libname	%mklibname %{oname}- %{api} %{major}
%define girname	%mklibname %{oname}-gir %{api}
%define develname %mklibname -d %{oname}- %{api}

Summary:	Source code viewing library
Name:		gtksourceview3
Version: 	3.4.1
Release:	1
License:	GPLv2+
Group:		Editors
URL:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/%{oname}-%{version}.tar.xz
BuildRequires:  intltool
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(libxml-2.0)

%description
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{libname}
Summary:	Source code viewing library
Group:		Editors
Requires:	%{name} = %{version}-%{release}

%description -n %{libname}
GtkSourceview is a library that adds syntax highlighting,
line numbers, and other programming-editor features.
GtkSourceView specializes these features for a code editor.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{develname}
Summary:	Libraries and include files for GtkSourceView
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{oname}-%{api}-devel = %{version}-%{release}

%description -n %{develname}
GtkSourceView development files 

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x

%make LIBS='-lgmodule-2.0'

%install
rm -rf %{buildroot}
%makeinstall_std

%{find_lang} %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS NEWS README
%{_datadir}/gtksourceview-%{api}

%files -n %{libname} 
%{_libdir}/libgtksourceview-%{api}.so.%{major}*

%files -n %{girname} 
%{_libdir}/girepository-1.0/GtkSource-%{api}.typelib

%files -n %{develname}
%doc %{_datadir}/gtk-doc/html/gtksourceview-%{api}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/GtkSource-%{api}.gir
