%global packname  rJava
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          0.9.4
Release:          3
Summary:          Low-level R to Java interface
Group:            Sciences/Mathematics
License:          GPL-2
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/rJava_0.9-4.tar.gz
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


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.9_3-1
+ Revision: 777807
- Import R-rJava
- Import R-rJava


