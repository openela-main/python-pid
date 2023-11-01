%global srcname pid

Name:           python-%{srcname}
Version:        2.1.1
Release:        7%{?dist}
Summary:        PID file management library

License:        ASL 2.0
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/p/%{srcname}/%{srcname}-%{version}.tar.gz

BuildArch:      noarch

%description
pid provides a PidFile class that manages PID files. PidFile features:
  - stale detection
  - locking using fcntl
  - chmod (default is 0o644)
  - chown
  - custom exceptions

PidFile can also be used as a context manager or a decorator.

%package -n python3-%{srcname}
Summary:        PID file management library

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-nose

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
pid provides a PidFile class that manages PID files. PidFile features:
  - stale detection
  - locking using fcntl
  - chmod (default is 0o644)
  - chown
  - custom exceptions

PidFile can also be used as a context manager or a decorator.

%prep
%autosetup -n %{srcname}-%{version}
rm -rf *.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{srcname}
%license LICENSE
%doc AUTHORS CHANGELOG README.rst
%{python3_sitelib}/pid
%{python3_sitelib}/pid-*.egg-info

%changelog
* Thu Mar 22 2018 David Shea <dshea@redhat.com> - 2.1.1-7
- Remove the python2 package

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Jan 27 2018 Iryna Shcherbina <ishcherb@redhat.com> - 2.1.1-5
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 2.1.1-2
- Rebuild for Python 3.6

* Tue Nov 29 2016 David Shea <dshea@redhat.com> - 2.1.1-1
- Update to 2.1.1, which adds an optional allow_samepid parameter

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 03 2015 Robert Kuska <rkuska@redhat.com> - 2.0.1-3
- Rebuilt for Python3.5 rebuild

* Wed Aug 05 2015 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 2.0.1-2
- Update to modern python packaging guidelines

* Tue Aug  4 2015 David Shea <dshea@redhat.com> - 2.0.1-1
- Initial package
