#
# TODO:
# - add man files
#
%define		orgname		kde-dev-scripts
%define		_state		stable
%define		qtver		4.8.1

Summary:	An set of scripts useful for building and maintaining KDE
Summary(pl.UTF-8):	Zestaw skryptów do kompilowania i utrzymywania KDE
Name:		kde4-%{orgname}
Version:	4.12.0
Release:	1
License:	GPL
Group:		X11/Development/Tools
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	64bd8e953e8e571e2bdbc71a266fa170
URL:		http://www.kde.org/
BuildRequires:	QtNetwork-devel >= %{qtver}
BuildRequires:	QtScriptTools-devel >= %{qtver}
BuildRequires:	antlr
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	boost-devel >= 1.35.0
BuildRequires:	bzip2-devel
BuildRequires:	cmake >= 2.8.0
BuildRequires:	db-devel
BuildRequires:	docbook-dtd42-xml
BuildRequires:	docbook-style-xsl
BuildRequires:	gettext-devel
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.600
BuildRequires:	subversion-devel >= 0.37.0
BuildRequires:	utempter-devel
Suggests:	/usr/bin/perl
Obsoletes:	kde4-kdesdk-scripts-cvs
Obsoletes:	kde4-kdesdk-scripts-developer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains:
- script that extracts strings in an application's .rc file, e.g.
  testappui.rc, and writes into the pot file
- script that counts lines of code, comments and blank space in C and
  C++ source files
- script for finding missing and packaging crystal icons.
- kdelnk to desktop and zonetab2pot converter
- set of kde-build scripts
- set of scripts that allow more comfortable profiling of KDE apps
- set of scripts to fix licence header/KDE includes directives and
  strip irrelevant tags from .ui files
- KDE man pages generator
- multi-frame PNG to MNG converter

%description -l pl.UTF-8
Ten pakiet zawiera:
- skrypt, który wyciąga łańcuchy z plików .rc aplikacji, np.
  testappgui.rc i zapisuje je do plików pot, z których tworzy się
  tłumaczenia (pliki po)
- skrypt zliczający linijki kodu, komentarzy i znaków białych w
  plikach źródłowych C i C++
- skrypt do wyszukiwania brakujących i pakietowania ikon z motywu
  crystal.
- konwerter plików kdelnk na desktop i zonetab na pot
- zestaw skryptów kde-build
- zestaw skryptów umożliwiających wygodne profilowanie aplikacji KDE
- zestaw skryptów do poprawiania nagłówków informujących o licencji i
  dyrektyw w plikach nagłówkowych KDE oraz usuwania nieistotnych
  znaczników z plików .ui
- generator stron man dla KDE
- konwerter wieloramkowych PNG na MNG

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_gimpdir}/palettes,%{_appdefsdir}}

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT \
        kde_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/adddebug
%attr(755,root,root) %{_bindir}/build-progress.sh
%attr(755,root,root) %{_bindir}/cheatmake
%attr(755,root,root) %{_bindir}/create_cvsignore
%attr(755,root,root) %{_bindir}/create_makefiles
%attr(755,root,root) %{_bindir}/create_svnignore
%attr(755,root,root) %{_bindir}/cvsaddcurrentdir
%attr(755,root,root) %{_bindir}/cvsbackport
%attr(755,root,root) %{_bindir}/cvsforwardport
%attr(755,root,root) %{_bindir}/cvslastlog
%attr(755,root,root) %{_bindir}/cvsrevertlast
%attr(755,root,root) %{_bindir}/cvsversion
%attr(755,root,root) %{_bindir}/findmissingcrystal
%attr(755,root,root) %{_bindir}/fix-include.sh
%attr(755,root,root) %{_bindir}/kdedoc
%attr(755,root,root) %{_bindir}/krazy-licensecheck
%attr(755,root,root) %{_bindir}/optimizegraphics
%attr(755,root,root) %{_bindir}/nonsvnlist
%attr(755,root,root) %{_bindir}/pruneemptydirs
%attr(755,root,root) %{_bindir}/qtdoc
%attr(755,root,root) %{_bindir}/svnbackport
%attr(755,root,root) %{_bindir}/svnforwardport
%attr(755,root,root) %{_bindir}/svnchangesince
%attr(755,root,root) %{_bindir}/svngettags
%attr(755,root,root) %{_bindir}/svnlastlog
%attr(755,root,root) %{_bindir}/svnrevertlast
%attr(755,root,root) %{_bindir}/wcgrep
%attr(755,root,root) %{_bindir}/draw_lib_dependencies
%attr(755,root,root) %{_bindir}/create_makefile
%attr(755,root,root) %{_bindir}/makeobj
%attr(755,root,root) %{_bindir}/cvscheck
%attr(755,root,root) %{_bindir}/cvslastchange
%attr(755,root,root) %{_bindir}/noncvslist
%attr(755,root,root) %{_bindir}/cvs-clean
%attr(755,root,root) %{_bindir}/cvsblame
%attr(755,root,root) %{_bindir}/colorsvn
%attr(755,root,root) %{_bindir}/svn-clean
%attr(755,root,root) %{_bindir}/svnlastchange
%attr(755,root,root) %{_bindir}/svnversions
%attr(755,root,root) %{_bindir}/extractrc
%attr(755,root,root) %{_bindir}/extractattr
%attr(755,root,root) %{_bindir}/zonetab2pot.py
%attr(755,root,root) %{_bindir}/fixkdeincludes
%attr(755,root,root) %{_bindir}/fixuifiles
%attr(755,root,root) %{_bindir}/includemocs
%attr(755,root,root) %{_bindir}/cxxmetric
%attr(755,root,root) %{_bindir}/extend_dmalloc
%attr(755,root,root) %{_bindir}/kdekillall
%attr(755,root,root) %{_bindir}/kdelnk2desktop.py
%attr(755,root,root) %{_bindir}/package_crystalsvg
%attr(755,root,root) %{_bindir}/png2mng.pl
%attr(755,root,root) %{_bindir}/kdemangen.pl
%attr(755,root,root) %{_bindir}/svnintegrate
%attr(755,root,root) %{_bindir}/kde_generate_export_header
%attr(755,root,root) %{_bindir}/kde-systemsettings-tree.py
%attr(755,root,root) %{_bindir}/reviewboard-am
%{_mandir}/man1/adddebug.1*
%{_mandir}/man1/cheatmake.1*
%{_mandir}/man1/create_cvsignore.1*
%{_mandir}/man1/create_makefile.1*
%{_mandir}/man1/create_makefiles.1*
%{_mandir}/man1/cvscheck.1*
%{_mandir}/man1/cvslastchange.1*
%{_mandir}/man1/cvslastlog.1*
%{_mandir}/man1/cvsrevertlast.1*
%{_mandir}/man1/cxxmetric.1*
%{_mandir}/man1/extend_dmalloc.1*
%{_mandir}/man1/extractrc.1*
%{_mandir}/man1/fixincludes.1*
%{_mandir}/man1/pruneemptydirs.1*
%{_mandir}/man1/qtdoc.1*
%{_mandir}/man1/reportview.1*
%{_mandir}/man1/transxx.1*
%{_mandir}/man1/zonetab2pot.py.1*
