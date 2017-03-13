%{?scl:%scl_package nodejs-has-color}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:       %{?scl_prefix}nodejs-has-color
Version:    0.1.7
Release:    5%{?dist}
Summary:    Detects whether a terminal supports color
License:    MIT
URL:        https://github.com/sindresorhus/has-color
Source0:    http://registry.npmjs.org/has-color/-/has-color-%{version}.tgz
Source1:    https://raw.githubusercontent.com/sindresorhus/has-color/ab671b1f74846d9fb9caea8dc302603a865be3cc/test.js
# https://github.com/sindresorhus/has-color/pull/4
Source2:    LICENSE

BuildArch:  noarch
%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
%endif

%description
%{summary}.

%prep
%setup -q -n package
cp -p %{SOURCE1} .
cp -p %{SOURCE2} .

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/has-color
cp -pr package.json index.js \
    %{buildroot}%{nodejs_sitelib}/has-color

%nodejs_symlink_deps


%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
/usr/bin/mocha
%endif

%files
%doc LICENSE readme.md
%{nodejs_sitelib}/has-color

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.7-5
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.7-4
- Rebuilt with updated metapackage

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.7-3
- Enable scl macros

* Mon Sep 14 2015 Troy Dawson <tdawson@redhat.com> - 0.1.7-2
- Disable tests until all dependencies are built

* Sun Apr 20 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.7-1
- update to upstream release 0.1.7

* Thu Mar 13 2014 Jamie Nguyen <jamielinux@fedoraproject.org> - 0.1.4-1
- initial package
