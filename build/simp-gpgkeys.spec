Summary: GPGKEYS
Name: simp-gpgkeys
Version: 3.1.2
Release: 0
License: Public Domain
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildarch: noarch
Requires: facter

Prefix: %{_datadir}/simp/GPGKEYS

%description
A collection of GPG Keys Required for SIMP to function properly.

All keys copyright their respective owners.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

# Make your directories here.
mkdir -p %{buildroot}/%{_sysconfdir}/pki/rpm-gpg
mkdir -p %{buildroot}/%{prefix}

# Now install the files.
cp GPGKEYS/RPM-GPG-KEY-puppet* %{buildroot}/%{_sysconfdir}/pki/rpm-gpg
cp GPGKEYS/RPM-GPG-KEY-SIMP* %{buildroot}/%{_sysconfdir}/pki/rpm-gpg
cp GPGKEYS/* %{buildroot}/%{prefix}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%{_sysconfdir}/pki/rpm-gpg
%{prefix}

%post
#!/bin/bash
export PATH=/opt/puppetlabs/bin:$PATH

# If we're a SIMP server, place the keys into the appropriate web directory
if [ -d '/var/www/yum/SIMP' ]; then
  dir='/var/www/yum/SIMP/GPGKEYS'
  if [ ! -d $dir ]; then
    mkdir -p -m 0755 "${dir}"
  fi
  cp %{prefix}/RPM-GPG-KEY* "${dir}"

  # Get rid of any files that are present that aren't in the new directory.
  # Ensure that we don't have issues with operations in progress.
  old_key_list=`mktemp --suffix=.simp_gpgkeys`
  new_key_list=`mktemp --suffix=.simp_gpgkeys`

  find "${dir}" -name "RPM-GPG-KEY*" -maxdepth 1 -printf "%f\n" | sort -u > $old_key_list
  find "%{prefix}" -name "RPM-GPG-KEY*" -maxdepth 1 -printf "%f\n" | sort -u > $new_key_list

  for file in `comm -23 $old_key_list $new_key_list`; do
    if [ -f "${dir}/${file}" ]; then
      rm -f "${dir}/${file}"
    fi
  done

  if [ -f $old_key_list ]; then
    rm -f $old_key_list
  fi

  if [ -f $new_key_list ]; then
    rm -f $new_key_list
  fi

  # Link system GPG keys into SIMP repo
  if [ `facter operatingsystem` == 'CentOS' ]; then
    search_string='.*CentOS-[[:digit:]]'
  elif [ `facter operatingsystem` == 'RedHat' ]; then
    search_string='.*redhat.*release.*'
  else
    search_string=''
  fi
  if [ -n "$search_string" ]; then
    for file in `find /etc/pki/rpm-gpg/ -regextype posix-extended -regex ${search_string}`; do
      cp ${file} ${dir}
    done
  fi
  # Ensure GPG permissions
  chown -R root:48 ${dir}
  find ${dir} -type f -exec chmod 640 {} +
fi

%changelog
* Thu Apr 22 2021 Jeanne Greulich <jeanne.greulich@gmail.com> - 3.1.2-0
- Fixed a bug where the GPG keys were copied into /var/www/yum/SIMP/GPGKEYS/
  during the post install, even if /var/www/yum/SIMP/ did not exist.
- Fixed a bug where the copy of the GPG keys into /var/www/yum/SIMP/GPGKEYS/
  during the post install failed, when /var/www/yum/SIMP/ existed but
  /var/www/yum/SIMP/GPGKEYS/ did not exist.

* Tue Dec 17 2019 Jeanne Greulich <jeanne.greulich@gmail.com> - 3.1.1-0
- Added the CentOS8 and EPEL 8 GPGkeys

* Tue Apr 09 2019 Joseph Sharkey <shark.bruhaha@gmail.com> - 3.1.0-0
- Removed Elastic-search and Grafana GPG keys

* Mon Sep 17 2018 Brandon Riden <brandon.riden@onyxpoint.com> - 3.0.4-0
- Update SIMP-6 Release Key to include new signatures

* Fri Sep 22 2017 Liz Nemsick <lnemsick.simp@gmail.com> - 3.0.3-0
- Fix changelog/version mismatch which resulted in the release of
  a 3.0.2 tag for which the RPM version was actually 3.0.3.

* Wed Aug 23 2017 Nick Markowski <nmarkowski@keywcorp.com> - 3.0.2-0
- Removed postun section, which removed all keys from /var/www/yum/SIMP/GPGKEYS
  on upgrade.

* Mon Aug 21 2017 Liz Nemsick <lnemsick.simp@gmail.com> - 3.0.2-0
- Added the postgresql96 GPG key

* Fri Jun 09 2017 Nick Miller <nick.miller@onyxpoint.com> - 3.0.2-0
- simp-gpgkeys is now its own module
- Added a yaml file with a download source and a fingerprint to check cert integrity
  - And a travis file to check them

* Thu Mar 09 2017 Trevor Vaughan <tvaughan@onyxpoint.com> - 3.0.1-0
- Added the updated Grafana GPG key and renamed the old one to note its legacy
  status

* Fri Feb 24 2017 Trevor Vaughan <tvaughan@onyxpoint.com> - 3.0.0-1
- Only copy in the SIMP and Puppet GPG keys into the system trust chain.
  Copying more than that is too presumptive.
- Removed the 'dist' qualifier from the version since it was determined that
  the public GPG keys are OK to be common across all releases.

* Tue Feb 14 2017 Nick Miller <nick.miller@onyxpoint.com> - 3.0.0-0
- Added new puppet gpg key from http://yum.puppetlabs.com/RPM-GPG-KEY-puppet
- Ensure facter is in $PATH during post install

* Tue Oct 27 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.0-3
- Fixed some logic bugs in the %postinstall script

* Tue Jul 28 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.0-2
- Now install the GPG keys to /usr/share/simp/GPGKEYS and /etc/pki/rpm-gpg
- Copy the keys into the SIMP default web dirs if they exist and be sure to
  clean up after ourselves in the future.

* Sat Jun 27 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.0-1
- Added the OS version to differentiate between the versions.

* Mon May 25 2015 Trevor Vaughan <tvaughan@onyxpoint.com> - 2.0.0-0
- Initial Public Release
