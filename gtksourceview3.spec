%define api	3.0
%define major	0
%define oname	gtksourceview
%define libname	%mklibname %{oname}- %{api} %{major}
%define girname	%mklibname %{oname}-gir %{api}
%define devname %mklibname -d %{oname}- %{api}

Summary:	Source code viewing library
Name:		gtksourceview3
Version: 	3.6.1
Release:	1
License:	GPLv2+
Group:		Editors
URL:		http://people.ecsc.co.uk/~matt/downloads/rpms/gtksourceview/
Source0:	ftp://ftp.gnome.org/pub/GNOME/sources/%{oname}/3.6/%{oname}-%{version}.tar.xz
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

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n %{devname}
Summary:	Libraries and include files for GtkSourceView
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	%{oname}-%{api}-devel = %{version}-%{release}

%description -n %{devname}
GtkSourceView development files 

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x

%make LIBS='-lgmodule-2.0'

%install
%makeinstall_std

%{find_lang} %{oname}-%{api}

%files -f %{oname}-%{api}.lang
%doc AUTHORS NEWS README
%{_datadir}/gtksourceview-%{api}

%files -n %{libname} 
%{_libdir}/libgtksourceview-%{api}.so.%{major}*

%files -n %{girname} 
%{_libdir}/girepository-1.0/GtkSource-%{api}.typelib

