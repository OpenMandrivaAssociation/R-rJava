%global packname  rJava
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9_3
Release:          1
Summary:          Low-level R to Java interface
Group:            Sciences/Mathematics
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-3.tar.gz
Requires:         R-methods
Requires:         java
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods
BuildRequires:    java-rpmbuild
BuildRequires:    x11-server-xvfb

%description
Low-level interface to Java VM very much like .C/.Call and friends. Allows
creation of objects, calling methods and accessing fields.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
xvfb-run %{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/java
%{rlibdir}/%{packname}/javadoc
%{rlibdir}/%{packname}/jri
%{rlibdir}/%{packname}/libs