%files -n %{devname}
%doc %{_datadir}/gtk-doc/html/gtksourceview-%{api}
%{_libdir}/*.so
%{_includedir}/*
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/GtkSource-%{api}.gir


%changelog
* Tue Oct 23 2012 Arkady L. Shane <ashejn@rosalab.ru> 3.6.0-1
- update to 3.6.0

* Thu May 17 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.4.2-1
+ Revision: 799324
- update to new version 3.4.2

* Fri May 04 2012 Guilherme Moro <guilherme@mandriva.com> 3.4.1-1
+ Revision: 796362
- Updated to version 3.4.1

* Sat Mar 10 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.2.3-1
+ Revision: 783797
- new version 3.2.3
- cleaned up spec
- remove dep loop

* Fri Jul 01 2011 Götz Waschk <waschk@mandriva.org> 3.0.5-1
+ Revision: 688478
- new version

* Sun Jun 19 2011 Götz Waschk <waschk@mandriva.org> 3.0.4-1
+ Revision: 686067
- new version
- xz tarball

* Sat Jun 18 2011 Götz Waschk <waschk@mandriva.org> 3.0.3-1
+ Revision: 685907
- new version

* Wed May 25 2011 Götz Waschk <waschk@mandriva.org> 3.0.2-1
+ Revision: 678982
- new version

* Tue Apr 26 2011 Funda Wang <fwang@mandriva.org> 3.0.1-1
+ Revision: 659124
- update to new version 3.0.1

* Tue Apr 05 2011 Funda Wang <fwang@mandriva.org> 3.0.0-1
+ Revision: 650454
- update to new version 3.0.0

* Wed Mar 23 2011 Funda Wang <fwang@mandriva.org> 2.91.9-1
+ Revision: 648018
- New version 2.91.9
  disable glade support as it requires glade4
  introspection warning not required with latest g-i

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.90.4-1mdv2011.0
+ Revision: 563661
- gtk+3 version

* Fri Jul 30 2010 Götz Waschk <waschk@mandriva.org> 2.11.2-1mdv2011.0
+ Revision: 563496
- update build deps
- new version
- add introspection support

* Sun Jul 11 2010 Götz Waschk <waschk@mandriva.org> 2.10.4-1mdv2011.0
+ Revision: 550812
- update to new version 2.10.4

* Wed Apr 28 2010 Christophe Fergeau <cfergeau@mandriva.com> 2.10.1-2mdv2010.1
+ Revision: 540346
- rebuild so that shared libraries are properly stripped again

* Mon Apr 26 2010 Götz Waschk <waschk@mandriva.org> 2.10.1-1mdv2010.1
+ Revision: 538922
- update to new version 2.10.1

* Sun Mar 28 2010 Götz Waschk <waschk@mandriva.org> 2.10.0-1mdv2010.1
+ Revision: 528497
- update to new version 2.10.0

* Wed Mar 17 2010 Götz Waschk <waschk@mandriva.org> 2.9.9-1mdv2010.1
+ Revision: 523305
- update to new version 2.9.9

* Mon Mar 01 2010 Götz Waschk <waschk@mandriva.org> 2.9.8-1mdv2010.1
+ Revision: 513136
- update to new version 2.9.8

* Mon Feb 22 2010 Götz Waschk <waschk@mandriva.org> 2.9.7-1mdv2010.1
+ Revision: 509802
- update to new version 2.9.7

* Mon Jan 25 2010 Götz Waschk <waschk@mandriva.org> 2.9.5-1mdv2010.1
+ Revision: 496484
- update to new version 2.9.5

* Tue Jan 12 2010 Götz Waschk <waschk@mandriva.org> 2.9.4-1mdv2010.1
+ Revision: 490117
- update to new version 2.9.4

* Wed Dec 09 2009 Götz Waschk <waschk@mandriva.org> 2.9.3-1mdv2010.1
+ Revision: 475488
- update build deps
- update to new version 2.9.3

* Mon Sep 28 2009 Götz Waschk <waschk@mandriva.org> 2.8.1-1mdv2010.0
+ Revision: 450709
- update to new version 2.8.1

* Mon Sep 21 2009 Götz Waschk <waschk@mandriva.org> 2.8.0-1mdv2010.0
+ Revision: 446726
- update to new version 2.8.0

* Mon Sep 14 2009 Götz Waschk <waschk@mandriva.org> 2.7.5-1mdv2010.0
+ Revision: 440951
- update to new version 2.7.5

* Sun Aug 23 2009 Götz Waschk <waschk@mandriva.org> 2.7.4-1mdv2010.0
+ Revision: 420183
- update to new version 2.7.4

* Tue Jul 28 2009 Götz Waschk <waschk@mandriva.org> 2.7.3-1mdv2010.0
+ Revision: 401390
- update to new version 2.7.3

* Sun Jul 19 2009 Götz Waschk <waschk@mandriva.org> 2.7.2-1mdv2010.0
+ Revision: 397895
- update to new version 2.7.2

* Tue May 26 2009 Götz Waschk <waschk@mandriva.org> 2.7.1-1mdv2010.0
+ Revision: 379942
- update to new version 2.7.1

* Sat May 16 2009 Götz Waschk <waschk@mandriva.org> 2.6.2-1mdv2010.0
+ Revision: 376420
- new version
- drop patch

* Tue Apr 14 2009 Götz Waschk <waschk@mandriva.org> 2.6.1-1mdv2009.1
+ Revision: 366973
- update to new version 2.6.1

* Sun Mar 15 2009 Götz Waschk <waschk@mandriva.org> 2.6.0-1mdv2009.1
+ Revision: 355375
- update to new version 2.6.0

* Mon Mar 02 2009 Götz Waschk <waschk@mandriva.org> 2.5.6-1mdv2009.1
+ Revision: 347284
- update to new version 2.5.6

* Sun Feb 15 2009 Götz Waschk <waschk@mandriva.org> 2.5.5-1mdv2009.1
+ Revision: 340569
- update to new version 2.5.5

* Tue Feb 03 2009 Götz Waschk <waschk@mandriva.org> 2.5.4-1mdv2009.1
+ Revision: 336732
- update to new version 2.5.4

* Mon Jan 19 2009 Götz Waschk <waschk@mandriva.org> 2.5.3-1mdv2009.1
+ Revision: 331392
- update to new version 2.5.3

* Tue Jan 06 2009 Götz Waschk <waschk@mandriva.org> 2.5.2-1mdv2009.1
+ Revision: 325233
- update to new version 2.5.2

* Sat Dec 27 2008 Götz Waschk <waschk@mandriva.org> 2.5.1-1mdv2009.1
+ Revision: 319938
- new version
- fix build

* Fri Nov 07 2008 Götz Waschk <waschk@mandriva.org> 2.4.1-2mdv2009.1
+ Revision: 300852
- rebuild for new libxcb

* Sat Nov 01 2008 Götz Waschk <waschk@mandriva.org> 2.4.1-1mdv2009.1
+ Revision: 299158
- update to new version 2.4.1

* Sat Sep 20 2008 Götz Waschk <waschk@mandriva.org> 2.4.0-1mdv2009.0
+ Revision: 286080
- new version

* Mon Sep 08 2008 Götz Waschk <waschk@mandriva.org> 2.3.3-1mdv2009.0
+ Revision: 282762
- new version

* Sun Aug 31 2008 Götz Waschk <waschk@mandriva.org> 2.3.2-1mdv2009.0
+ Revision: 277896
- new version

* Mon Aug 11 2008 Götz Waschk <waschk@mandriva.org> 2.3.1-1mdv2009.0
+ Revision: 270640
- new version

* Sat Aug 09 2008 Götz Waschk <waschk@mandriva.org> 2.3.0-1mdv2009.0
+ Revision: 270093
- new version
- update license
- don't depend on gnomeprint anymore

* Mon Jun 23 2008 Götz Waschk <waschk@mandriva.org> 2.2.2-1mdv2009.0
+ Revision: 227969
- new version

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Apr 09 2008 Götz Waschk <waschk@mandriva.org> 2.2.1-1mdv2009.0
+ Revision: 192472
- new version

* Mon Mar 10 2008 Götz Waschk <waschk@mandriva.org> 2.2.0-1mdv2008.1
+ Revision: 183387
- new version

* Mon Feb 25 2008 Götz Waschk <waschk@mandriva.org> 2.1.3-1mdv2008.1
+ Revision: 174978
- new version

* Tue Feb 05 2008 Götz Waschk <waschk@mandriva.org> 2.1.2-1mdv2008.1
+ Revision: 162620
- new version

* Tue Jan 29 2008 Götz Waschk <waschk@mandriva.org> 2.1.1-1mdv2008.1
+ Revision: 159723
- new version

* Mon Jan 14 2008 Götz Waschk <waschk@mandriva.org> 2.1.0-1mdv2008.1
+ Revision: 151726
- fix buildrequires
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Götz Waschk <waschk@mandriva.org> 2.0.2-1mdv2008.1
+ Revision: 113311
- new version

* Wed Oct 17 2007 Götz Waschk <waschk@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 99555
- new version

* Mon Sep 17 2007 Götz Waschk <waschk@mandriva.org> 2.0.0-1mdv2008.0
+ Revision: 88995
- new version
- update file list

* Mon Sep 10 2007 Götz Waschk <waschk@mandriva.org> 1.90.5-1mdv2008.0
+ Revision: 84189
- new version

* Thu Aug 30 2007 Götz Waschk <waschk@mandriva.org> 1.90.4-2mdv2008.0
+ Revision: 75310
- remove wrong obsoletes

* Tue Aug 28 2007 Götz Waschk <waschk@mandriva.org> 1.90.4-1mdv2008.0
+ Revision: 72490
- new version
- new devel name

* Wed Aug 01 2007 Götz Waschk <waschk@mandriva.org> 1.90.3-1mdv2008.0
+ Revision: 57377
- new version

* Wed Jul 04 2007 Götz Waschk <waschk@mandriva.org> 1.90.2-1mdv2008.0
+ Revision: 47927
- new version
- update file list

* Tue Jun 19 2007 Götz Waschk <waschk@mandriva.org> 1.90.1-1mdv2008.0
+ Revision: 41284
- new version
- new version
- new API version

  + Anssi Hannula <anssi@mandriva.org>
    - rebuild with correct optflags

